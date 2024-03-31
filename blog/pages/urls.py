from django.urls import path
from blog.pages import views

app_name = 'blog.pages'

urlpatterns = [
    path('', views.LatestPostListView.as_view(), name='blog'),
    path('blogabout/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView, name='contact'),
]
