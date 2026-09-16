from apps.users.repositories.user_repository import UserRepository
from core.exceptions import BusinessException


class UserService:

    @staticmethod
    def create_user(name: str, email: str):
        if UserRepository.get_by_email(email):
            raise BusinessException("Email já cadastrado.")

        return UserRepository.create(name=name, email=email)

    @staticmethod
    def list_users():
        return UserRepository.get_all()

    @staticmethod
    def get_user(user_id):
        user = UserRepository.get_by_id(user_id)

        if not user:
            raise BusinessException("Usuário não encontrado.")

        return user

    @staticmethod
    def update_user(user_id, name: str = None, email: str = None):
        user = UserRepository.get_by_id(user_id)

        if not user:
            raise BusinessException("Usuário não encontrado.")

        if email and email != user.email and UserRepository.get_by_email(email):
            raise BusinessException("Email já cadastrado.")

        fields = {}
        if name is not None:
            fields['name'] = name
        if email is not None:
            fields['email'] = email

        return UserRepository.update(user, **fields)

    @staticmethod
    def deactivate_user(user_id):
        user = UserRepository.get_by_id(user_id)

        if not user:
            raise BusinessException("Usuário não encontrado.")

        UserRepository.delete(user)