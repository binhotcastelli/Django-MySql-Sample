from django.urls import path
from apps.users.views.user_views import (
    list_users,
    create_user,
    get_user,
    update_user,
    deactivate_user,
)

urlpatterns = [
    path('', list_users, name='list_users'),
    path('create/', create_user, name='create_user'),
    path('<uuid:user_id>/', get_user, name='get_user'),
    path('<uuid:user_id>/update/', update_user, name='update_user'),
    path('<uuid:user_id>/deactivate/', deactivate_user, name='deactivate_user'),
]