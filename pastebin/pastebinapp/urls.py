from django.urls import path
from . import views
urlpatterns = [
    path("pastebin", views.create_pastebin),
]

