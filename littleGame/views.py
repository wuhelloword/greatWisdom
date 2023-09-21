from django.http import HttpResponse
from django.shortcuts import render

def ori(requests):
    # return render(requests, 'ori.html', {'name': 'helloword'})
    return render(requests, 'ori.html')