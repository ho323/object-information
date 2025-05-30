import numpy as np

def depth_to_pointcloud(depth_region_cm, focal_length_px):
    h, w = depth_region_cm.shape
    u = np.linspace(0, w - 1, w)
    v = np.linspace(0, h - 1, h)
    uu, vv = np.meshgrid(u, v)

    z = depth_region_cm
    x = (uu - w / 2) * z / focal_length_px
    y = (vv - h / 2) * z / focal_length_px
    points = np.stack([x, y, z], axis=-1).reshape(-1, 3)
    return points

def safe_point(x, y, img_shape):
    h, w = img_shape[:2]
    x = min(max(x, 0), w - 1)
    y = min(max(y, 0), h - 1)
    return x, y 