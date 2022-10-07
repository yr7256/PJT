# A. base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
  <title>Document</title>
</head>
<body>
  <div class="container">
    {% load bootstrap5 %}
    {% block content %}
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
</body>
</html>
```

# B. index.html

```html
{% extends 'base.html' %}
{% block content %}
  <h1>INDEX</h1>
  <a href="{% url 'movies:create' %}">CREATE</a>
  <hr>
  {% for movie in movies %}
    <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a>
    <p>{{ movie.score }}</p>
    <hr>
  {% endfor %}
{% endblock content %}
```

```python
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)
```

![](C:\Users\multicampus\AppData\Roaming\marktext\images\2022-10-07-15-49-20-image.png)

# C. detail.html

```html

{% extends 'base.html' %}
{% block content %}
<h1 class='text-center'>DETAIL</h1>
<hr>
<div class="card mx-auto" style="width: 25rem;">
  <img src="{{ movie.poster_url }}" alt=" ">
    <h3>{{ movie.title }}</h3>
    <p>audience : {{ movie.audience }}</p>
    <p>Release Dates : {{ movie.release_date }}</p>
    <p>Genre : {{ movie.genre }}</p>
    <p>Score : {{ movie.score }}</p>
    <P>{{ movie.description }}</p>
    <div class="d-flex justify-content-start">
    <a class="btn btn-info mx-2" href="{% url 'movies:update' movie.pk %}" role="button">UPDATE</a>
    <form action="{% url 'movies:delete' movie.pk %}" method="POST">
      {% csrf_token %}
      <button class="btn btn-danger" type="submit">DELETE</button>
    </form>
    </div>
</div>
<a class="btn btn-warning" href="{% url 'movies:index' %}" role="button">BACK</a>
{% endblock content %}

```

```python
@require_safe
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)
```

![](C:\Users\multicampus\AppData\Roaming\marktext\images\2022-10-07-15-52-56-image.png)

배운 점 : d-flex, card, button 등 bootstrap 사용법에 대해서 복습하는 계기가 되었다.

어려웠던 점 : detail에는 bootstrap_form 형식이 적용되지 않아 직접 구현하는 것이 까다로웠다. 

# D. create.html

```html
{% extends 'base.html' %}
{% block content %}
  <h1>CREATE</h1>
  <hr>
  <form action="{% url 'movies:create' %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <button class="btn btn-primary" type="submit">Submit</button>
  </form>
  <hr>
  <a class="btn btn-info" href="{% url 'movies:index' %}" role="button">BACK</a>
{% endblock content %}

```

```python
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)
```

![](C:\Users\multicampus\AppData\Roaming\marktext\images\2022-10-07-15-52-06-image.png)

배운 점 : bootstrap_form 형식으로 받으면 정해진 형식으로 페이지를 구성할 수 있다는 것을 알게 되었다.

어려웠던 점 : release date, genre, score를 widget으로 바꿔서 받는 것이 어려웠다.

# E. update.html

```html
{% extends 'base.html' %}
{% block content %}
  <h1>UPDATE</h1>
  <hr>
  <form action="{% url 'movies:update' movie.pk %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <button class="btn btn-primary" type="submit">Submit</button>
    <button class="btn btn-primary" type="reset">Cancel</button>
  </form>
  <hr>
  <a class="btn btn-info" href="{% url 'movies:detail' movie.pk %}" role="button">BACK</a>
{% endblock content %}
```

```python
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)
```

![](C:\Users\multicampus\AppData\Roaming\marktext\images\2022-10-07-15-52-28-image.png)

배운 점 : bootstrap을 사용해 버튼의 색 등 페이지를 기본 html보다 깔끔하게 구성할 수 있다는 것을 알게 되었다.

어려웠던 점 : cancel의 input type을 reset 으로 받는 것을 생각하지 못해 오래 걸렸다.


