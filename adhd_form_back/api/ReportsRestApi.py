from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..ontology.Ontology import *


@api_view(['GET'])
def get_patients(request):
    response = fetch_patient_list()
    return Response(response, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_report(request):
    response = create_report(request.data)
    return Response(response, status=status.HTTP_200_OK)
