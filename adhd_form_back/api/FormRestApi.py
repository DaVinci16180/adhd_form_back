from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..ontology.Ontology import *


@api_view(['POST'])
def post_form(request):
    response = register_form(request.data)
    return Response(response, status=status.HTTP_200_OK)
