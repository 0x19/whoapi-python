''' Simple demonstration how to get whois of some domain with WhoAPI '''

from whoapi import WhoAPI

# First step is to initialize the object
whoapi = WhoAPI( whoapi_key = '{demokey}' )

# Now what we need to do is to query the service :)

# All parameters that are supported by query method
# whoapi.query( domain='{domain}', request_type='{request_type}', rr='{rr}', ip='{ip}', port='{port}', fullurl='{fullurl}' )

query_response = whoapi.query( domain='{domain}', request_type='whois' )

print query_response # Will contain JSON object
