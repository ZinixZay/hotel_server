from django.urls import path
from .viewsets import Test1ViewSet, Test2ViewSet

urlpatterns = [
    path('test/hotel1', Test1ViewSet.as_view()),
    path('test/hotel2', Test2ViewSet.as_view())
]
