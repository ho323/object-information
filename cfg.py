import random
import torch


DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
DISPLAY_FPS = 30
FRAME_MARGIN = 50

# ================== 물체 인식 모델 ================== #
# COCO 클래스 목록
COCO_CLASSES = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant',
    'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog',
    'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe',
    'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
    'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat',
    'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot',
    'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
    'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop',
    'mouse', 'remote', 'keyboard', 'cell phone', 'microwave',
    'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock',
    'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

random.seed(42)
CLASS_COLORS = [(random.random(), random.random(), random.random()) for _ in range(len(COCO_CLASSES))]
OD_MODEL_PATH = "./checkpoints/yolov8x.pt"


# ================== 세그멘테이션 모델 ================== #
SAM_MODEL_PATH = "./checkpoints/sam_vit_b_01ec64.pth"


# ================== 재료 분류 모델 ================== #
MATARIALS_MODEL_PATH = "./checkpoints/material_classification_efficientnet_minc.pth" 
MTR_CATEGORY = [
    "brick",
    "carpet",
    "ceramic",
    "fabric",
    "foliage",
    "food",
    "glass",
    "hair",
    "leather",
    "metal",
    "mirror",
    "other",
    "painted",
    "paper",
    "plastic",
    "polishedstone",
    "skin",
    "sky",
    "stone",
    "tile",
    "wallpaper",
    "water",
    "wood",
    ]

# 밀도 (g/cm³)
DENSITIES = {
        "brick": 1.8,
        "carpet": 0.3,
        "ceramic": 2.4,
        "fabric": 0.6,
        "foliage": 0.5,
        "food": 1.0,
        "glass": 2.5,
        "hair": 0.03,
        "leather": 0.9,
        "metal": 7.8,
        "mirror": 2.5,
        "other": 1.0,
        "painted": 1.3,
        "paper": 0.8,
        "plastic": 1.2,
        "polishedstone": 2.7,
        "skin": 1.1,
        "sky": 0.0012,  #공기 
        "stone": 2.7,
        "tile": 2.0,
        "wallpaper": 0.7,
        "water": 1.0,
        "wood": 0.6
    }