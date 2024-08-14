from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .ml_models.gemini_chat import send_message

# Create your views here.
def notes(request):
  return render(request, 'notes.html')

@csrf_exempt
def get_response(request):
  if request.method == 'POST':
    try:
      data =json.loads(request.body)
      text = data.get('text', '')
      print(f"The user text is: {text}") 
      result = send_message(text)
      print(f"The respond is: {result}")
      return JsonResponse({ 'result': result })
    
    except json.JSONDecodeError:
      return JsonResponse({'error': 'Invalid data detected'}, status=400)
    
  return JsonResponse({'error': 'A JSON request is needed'}, status=405)