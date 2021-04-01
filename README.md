## Django

Django Study - Blog project

---

#### 가상환경 생성
python -m venv [가상환경 명]

#### 가상환경 실행
mac - source [가상환경 명]/bin/activate <br>
window - source [가상환경 명]/Scripts/activate

#### 장고 설치
pip install django

#### 장고 프로젝트 생성
django-admin startproject [프로젝트 명]

#### 서버 실행 (프로젝트로 들어온 뒤)
python manage.py runserver

---

#### MTV 패턴

Model (Back End) - DateBase <br>
Template (Front End) - 사용자가 보이는 영역 html, css등 <br>
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

### DateBase

makemigrations : 앱 내의 migration 폴더를 만들어서 models.py의 변경사항 저장

migrate : migration 폴더를 실행시켜 데이터베이스에 적용

→ model에 변경사항이 있을 경우 makemigrations > migrate

### CRUD

#### GET vs POST

get은 데이터를 얻기 위한 요청
데이터가 url에 보임 ..
<br>

post는 데이터를 생성하기 위한 요청
데이터가 url에 보이지 않고 csrf 공격을 방지함

#### Update

수정할 데이터의 id 값을 받아야함

수정해야 할 데이터를 데이터베이스에 불러서 다시 덮어씌워야 한다고 생각하면 됨

---

#### Templete 상속






