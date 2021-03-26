from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from msg.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'csv', MessageViewSet)

app_name='msg'
urlpatterns = [
    path('message/create/', MessageCreateView.as_view()),
    path('all/', MessageListView.as_view()),
    url(r'^', include(router.urls)),
    path('message/detail/<int:pk>/', MessageDetailView.as_view()),
]