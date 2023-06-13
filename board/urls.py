from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/',views.List.as_view(), name='list'),
    path('regist/',views.Regist.as_view(),name='regist'),
    path('detail/<int:pk>/',views.Detail.as_view(), name='detail'),
    path('edit/<int:pk>/',views.Edit.as_view(), name='edit'),
    path('delete/<int:pk>/',views.Delete.as_view(), name='delete'),
]

