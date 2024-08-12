from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ml_model import generate_response

# Create your views here.
@api_view(['POST'])
def get_response(request):
  prompt = request.data.get('prompt')
  if prompt:
    response = generate_response(prompt)
    return Response({"response": response})
  return Response({"error": "No prompt provided"}, status=400)
