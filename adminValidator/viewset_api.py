from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from DATABASE.models import BlogMainDatabase
from DATABASE.serializers import BlogSerializers

# Create your views here.
@api_view(['GET', 'POST'])
def adminValidatorViewSet(request):
    if (request.method == 'GET'):

        # QUEUE LOGIC
        # QUEUE LOGIC
        # QUEUE LOGIC
        # QUEUE LOGIC
        # QUEUE LOGIC
        pass
    if (request.method == 'POST'):

        # Accept or Denied Content Logic
        # Accept or Denied Content Logic
        # Accept or Denied Content Logic
        # Accept or Denied Content Logic
        # Accept or Denied Content Logic
        pass
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

@api_view(['POST'])
def login(request):
    return HttpResponse('LOGIN GAN', request)