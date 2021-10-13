from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, Hi! vurrente server time is {now}'.format(now=str(now)))

def hi(request):
    numbers = [int(x) for x in request.GET['numbers'].split(',')]
    numbers.sort()
    response = {'nums':numbers}
    return JsonResponse(response)