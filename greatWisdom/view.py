from django.http import HttpResponse
from django.shortcuts import render


def page_view(requests):
    return render(requests, 'index.html')