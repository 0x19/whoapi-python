whoapi-python
=============

This library interacts with the [WhoAPI](http://www.whoapi.com) service. It allows you to use the REST API in a pythonic way to initiate and 
run all nice features that WhoAPI offer!


Installation
------------

Download the latest source from https://github.com/0x19/whoapi-python/tarball/master or checkout the code, 
then `cd` into the resulting directory and run `python setup.py install`.

*OR*

You can just open your terminal and hit `pip install whoapi`


Quick Start
-----------

WhoAPI Key can be found at [Account Details](http://whoapi.com/myaccount.html)

```python
from whoapi import WhoAPI

# First step is to initialize the object
whoapi = WhoAPI( whoapi_key = '{apikey}' )

# Now what we need to do is to query the service :)
query_response = whoapi.query( domain='{domain}', request_type='whois' )

print query_response # Will contain JSON object
```


