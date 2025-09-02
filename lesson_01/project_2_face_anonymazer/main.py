import os
import argparse

import cv2
import mediapipe as mp

def process_image(img, face_detection):
    H, W, _ = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box
            
            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)

            #blur faces
            img[y1:y1+h, x1:x1+w, :] = cv2.blur(img[y1:y1+h, x1:x1+w, :], (30, 30))
        
        return img
    
args = argparse.ArgumentParser()
#image
#args.add_argument("--mode", default='image')
#args.add_argument("--filePath", default='./data/person.jpg.mp4')
#video
#args.add_argument("--mode", default='video')
#args.add_argument("--filePath", default='./data/testVideo.mp4')
#webcam
args.add_argument("--mode", default='webcam')
args.add_argument("--filePath", default=None)

args = args.parse_args()

output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# detect faces
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    if args.mode in ['image']:
        # read image
        img = cv2.imread(args.filePath)
        img = process_image(img, face_detection)
        # save image
        cv2.imwrite(os.path.join(output_dir, 'output.png'), img)

    elif args.mode in ['video']:
        cap = cv2.VideoCapture(args.filePath)
        ret, frame = cap.read()

        output_video = cv2.VideoWriter(os.path.join(output_dir, 'output.mp4'),
                                       cv2.VideoWriter_fourcc(*'MP4V'),
                                       25,
                                       (frame.shape[1], frame.shape[0]))
        
        while ret:
            frame = process_image(frame, face_detection)
            output_video.write(frame)
            ret, frame = cap.read()

        cap.release()
        output_video.release()

    elif args.mode in ['webcam']:
        cap = cv2.VideoCapture(0)

        ret, frame = cap.read()
        while ret:
            frame = process_image(frame, face_detection)

            cv2.imshow('frame', frame)
            cv2.waitKey(25)

            ret, frame = cap.read()

        cap.release()


#print(out.detections)
    # [label_id: 0
    # score: 0.9693199396133423
    # location_data {
    # format: RELATIVE_BOUNDING_BOX
    # relative_bounding_box {
    #     xmin: 0.3814805746078491
    #     ymin: 0.21209096908569336
    #     width: 0.32548582553863525
    #     height: 0.21699073910713196
    # }
    # relative_keypoints {
    #     x: 0.46973246335983276
    #     y: 0.26222196221351624
    # }
    # relative_keypoints {
    #     x: 0.6189945936203003
    #     y: 0.269063800573349
    # }
    # relative_keypoints {
    #     x: 0.5412529110908508
    #     y: 0.3112516701221466
    # }
    # relative_keypoints {
    #     x: 0.5368944406509399
    #     y: 0.35967883467674255
    # }
    # relative_keypoints {
    #     x: 0.3823986053466797
    #     y: 0.28522875905036926
    # }
    # relative_keypoints {
    #     x: 0.701628565788269
    #     y: 0.2986412048339844
    # }
    # }
    # ]