from django.contrib import admin
from django.urls import path, include
from . import views

# admin안에 여러 url이 정의되어 있다. 
# aaaa.com/admin/~~~/~~~ <= 장고의 admin을 관리.

urlpatterns = [
    path('detail/<int:pk>/', views.board_detail),
    path('list/', views.board_list),
    path('write/', views.board_write)
]
