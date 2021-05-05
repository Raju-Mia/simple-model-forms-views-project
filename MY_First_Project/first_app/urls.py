from django.conf import settings
from django.urls import path
from . import views

# app_name ="'first_app'"

urlpatterns = [
    path("index/", views.index , name="index"),
    path("album/",views.album, name ="album"),
    path("form/", views.form, name="form"),
    path("addform/", views.add_form, name="add_form"),
]
