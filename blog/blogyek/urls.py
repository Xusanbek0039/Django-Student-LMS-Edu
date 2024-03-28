
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include('blog.pages.urls')),
    path('post/', include('blog.posts.urls')),
    path('hisob/', include('blog.users.urls')),

] 