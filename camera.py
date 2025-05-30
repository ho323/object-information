import pyrealsense2 as rs
import numpy as np
import cv2

class RealSenseCamera:
    def __init__(self, width=640, height=480, fps=30):
        self.width = width
        self.height = height
        self.fps = fps
        
        # 카메라 초기화
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, fps)
        self.config.enable_stream(rs.stream.depth, width, height, rs.format.z16, fps)
        
        # 파이프라인 시작
        self.profile = self.pipeline.start(self.config)
        self.depth_scale = self.profile.get_device().first_depth_sensor().get_depth_scale()
        self.align = rs.align(rs.stream.color)
        
        # 필터 설정
        self.spatial = rs.spatial_filter()
        self.temporal = rs.temporal_filter()
        self.hole_filling = rs.hole_filling_filter()

    def get_frames(self):
        frames = self.pipeline.wait_for_frames()
        frames = self.align.process(frames)
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        
        if not depth_frame or not color_frame:
            return None, None
            
        # 깊이 필터링
        depth_frame = self.spatial.process(depth_frame)
        depth_frame = self.temporal.process(depth_frame)
        depth_frame = self.hole_filling.process(depth_frame)
        
        # 이미지 변환
        depth_img = np.asanyarray(depth_frame.get_data()).astype(np.float32)
        color_img = np.asanyarray(color_frame.get_data())
        depth_cm = depth_img * self.depth_scale * 100.0
        
        return color_img, depth_cm, depth_frame

    def get_depth_colormap(self, depth_cm):
        depth_vis = cv2.convertScaleAbs(depth_cm, alpha=0.5)
        depth_colormap = cv2.applyColorMap(depth_vis.astype(np.uint8), cv2.COLORMAP_JET)
        return depth_colormap

    def stop(self):
        self.pipeline.stop() 