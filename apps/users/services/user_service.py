from core.services.base_service import BaseService
from apps.users.repositories.user_repository import UserRepository

class UserService(BaseService):

    def __init__(self):
        super().__init__(UserRepository())

    def create_user(self, name, email):
        if self.repository.get_by_email(email):
            raise ValueError("Email já cadastrado")

        return self.repository.create(
            name=name,
            email=email
        )