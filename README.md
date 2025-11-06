# 객체 감지 및 측정 시스템
RGB-D 카메라를 사용하여 실시간으로 객체를 감지하고 크기를 측정하는 시스템입니다.  
시연 영상 : https://youtu.be/aHTMQaz42Nk    
<img width="758" height="611" alt="image" src="https://github.com/user-attachments/assets/5a40bf54-d1a9-427b-8ef9-7b173ce898e3" />  


## 주요 기능

- RealSense 카메라를 통한 실시간 RGB-D 영상 획득
- YOLO를 사용한 객체 감지
- 감지된 객체의 실제 크기 측정 (너비, 높이, 면적)

## 시스템 요구사항

- Python 3.10 이상
- CUDA 지원 GPU (권장)
- Intel RealSense 카메라 (D435/D455 권장)

## 설치 방법

1. 저장소 클론
```bash
git clone https://github.com/ho323/object-information
cd object-information
```

2. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

3. YOLO 모델 다운로드
```bash
# YOLO 모델 파일을 cfg.OD_MODEL_PATH에 지정된 경로에 다운로드
```

## 사용 방법

1. RealSense 카메라 연결
2. 프로그램 실행
```bash
python main.py
```

3. 키보드 단축키
- `q`: 프로그램 종료
- `s`: 현재 화면 저장

## 프로젝트 구조

```
.
├── main.py          # 메인 실행 파일
├── camera.py        # RealSense 카메라 제어
├── detector.py      # YOLO 객체 감지
├── utils.py         # 유틸리티 함수
├── cfg.py          # 설정 파일
└── requirements.txt # 필요한 패키지 목록
```

## 모듈 설명

### camera.py
- RealSense 카메라 초기화 및 제어
- RGB-D 영상 획득
- 깊이 필터링 및 처리

### detector.py
- YOLO 모델을 사용한 객체 감지
- 감지된 객체의 크기 측정
- 시각화 기능

### utils.py
- 3D 포인트 클라우드 변환
- 부피 계산
- 좌표 변환 유틸리티

## 설정

`cfg.py` 파일에서 다음 설정을 변경할 수 있습니다:
- 카메라 해상도 및 FPS
- YOLO 모델 경로
- 기타 시스템 설정
