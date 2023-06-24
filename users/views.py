from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token

from users.serializers import *

# Create your views here.


@api_view(['POST'])
@permission_classes((IsAdminUser, ))
def signup(request):
    context = {}
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        user = user_serializer.save()
        user.set_password(request.data['password'])
        user.save()

        context['user'] = user_serializer.data
        profile_serializer = ProfileSerializer(
            data={'user': user_serializer.data['id']})
        if profile_serializer.is_valid():
            profile_serializer.save()
            context['message'] = 'User created successfully'
            
            username = request.data['username']
            password = request.data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                context['token'] = token.key
            return Response(context, status.HTTP_201_CREATED)
    else:
        return Response(user_serializer.errors, status.HTTP_400_BAD_REQUEST)
