import secrets
from datetime import datetime
from django.db import models

class AccessTokenManager(models.Manager):

    def create_token(self, user):
        token = self.create(
            token = secrets.token_urlsafe(32),
            created_by = str(user),
        )

        return token


