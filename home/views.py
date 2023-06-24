from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
@permission_classes((IsAdminUser, ))
def api_overview(request):
    context = {}
    urls = {
        'API Overview': '/',
    }
    context['urls'] = urls
    return Response(context, status.HTTP_200_OK)