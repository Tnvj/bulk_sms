# accounts/middleware.py

from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect

class SessionIdleTimeout:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)

        if 'last_activity' in request.session:
            idle_time = (request.timestamp - request.session['last_activity']).total_seconds()
            if idle_time > settings.SESSION_COOKIE_AGE:
                messages.add_message(request, messages.INFO, 'Your session has expired due to inactivity.')
                del request.session['last_activity']
                return redirect('logout')

        request.session['last_activity'] = request.timestamp
        return self.get_response(request)
