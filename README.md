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

makemigrations
: 앱 내의 migration 폴더를 만들어서 models.py의 변경사항을 저장

migrate : migration 폴더를 실행시켜 데이터베이스에 적용

→ model에 변경사항이 있을 경우 <b>makemigrations > migrate </b>

#### 슈퍼 유저 생성
python manage.py createsuperuser

### CRUD

#### GET vs POST

get은 데이터를 얻기 위한 요청 <br>
데이터가 url에 보임 ..
<br>

post는 데이터를 생성하기 위한 요청 <br>
데이터가 url에 보이지 않고 csrf 공격을 방지함

→ 데이터 생성 기능으로 가능한 무조건 post를 써야함
```python
    <form action="" method="POST">
        {% csrf_token %} 
        # 서버에서 인지해 공격을 방지할 수 있음
    </form>
```
#### Update

수정할 데이터의 id 값을 받아야함

수정해야 할 데이터를 데이터베이스에 불러서 다시 덮어씌워야 한다고 생각하면 됨

---

### Templete 상속
```python
{% extends 'base.html' %}
{% block content %}
{% endblock %}
```
### urls.py 관리

project폴더에 있는 urls.py의 코드길이는 간결해지고 app별로 urls.py를 관리할 수 있어서 프로젝트 시 좋음

---

### 장고에서 다루는 파일

- <b> 정적 파일 </b>
  : 미리 서버에 저장되어 있는 파일, 서버에 저장된 그대로를 서비스해주는 파일

    * Static : 개발자가 서버를 개발할 때 미리 넣어놓은 정적파일 (img, js, css)


    * media : 사용자가 업로드 할 수 있는 파일

- <b>동적 파일</b>
  : 서버의 데이터들이 어느정도 가공된 다음 보여지는 파일


### Static
```python
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'blog', 'static')] # 현재 static파일들이 어디에 있는지 경로를 적어줌

    STATIC_ROOT = os.path.join(BASE_DIR, 'static') # static 파일을 어디에 모을것인지
```

### Media
```python
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # 이용자가 업로드 한 파일을 모으는 곳

    MEDIA_URL = '/media/' # media파일의 url를 설정함
```

project내의 urls.py

```python
rom django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
```
---

### Form

<b>forms.py</b> 를 통해 데이터베이스 모델이 변할 때마다 복잡하게 바꿀 필요가 없음 

유효성 검사를 편하게 사용 가능


### User 확장과 인증

authenticate > 로그인 요청된 정보가 데이터와 맞는지


login > 로그인 객체를 통해 클라이언트가 인증된 상태가 될 수 있도록 하는 함수


logout > 서버에게 인증을 풀어달라는 요청


### Paginator

블로그 객체를 잘라서 보내줌