from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    # role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'username', 'email', 'avatar', 'role']

    # def get_role(self, obj):
    #     return obj.role.name if obj.role else None


# class UserRoleSerializer(serializers.ModelSerializer):
#     role = serializers.SerializerMethodField()

#     class Meta:
#         model = User
#         fields = ['id', 'first_name', 'last_name',
#                   'username', 'email', 'avatar', 'role']

#     def get_role(self, obj):
#         return obj.role.name if obj.role else None
