from rest_framework.views import exception_handler

from core.exceptions import PythonDjangoException


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if isinstance(exc, PythonDjangoException):
        response.data['error'] = str(exc)
    response.data['status_code'] = response.status_code
    return response
