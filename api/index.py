import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from app import app
from werkzeug.wrappers import Request, Response

def handler(request):
    # For Vercel Python runtime, we get a Request object
    with app.request_context(request.environ):
        response = app.full_dispatch_request()
        return response