from django.http import HttpResponse


def index(request):
    return HttpResponse("Post a lost or found pet")