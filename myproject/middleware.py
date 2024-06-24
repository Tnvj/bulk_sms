# bulk_sms/middleware.py

from datetime import datetime

class TimestampMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.timestamp = datetime.now()
        response = self.get_response(request)
        return response
