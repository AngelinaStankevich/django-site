from django.http import HttpResponse


def index(request):  # HttpRequest
    return HttpResponse("Страница furniture.")
