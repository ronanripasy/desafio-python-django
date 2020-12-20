from rest_framework.exceptions import APIException


class PythonDjangoException(APIException):
    default_code = 'pd_exception'

    def __init__(self, message, status=500):
        super(PythonDjangoException, self).__init__(message)
        self.status_code = status
