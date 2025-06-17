from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('forum/<int:id>/', forum_detail, name='forum_detail'),
    path('forum/', forum_list, name='forum_list'), 
    path('flag-access/', flag_view, name='flag_view'),
    path('logout/', logout_view, name='logout'), 
]
