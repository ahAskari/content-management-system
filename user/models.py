from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    avatar = models.ForeignKey(
        'media.Photo', blank=True, null=True, on_delete=models.CASCADE, related_name='user')
    role = models.ForeignKey(
        'role.Role', on_delete=models.CASCADE, related_name='user', null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f'{self.pk} - {self.username} - ({self.role})'


# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user: User):
#         token = super().get_token(user)
#         token['username'] = user.username
#         token['email'] = user.email

#         return token
