from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views import defaults as default_views
from bot import views
from blog.pages.views import *
from blog.posts.views import *

admin.site.site_header = "ITC LMS Platformasi"

urlpatterns = [
    # blog page urllar
    path('blog/', LatestPostListView.as_view(), name='blog'),
    path('about/', AboutView.as_view(), name='blogabout'),
    path('contact/', ContactView, name='blogcontact'),
    path('blogsearch/', search, name='blogsearch'),
    path('blog/', include('blog.pages.urls', namespace='blog')),
    # path('posts', PostList, name='posts'),
    path('create/', PostCreateView.as_view(), name='postCreate'),
    path('update/<slug:slug>/', PostUpdateView.as_view(), name='postUpdate'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='postDelete'),
    path('categories/<slug:category_slug>', PostList, name='posts_by_category'),
    path('tags/<slug:tag_slug>', PostList, name='posts_by_tag'),
    path('<slug:post_category_slug>/<int:id>/<slug:slug>/', PostDetailView.as_view(), name='postDetail'),
    path('blogsearch/', search, name='blogsearch'),
    path('comment/<int:pk>/', CommentView.as_view(), name='addComment'),
    path('posts/', include('blog.posts.urls', namespace='posts')),

    # AI bo'limi urllari
    path("chat/", views.chat_page, name="chat_page"),
    path('submit/', include('bot.urls', namespace='bot')),

    path('clear_chat_history/', views.clear_chat_history, name='clear_chat_history'),
    path('delete_message_from_db/<int:v_id>', views.delete_message_from_db, name="delete_message_from_db"),
    path('update_prompt/', views.update_prompt, name='update_prompt'),
    path('delete_prompt/', views.delete_prompt, name='delete_prompt'),
    
    # path("jet/", include("jet.urls", "jet")),  # Django JET URLS
    # path(
    #     "jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")
    # ),  # Django JET dashboard URLS

    # path("blog", include("blog.blogyek.urls")),
    path("", include("core.urls")),
    path("accounts/", include("accounts.urls")),
    path("programs/", include("course.urls")),
    path("result/", include("result.urls")),
    path("search/", include("search.urls")),
    path("quiz/", include("quiz.urls")),
    # path("payments/", include("payments.urls")),
    path("accounts/api/", include("accounts.api.urls", namespace="accounts-api")),
    path("admin/", admin.site.urls),
]
handler404 = 'core.views.handler404'
handler500 = 'core.views.handler500'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Saxifa topilmadi iltimos tizimni yangilang!")},
        ),
        path("500/", default_views.server_error),
    ]
