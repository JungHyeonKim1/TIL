from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('detail/', views.detail, name='detail'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/update/', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
