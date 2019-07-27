from django.urls import path

from . import views

app_name = "fileeditor"

urlpatterns = [
    path('', views.index, name="index"),
    path('<path:dirname>/create', views.filecreate, name="filecreate"),
    path('<path:dirname>/<str:filename>.txt/delete', views.filedelete, name="filedelete"),
    path('<path:dirname>/<str:filename>.txt', views.fileread, name="fileread"),
    path('<path:dirname>', views.dirlist, name="dirlist"),
]
