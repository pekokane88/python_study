# 간단한 슬라이드 1장 PPT 제작 자동화 파이썬 스크립트

### 개요
<ul>
  - 한 장짜리 슬라이드 ppt 를 간단하게 만들기 위한 파이썬 스크립트
  - 제목, 내용, 이미지 선택 or 이미지 캡처를 하면 그 내용을 가지고 파워포인트를 만들어 준다.
  - output으로는 현재 time을 이름으로 가진 파워포인트가 생성된다.
</ul>

### 사용 스택
<ul>
  - Pyside6 : GUI를 제작하기 위해.
  - Qt-Designer : GUI를 제작하기 위한 GUI를 사용하기 위해.
  - mainWindow(상속) : Qt-Designer 에서 만든 ui를 상속받아서 그대로 사용.
  - python-pptx : ppt를 생성하기 위해 사용.
  - date : 중복을 방지하기 위해 시간 정보를 이용.
  - PIL : 이미지를 처리하기 위해.
  - pyautogui : 스크린 캡처를 하기 위한 매크로 도구.
</ul>

### 추후 사항
<ul>
  - pyinstaller 를 이용한 실행파일화
  - 다중 슬라이드 생성 및 편집
  - 현재 base.pptx 라는 기본 틀을 불러와서 지정해둔 shape 에 title, image, text를 추가하는 방식에서 스크립트로 전부 생성할 수 있도록 수정.
</ul>

### 변경 사항
<ul>
  - 화면 크기 조정
  - 화면 위치 조정
  - qrc 를 이용한 application logo 이미지 추가
  - pyinstaller 에 --logo 옵션을 이용한 아이콘 이미지 추가 기능 확인
</ul>

###### 수정 날짜 22.08.22 17:34
  
