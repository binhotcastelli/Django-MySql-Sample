from django.urls import path
from apps.users.views.user_views import list_users

urlpatterns = [
    path('', list_users, name='list_users'),
]