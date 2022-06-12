from django.http import HttpResponse


def index(request):  # HttpRequest
    return HttpResponse("Страница мебели")


def categories(request):
    return HttpResponse("<h1> Мебель по категориям</h1>")
