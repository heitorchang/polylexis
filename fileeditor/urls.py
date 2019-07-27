from django.urls import path

from . import views

app_name = "fileeditor"

urlpatterns = [
    path('<str:dirname>/', views.dirlist, name="dirlist")
]
