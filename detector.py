import cv2
import torch
from ultralytics import YOLO
import cfg

class ObjectDetector:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = YOLO(cfg.OD_MODEL_PATH).to(self.device)
        
    def detect(self, image, conf_threshold=0.7):
        results = self.model(image, conf=conf_threshold, verbose=False)
        return results[0].boxes.data.cpu().numpy()
        
    def process_detection(self, det, depth_cm, color_img, intrinsics):
        x1, y1, x2, y2, conf, cls = map(int, det[:6])
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        # 프레임 범위 체크
        frame_h, frame_w = depth_cm.shape
        margin = cfg.FRAME_MARGIN
        if x1 < margin or y1 < margin or x2 > (frame_w - margin) or y2 > (frame_h - margin):
            return color_img

        label = self.model.names[int(cls)]
        z_center = depth_cm[cy, cx]
        delta_x = abs(x2 - x1)
        delta_y = abs(y2 - y1)
        fx, fy = intrinsics.fx, intrinsics.fy

        if z_center > 0:
            width_cm = (delta_x * z_center) / fx
            height_cm = (delta_y * z_center) / fy
        else:
            width_cm, height_cm = None, None

        # 시각화
        cv2.rectangle(color_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(color_img, f"{label}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        if width_cm and height_cm:
            cv2.putText(color_img, f"W: {width_cm:.1f}cm", (x1, y2 + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
            cv2.putText(color_img, f"H: {height_cm:.1f}cm", (x2 + 10, y1 + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
            area_cm2 = width_cm * height_cm
            cv2.putText(color_img, f"Area: {area_cm2:.1f} cm2", (x1, y2 + 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

        return color_img 