# myapp/middleware.py
from django.http import HttpResponseForbidden

class TokenAuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.headers.get('Authorization')
        if not self.is_valid_token(token):
            return HttpResponseForbidden("Invalid or missing token")
        response = self.get_response(request)
        return response

    def is_valid_token(self, token):
        return True  
