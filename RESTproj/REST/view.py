from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def someData(request):
    return Response({'name':'Pupa', 'occupation':'mem'})
