import azure.functions as func
from myblog.wsgi import application

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.WsgiMiddleware(application).handle(req, context)
