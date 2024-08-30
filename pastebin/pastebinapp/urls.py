from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

route = SimpleRouter()

route.register('api', views.PastebinViewset)

urlpatterns = [
]

urlpatterns += route.urls

