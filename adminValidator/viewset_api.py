from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from DATABASE.models import BlogMainDatabase
from DATABASE.serializers import BlogSerializers

# Create your views here.
@api_view(['GET', 'POST'])
def adminValidatorViewSet(request):
    if (request.method == 'GET'):
        if ('token' in request.GET):
            token = request.GET['token']
            if (token == 'Ba72o5PX4vIH'):
                pass
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # QUEUE LOGIC
        # QUEUE LOGIC
        # QUEUE LOGIC
        # QUEUE LOGIC
        # QUEUE LOGIC
        pass
    if (request.method == 'POST'):
        if ('token' in request.POST):
            token = request.POST['token']
            if (token == 'Ba72o5PX4vIH'):
                pass
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # Accept or Denied Content Logic
        # Accept or Denied Content Logic
        # Accept or Denied Content Logic
        # Accept or Denied Content Logic
        # Accept or Denied Content Logic
        pass
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)