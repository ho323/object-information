import cfg
import cv2
import numpy as np
from camera import RealSenseCamera
from detector import ObjectDetector

def main():
    # 초기화
    camera = RealSenseCamera(width=cfg.DISPLAY_WIDTH, height=cfg.DISPLAY_HEIGHT, fps=cfg.DISPLAY_FPS)
    detector = ObjectDetector()
    save_count = 0
    cv2.namedWindow('YOLO + RealSense 측정')

    try:
        prev_time = 0
        while True:
            # 프레임 획득
            color_img, depth_cm, depth_frame = camera.get_frames()
            if color_img is None or depth_cm is None:
                continue

            # 객체 감지
            detections = detector.detect(color_img)
            for det in detections:
                intrinsics = depth_frame.profile.as_video_stream_profile().get_intrinsics()
                color_img = detector.process_detection(det, depth_cm, color_img, intrinsics)

            # 깊이 시각화
            depth_colormap = camera.get_depth_colormap(depth_cm)
            if depth_colormap.shape != color_img.shape:
                depth_colormap = cv2.resize(depth_colormap, (color_img.shape[1], color_img.shape[0]))

            # FPS 계산 및 표시
            current_time = cv2.getTickCount()
            fps = cv2.getTickFrequency() / (current_time - prev_time)
            prev_time = current_time
            cv2.putText(color_img, f"FPS: {fps:.1f}", (color_img.shape[1]-120, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

            # 결과 표시
            combined = np.hstack((color_img, depth_colormap))
            cv2.imshow('YOLO + RealSense 측정', combined)

            # 키 입력 처리
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            elif key == ord('s'):
                filename = f"output_{save_count}.png"
                cv2.imwrite('./output/'+filename, combined)
                print(f"[저장됨] {filename}")
                save_count += 1

    finally:
        camera.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
