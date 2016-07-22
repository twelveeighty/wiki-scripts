#! /usr/bin/env python3

from ws.client.api import API

class fixtures:
    api = None

def setup_package():
    # NOTE: anonymous, will be very slow for big data!
    api_url = "https://wiki.archlinux.org/api.php"
    index_url = "https://wiki.archlinux.org/index.php"
    ssl_verify = True
    session = API.make_session(ssl_verify=ssl_verify)
    fixtures.api = API(api_url, index_url, session)

def teardown_package():
    fixtures.api = None
