# A. base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div class="container">
    {% block content %}
    {% endblock content %}
  </div>
</body>
</html>
```



# B. index.html

![](C:\Users\multicampus\AppData\Roaming\marktext\images\2022-09-02-17-13-33-image.png)

```html
{% extends 'base.html' %}

{% block content %}
  <h1>INDEX</h1>
  <a href="{% url 'movies:new' %}">[NEW]</a>
  <hr>
  {% for movie in movies %}
    <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a>
    <p>{{ movie.score }}</p>
  {% endfor %}
{% endblock content %}
```

new에서 index로 보낼 때, movie.pk로 각각 받아줘야 리스트가 저장된다는 사실을 몰라서, 그 오류때문에 오래 고민했다.



# C. detail.html

![](C:\Users\multicampus\AppData\Roaming\marktext\images\2022-09-02-17-15-55-image.png)

```html
{% extends 'base.html' %}
{% block content %}
  <h2>DETAIL</h2>
  <hr>
  <img src="{{ movie.poster_url }}" alt=" ">
  <h3>{{ movie.title }}</h3>
  <p>audience : {{ movie.audience }}</p>
  <p>Release Dates : {{ movie.release_date }}</p>
  <p>Genre : {{ movie.genre }}</p>
  <p>Score : {{ movie.score }}</p>
  <P>{{ movie.description }}</p>
  <a href="{% url 'movies:edit' movie.pk %}">EDIT</a>
  <form action="{% url 'movies:delete' movie.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
  <a href="{% url 'movies:index' %}">[back]</a>
{% endblock content %}
```

csrf_token이 있어야 표를 수정, 삭제 할 수 있다는 사실을 알게 되었다. 개념으로는 이해가 잘 되지 않는 부분이 있었는데 실습을 하며 알게 되었다.



# D. new.html

![](C:\Users\multicampus\AppData\Roaming\marktext\images\2022-09-02-17-17-10-image.png)

```html
{% extends 'base.html' %}
{% block content %}
  <h1>NEW</h1>
  <hr>
  <form action="{% url 'movies:create' %}" method="POST">
    {% csrf_token %}
    <label for="title">TITLE</label>
    <input type="text" name="title"><br>
    <label for="audience">AUDIENCE</label>
    <input type="text" name="audience"><br>
    <label for="release_date">RELEASE_DATE</label>
    <input type="date" name="release_date"><br>
    <label for="genre">GENRE</label>
    <select name="genre" id='genre'>
      <option value="comedy">코미디</option>
      <option value="sf">SF</option>
      <option value="tv_movie">TV 영화</option>
      <option value="family">가족</option>
      <option value="horror">공포</option>
      <option value="documentary">다큐멘터리</option>
      <option value="drama">드라마</option>
      <option value="romance">로맨스</option>
      <option value="adventure">모험</option>
      <option value="mystery">미스터리</option>
      <option value="crime">범죄</option>
      <option value="western">서부</option>
      <option value="thriller">스릴러</option>
      <option value="animation">애니메이션</option>
      <option value="action">액션</option>
      <option value="history">역사</option>
      <option value="music">음악</option>
      <option value="war">전쟁</option>
      <option value="fantasy">판타지</option>
    </select><br>
    <label for="score">SCORE</label>
    <input type="text" name="score"><br>
    <label for="poster_url">POSTER_URL</label>
    <input type="text" name="poster_url"><br>
    <label for="description">DESCRIPTION</label>
    <textarea name="description"></textarea><br>
    <input type="submit" value="Submit">
  </form>
  <hr>
  <a href="{% url 'movies:index' %}">BACK</a>
{% endblock content %}
```

select를 이용해 옵션 메뉴를 제공한다는 사실을 알게 되었다.



# E. edit.html

![](C:\Users\multicampus\AppData\Roaming\marktext\images\2022-09-02-17-18-16-image.png)

```html
{% extends 'base.html' %}
{% block content %}
  <h1>EDIT</h1>
  <form action="{% url 'movies:update' movie.pk %}" method="POST">
    {% csrf_token %}
    <label for="title">TITLE</label>
    <input type="text" name="title" value="{{ movie.title }}"><br>
    <label for="audience">AUDIENCE</label>
    <input type="text" name="audience" value="{{ movie.audience }}"><br>
    <label for="release_date">RELEASE_DATE</label>
    <input type="date" name="release_date" value="{{ date }}"><br>
    <label for="genre">GENRE</label>
    <select name="genre" id='genre'>
      <option value="">{{ movie.genre }}</option>
      <option value="코미디">코미디</option>
      <option value="SF">SF</option>
      <option value="TV 영화">TV 영화</option>
      <option value="가족">가족</option>
      <option value="공포">공포</option>
      <option value="다큐멘터리">다큐멘터리</option>
      <option value="드라마">드라마</option>
      <option value="로맨스">로맨스</option>
      <option value="모험">모험</option>
      <option value="미스터리">미스터리</option>
      <option value="범죄">범죄</option>
      <option value="서부">서부</option>
      <option value="스릴러">스릴러</option>
      <option value="애니메이션">애니메이션</option>
      <option value="액션">액션</option>
      <option value="역사">역사</option>
      <option value="음악">음악</option>
      <option value="전쟁">전쟁</option>
      <option value="판타지">판타지</option>
    </select><br>
    <label for="score">SCORE</label>
    <input type="text" name="score" value="{{ movie.score }}"><br>
    <label for="poster_url">POSTER_URL</label>
    <input type="text" name="poster_url" value="{{ movie.poster_url }}"><br>
    <label for="description">DESCRIPTION</label>
    <textarea name="description">{{ movie.description }}</textarea><br>
    <input type="reset" value="Reset">
    <input type="submit" value="Submit">
  </form>
  <hr>
  <a href="{% url 'movies:index' %}">BACK</a>
  </form>
{% endblock content %}
```

다른건 비교적 어렵지 않게 원래의 요소를 반환 시킬 수 있었지만, release_date와 genre가 문제였다.  release_date는 views.py에서 edit(request) 함수를 선언할 때, date = movie.release_date.strftime('%Y-%m-%d') 와 같은 형식으로 context안에 넣는 것으로 해결했다. genre의 경우에는, 처음에는 value를 영어로 받아서 어떻게 할지 고민을 했는데, 그냥 value도 모두 한글로 받고 가장 처음에 나오는 것을 {{ movie.genre }} 로 표시하게 했다. 중복된다는 점이 있었지만, genre가 많은 경우에 가장 효율적인 방법이라고 생각해 이 방법을 택했다.
