''' A library that provides a Python interface to the ScreenConnect API '''

from __future__ import print_function

import sys
import time


try:
    # Python 3
    from urllib.parse import urlparse, urlunparse, urlencode
    from urllib.request import urlopen
    from urllib.request import __version__ as urllib_version
except ImportError:
    from urlparse import urlparse, urlunparse
    from urllib2 import urlopen
    from urllib import urlencode
    from urllib import __version__ as urllib_version


class ScreenConnect():
    ''' A python interface into the ScreenConnect API '''

    def __init__(self,
                 url,
                 auth = None):
        ''' Instantiate a new ScreenConnect object 
        
        url = publicly accessible url for your ScreenConnect web server 
        auth = (user, pwd)
        '''

        self.url = url
        self.user, self.pwd = auth

    def _set_authentication_cookie(self):
        ''' Captures and stored the authentication cookie for specified
        user '''

        # Need to add authentication to the request
        r = urllib.request.urlopen(self.url)
        self._auth_cookie = r.getheader('Set-Cookie')

    def _reset_auth_account(self, auth):
        ''' Resets the designated account for authorization '''

        if self.user == user and self.pwd == pwd:
            return None

        self.user, self.pwd = auth
        self._auth_cookie = None