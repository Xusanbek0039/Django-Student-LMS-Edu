
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("chat", include("bot.urls")),
]
