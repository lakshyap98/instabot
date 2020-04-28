from django.conf import settings
import re
from django.shortcuts import render
from django.http import HttpResponse

EXEMPT_URL = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URL'):
    EXEMPT_URL += [re.compile(url.lstrip('/')) for url in settings.LOGIN_EXEMPT_URL]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        print("------------------------", response)
        return response
    
    def process_view(self, request, view_func, *args, **kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip("/")

        if not request.user.is_authenticated:
            if not any(url.match(path) for url in EXEMPT_URL):
                return HttpResponse("Please log in first")
    
    # def process_exception(self, request, exception):
    #     print("IN THe MIDDLEWARE EXCEPTION")
    
    # def process_template_response(self, request, response):
    #     print("IN THe MIDDLEWARE TEMPLATE RESPONSE")