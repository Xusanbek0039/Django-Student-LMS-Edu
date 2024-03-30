from django.urls import path
from . import views


app_name = "bot"
urlpatterns = [
    path('chat/', views.chat_page, name="chat_page"),
    path('submit/', views.submit_form, name='submit_form'),
    path('clear_chat_history/', views.clear_chat_history, name='clear_chat_history'),
    path('delete_message_from_db/<int:v_id>', views.delete_message_from_db, name="delete_message_from_db"),
    path('update_prompt/', views.update_prompt, name='update_prompt'),
    path('delete_prompt/', views.delete_prompt, name='delete_prompt'),
    


    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('online_people/', views.online_people, name='online_people'),
]