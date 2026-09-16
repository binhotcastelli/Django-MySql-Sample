import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from apps.users.services.user_service import UserService
from core.exceptions import BusinessException


def serialize_user(user):
    return {
        "id": str(user.id),
        "name": user.name,
        "email": user.email,
    }


@require_http_methods(["GET"])
def list_users(request):
    users = UserService.list_users()
    return JsonResponse([serialize_user(u) for u in users], safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def create_user(request):
    try:
        data = json.loads(request.body)
        user = UserService.create_user(
            name=data['name'],
            email=data['email']
        )
        return JsonResponse(serialize_user(user), status=201)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido."}, status=400)
    except KeyError as e:
        return JsonResponse({"error": f"Campo obrigatório ausente: {e}"}, status=400)
    except BusinessException as e:
        return JsonResponse({"error": str(e)}, status=400)


@require_http_methods(["GET"])
def get_user(request, user_id):
    try:
        user = UserService.get_user(user_id)
        return JsonResponse(serialize_user(user))
    except BusinessException as e:
        return JsonResponse({"error": str(e)}, status=404)


@csrf_exempt
@require_http_methods(["PUT"])
def update_user(request, user_id):
    try:
        data = json.loads(request.body)
        user = UserService.update_user(
            user_id,
            name=data.get('name'),
            email=data.get('email')
        )
        return JsonResponse(serialize_user(user))
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido."}, status=400)
    except BusinessException as e:
        return JsonResponse({"error": str(e)}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def deactivate_user(request, user_id):
    try:
        UserService.deactivate_user(user_id)
        return JsonResponse({}, status=204)
    except BusinessException as e:
        return JsonResponse({"error": str(e)}, status=404)