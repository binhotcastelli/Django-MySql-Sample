from apps.users.models.user import User

class UserRepository:

    @staticmethod
    def get_all():
        return User.objects.filter(is_active=True)

    @staticmethod
    def get_by_id(user_id):
        return User.objects.filter(id=user_id, is_active=True).first()

    @staticmethod
    def get_by_email(email):
        return User.objects.filter(email=email, is_active=True).first()

    @staticmethod
    def create(**data):
        return User.objects.create(**data)

    @staticmethod
    def update(user, **data):
        for field, value in data.items():
            setattr(user, field, value)
        user.save()
        return user

    @staticmethod
    def delete(user):
        user.is_active = False
        user.save()