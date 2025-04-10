from django.urls import path
from .views import *

urlpatterns = [
    path('', user_list, name='user_list'),
    path('add/', add_user, name='add_user'),
    path('update/<int:user_id>/', update_user, name='update_user'),
    path('delete/<int:user_id>/', delete_user, name='delete_user'),
]
