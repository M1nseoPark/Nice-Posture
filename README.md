<h2>참고한 코드 및 영상</h2>

1)https://www.youtube.com/watch?v=xz9MvyKGYio&t=156s
웹사이트에 실시간 영상 띄우기 (django/open cv)-> 터미널이 실행이 안됨/html 코드 알 수 없음


2)https://www.youtube.com/watch?v=Az1MH_e1hVA
https://github.com/ageitgey/face_recognition
https://github.com/ageitgey/face_recognition/issues/175
실시간 얼굴인식이 가능한 face_recognition 라이브러리를 이용함
가장 짧고 쉬운 방법이나, dlib 라이브러리를 설치해야 하는데 window 시스템에서는 설치가 잘 안된다고 했고, 
6시간 넘게 도전(conda에서도 해보았고, cmake설치 및 wheel 라이브러리 설치(설치 방법도 다양하게), dlib와 cmake는 사이트애 
가서 다운로드 또한 시도/구글링 및 유튜브 참고 등 가능한 방법은 모두 도전)헤보았지만 dlib 설치 오류를 해결하지 못함)


3)https://www.youtube.com/watch?v=yqkISICHH-U&t=15515s
시작할 때 사용자가 사용자의 얼굴을 직접 라벨링 가능하며, 얼굴 및 사물인식하는 코드 있음
웹을 IBM과 node js에 연결함(웹 개발은 django와 aws 로 진행했기에 모델만 참고)

4)https://www.youtube.com/watch?v=hr7ghNicP8o&t=178s
open cv를 이용한 실시간 얼굴 인식은 가능하나 얼굴을 인식하는 사각형의 정확도가 낮으며 웹에 연결 못함

5)https://www.youtube.com/watch?v=xz9MvyKGYio
django를 이용한 웹에 실시간 영상 띄우기 
 => open cv 를 이용한 얼굴인식 기술을 합치지 못함
 
 6)https://www.youtube.com/watch?v=zzJfAw3ASzY&t=303s
 https://www.geeksforgeeks.org/realtime-distance-estimation-using-opencv-python/
 open cv와 자체적인 얼굴 인식 모델을 이용하여 웹카메라와 인식하는 대상, 얼굴과의 거리를 측정하는 코드 
 저희 팀이 생성한 모델은 while 루프 안에서 작동하나, 위 코드에서의 모델은 while 루프 밖에서 작동하여 결합하는 데 어려움이 있음
 
 7)https://github.com/krishnaik06/Flask-Web-Framework/commit/b8b21efa948bf29e04f727ffbcf908945ad582ed#
 얼굴 인식 및 웹에 실시간 영상을 띄울 수 있으나 우분투에서 실행 가능
 
 8)https://blog.naver.com/ljy9378/221442172937
 컴퓨터에 내장된 카메라가 아닌 라즈베리 파이에서 실행. 헤어스타일을 바꾸었을 때 인식이 잘 되지 않는다는 사실 인식
 ->사용자가 로그인 할 때마다 사용자의 이미지 데이터를 수집하고 라벨링 하는 작업을 거쳐야 한다는 점 파악
 
 

 
 
