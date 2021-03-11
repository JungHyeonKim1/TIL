from django.urls import path
# 명시적 상대경로 표현
from . import views     # 표현 방식이 특이하죠?


urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello'),
    # path('hello/<name>/', views.hello),   str이 기본값이기 때문이다.
]