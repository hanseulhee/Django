## Django

Django Study

---

#### 가상환경 생성
python -m venv[가상환경 명]

#### 가상환경 실행
mac - source[가상환경 명]/bin/activate <br>
window - source[가상환경 명]/Scripts/activate

#### 장고 설치
pip install django

#### 장고 프로젝트 생성
django-admin startproject [프로젝트 명]

#### 서버 실행 (프로젝트로 들어온 뒤)
python manage.py runserver

---

### MTV 패턴

Model (Back End) - DateBase
Template (Front End) - 사용자가 보이는 영역 html, css등
View (Back End) - 데이터를 처리하는 곳

### App 제작

#### App 생성
python manage.py startapp [앱 이름]

프로젝트폴더 > setting.py > INSTALLED_APPS에 앱의 이름.apps.apps.py의 class명 추가

#### Template 제작
앱폴더 > 템플릿 폴더생성 > html 생성

#### View 제작, URL연결
만든 view와 url 연결

---

