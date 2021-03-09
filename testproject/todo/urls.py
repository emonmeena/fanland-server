from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/<username>', views.user_details, name='user_details'),
    path('fanclubs/', views.fanclub_list, name='fanclub_list'),
    path('fanclubs/<club_id>', views.fanclub_details, name='fanclub_details'),
    path('chats/<chatroom_id>', views.chat_list, name='chat_list'),
    # path('userdata/<user_id>', views.user_data, name='user_data'),
]

