from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('index/', views.index, name = "index"),
    path('add/', views.add_view, name = "add"),
    path('add/addList/', views.addList, name = "addList"),
    path('deleteList/<str:pk>', views.deleteList, name = "deleteList"),
]
