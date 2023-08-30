from django.http import HttpResponse

def page_view(request):
    return HttpResponse("<h1>hello world</h1>")