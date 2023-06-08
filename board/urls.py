from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/',views.list, name='list'),
    path('regist/',views.regist,name='regist'),
    path('detail/<int:id>/',views.detail, name='detail'),
    path('edit/<int:id>/',views.edit, name='edit'),
    path('delete/<int:id>/',views.delete, name='delete'),
]

