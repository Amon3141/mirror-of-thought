from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
  return render(request, 'notes.html')

def sub(request, n):
  message = "This is the sub page %d"
  return HttpResponse(message % n)