# my_camera_calibration

해당 프로젝트는 Opencv를 활용한 간단하게 Camera Calibration을 할 수 있는 Python 프로그램입니다.


## Camera Calibration 결과

체스보드 패턴을 이용해 OpenCV의 Calibration 기능을 사용하여 Camera Calibration을 수행습니다. 얻어진 내부 파라미터 및 왜곡 계수는 다음과 같습니다.
| 파라미터 | 값 |
| ------ | ------ |
| K | [[944.53574431 ,  0 ,  345.32015375] [0 ,      876.31371825 , 644.90248486] [0 , 0 , 1]] |
| Distortion Coefficients | [[ 9.49929521e-02 , 3.11662831e+00 , -3.88910029e-02  , -4.50227023e-03  , -4.06874417e+01]] |
| Reprojection Error | 1.2006559540450095 |
## Distortion Correction 데모

위에서 얻은 Calibration 데이터를 활용해 영상의 렌즈 왜곡을 보정하였습니다. 보정된 영상은 output.avi 파일로 저장되었습니다.
- 원본 영상 - chessboard.avi
- 보정된 영상 - output.avi
- 
보정된 영상에서는 방사 왜곡과 접선 왜곡이 줄어들어 곡선으로 보이던 직선이 올바르게 보입니다. output.avi를 실행 보정 결과를 확인할 수 있습니다.
