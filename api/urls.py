from django.urls import include, path
from rest_framework import routers
from api import controllers

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('dogs/<int:pk>/', controllers.DogDetail.as_view()),
    path('dogs', controllers.DogList.as_view()),
    # path('breeds/<int:pk>/', controllers.BreedDetail.as_view()),
    # path('breeds', controllers.BreedList.as_view()),
    path('', include(router.urls)),
]
