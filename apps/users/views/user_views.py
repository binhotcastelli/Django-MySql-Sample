from django.http import JsonResponse
from apps.users.services.user_service import UserService

def list_users(request):
    users = UserService.list_users()
    data = [{"id": str(u.id), "name": u.name, "email": u.email} for u in users]
    return JsonResponse(data, safe=False)