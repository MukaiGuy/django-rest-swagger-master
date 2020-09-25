from django.conf import settings


def context_processors(request):

    return { 'APP_NAME': settings.APP_NAME }