from django.http import HttpResponse

def index(request):
    if request.method == 'GET':
        return HttpResponse("Hello, world. You're at the polls index.")
    elif request.method == 'POST':
        return HttpResponse("Hello, world. You're at the polls index.")
