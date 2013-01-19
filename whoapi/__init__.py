import os, logging, requests, re, json

from whoapi import exceptions, constants

class WhoAPI(object):

    def __init__(self, whoapi_key=None):
        self.whoapi_key   = whoapi_key
        self.domain       = None
        self.domain_regex = None
        self.request_type = None

        if len(self.whoapi_key) < 32:
            raise exceptions.KeyError('In order to query against WhoAPI you will need to provide valid WhoAPI key.')

    def query(self, domain, request_type, rr=None, ip=None, port=None, fullurl=None):
        self.domain       = domain
        self.request_type = request_type

        is_domain_valid   = self.is_valid_domain()

        logging.debug("[WhoAPI.query] Is domain valid? (%s)" % is_domain_valid)

        if not is_domain_valid:
            raise exceptions.DomainError('In order to query against WhoAPI you will need to provide valid WhoAPI key.')

        is_request_valid = self.is_valid_request()

        logging.debug('[WhoAPI.query] Is request type valid? (%s)' % is_request_valid)

        if not is_request_valid:
            raise exceptions.RequestTypeError('Invalid request type provided')

        
        whoapi_params = { 'domain' : self.domain, 'r' : self.request_type, 'apikey' : self.whoapi_key }

        if rr is not None:      
            whoapi_params['rr'] = rr

        if ip is not None:      
            whoapi_params['ip'] = ip

        if port is not None:    
            whoapi_params['port'] = port

        if fullurl is not None: 
            whoapi_params['fullurl'] = fullurl

        self.request = requests.get(constants.WHOAPI_BASE_URL, params=whoapi_params)

        logging.debug("[WhoAPI.query] Request URL : %s" % self.request.url)
        logging.debug("[WhoAPI.query] Response Status Code : %s" % self.request.status_code)
        logging.debug("[WhoAPI.query] Response Content : %s" % self.request.content)

        json_response = json.loads(self.request.content)

        try:
            status_code = json_response['status']

            if str(status_code) not in ( '0' ):
                raise exceptions.ResponseError(json_response['status_desc'], error_code=status_code)

        except (KeyError, AttributeError) as e:
            raise Exception("WhoAPI is probably down or under some heavy bug. Please contact WhoAPI support.")

        return json_response


    def is_valid_domain(self):

        logging.debug("[WhoAPI.is_valid_domain] Looking if %s is valid or not ..." % self.domain)

        if self.domain_regex is None:
            self.domain_regex = re.compile(r'^(?=.{4,255}$)([a-zA-Z0-9][a-zA-Z0-9-]{,61}[a-zA-Z0-9]\.)+[a-zA-Z0-9]{2,5}$')

        match = re.match(self.domain_regex, self.domain)

        if match: return True
        return False

    def is_valid_request(self):
        logging.debug("[WhoAPI.is_valid_request] Looking if %s is valid request or not ..." % self.request_type)
        return self.request_type in constants.WHOAPI_REQUEST_TYPES
