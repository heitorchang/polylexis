from django.urls import path

from . import views

app_name = "quizzes"

urlpatterns = [
    path('', views.index, name="index"),
    path('<path:dirname>/<str:filename>.txt', views.fileread, name="fileread"),
    path('<path:dirname>', views.dirlist, name="dirlist"),
]
