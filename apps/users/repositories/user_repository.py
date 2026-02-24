from core.repositories.base_repository import BaseRepository
from apps.users.models.user import User

class UserRepository(BaseRepository):

    def __init__(self):
        super().__init__(User)

    def get_by_email(self, email):
        return self.model.objects.filter(email=email).first()