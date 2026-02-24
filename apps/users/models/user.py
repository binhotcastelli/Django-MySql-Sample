from django.db import models
from core.models.base_model import BaseModel

class User(BaseModel):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name