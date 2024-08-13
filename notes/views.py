from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .ml_models.gemini_model import get_gemini_response

# Create your views here.
def notes(request):
  return render(request, 'notes.html')

@csrf_exempt
def get_response(request):
  if request.method == 'POST':
    try:
      data =json.loads(request.body)
      text = data.get('text', '')
      result = get_gemini_response(text)
      return JsonResponse({ 'result': result })
    
    except json.JSONDecodeError:
      return JsonResponse({'error': 'Invalid data detected'}, status=400)
    
  return JsonResponse({'error': 'A JSON request is needed'}, status=405)