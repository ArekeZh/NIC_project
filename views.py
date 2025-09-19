from django.http import HttpResponse, JsonResponse
from django.template import loader

def main_menu(request):
    return HttpResponse("Just a main page, enter '/ping' or '/sum?a=1&b=2' to get sm response")

def ping(request):
    return JsonResponse({"message": "pong"})

def sum(request):
    a = int(request.GET.get('a', 2))
    b = int(request.GET.get('b', 3))
    

    return JsonResponse({"result": a + b})
