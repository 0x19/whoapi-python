class KeyError(Exception):
    message = "In order to query against WhoAPI you will need to provide valid WhoAPI key."

    def __init__(self, error_code=None, http_code=None):
        Exception.__init__(self, self.message)
        self.message    = self.message
        self.error_code = error_code
        self.http_code  = http_code
        

class DomainError(Exception):
    message = "Invalid domain name provided"

    def __init__(self, error_code=None, http_code=None):
        Exception.__init__(self, self.message)
        self.message    = self.message
        self.error_code = error_code
        self.http_code  = http_code
        

class RequestTypeError(Exception):
    message = "Invalid request type provided"

    def __init__(self, error_code=None, http_code=None):
        Exception.__init__(self, self.message)
        self.message    = self.message
        self.error_code = error_code
        self.http_code  = http_code


class ResponseError(Exception):

    def __init__(self, message='', error_code=None, http_code=None):
        Exception.__init__(self, message)
        self.message    = message
        self.error_code = error_code
        self.http_code  = http_code