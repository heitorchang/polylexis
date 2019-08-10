from django.urls import path
from . import views

app_name = "dicionario"

urlpatterns = [
    path('', views.gregoport, name="gregoport"),
]
