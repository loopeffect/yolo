from ultralytics import YOLO
#import cv2
model = YOLO("C:\\Users\\hasna\\OneDrive\\Desktop\\yolov8\\best3.pt")  # load a pretrained model (recommended for training)
model.predict(source="0" , show=True, conf=0.5)