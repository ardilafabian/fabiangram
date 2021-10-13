from django.http import HttpResponse

# Utilities
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, Hi! vurrente server time is {now}'.format(now=str(now)))