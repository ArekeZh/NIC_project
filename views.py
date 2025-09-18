from django.http import HttpResponse, JsonResponse
from django.template import loader

def ping(request):
    return JsonResponse({"message": "pong"})

def sum(request):
    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))
    
    return JsonResponse({"result": a + b})