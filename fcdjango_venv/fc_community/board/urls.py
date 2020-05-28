from django.contrib import admin
from django.urls import path, include
from . import views

# admin안에 여러 url이 정의되어 있다. 
# aaaa.com/admin/~~~/~~~ <= 장고의 admin을 관리.

urlpatterns = [
    path('list/', views.board_list)
]
