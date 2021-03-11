from django.urls import path, re_path
from . import views


urlpatterns = [
    path('users/', views.post_user, name='post_user'),
    path('users/<username>/<userpassword>', views.user,
         name='get_put_delete_single_user'),
    path('userdetails/', views.post_user_detail, name='post_user_detail'),
    path('userdetails/<userid>/<datatype>/',
         views.get_user_detail_datatype, name='get_user_detail_datatype'),
    path('userdetails/<userid>/', views.put_user_detail, name='put_user_detail'),
    path('userdetails_basic/<userid>/',
         views.get_user_detail_basic, name='get_user_detail_basic'),
    path('fanclubs/', views.fanclub_list,
         name='get_all_fanclub_basic_post_fanclub'),
    path('fanclubs/<clubid>/', views.fanclub,
         name='get_put_delete_single_fanclub'),
    path('fanclubs_basic/created_by/<creator>', views.fanclub_basic_creator,
         name='get_single_fanclub_basic_creator'),
    path('fanclubs_basic/<clubid>/', views.fanclub_basic,
         name='get_single_fanclub_basic'),
    path('chats/<chatroomid>/', views.fanclub_chat_list,
         name='get_fanclub_chat_list')
]
