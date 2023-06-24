from rest_framework import serializers

from users.models import Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        
    def to_representation(self, instance):
        self.fields['user'] = UserSerializer(read_only=True)
        return super(ProfileSerializer, self).to_representation(instance)
        
    