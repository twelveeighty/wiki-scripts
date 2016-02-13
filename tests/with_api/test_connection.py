#! /usr/bin/env python3

from nose.tools import assert_equals, assert_false, assert_true, raises
from nose.plugins.attrib import attr

from . import fixtures

from ws.core.connection import APIWrongAction, APIError, APIExpandResultFailed

@attr(speed="slow")
class test_connection:
    """
    Tests :py:class:`ws.core.connection` methods on :py:obj:`fixtures.api` instance.

    TODO:
        - cookies
        - set_argparser, from_argparser
        - call_index
    """

    # check correct server
    def test_hostname(self):
        assert_equals(fixtures.api.get_hostname(), "wiki.archlinux.org")

    @raises(ValueError)
    def test_params_is_dict(self):
        fixtures.api.call_api(params=("foo", "bar"))

    @raises(APIWrongAction)
    def test_wrong_action(self):
        fixtures.api.call_api(params={"action": "wrong action"})

    @raises(APIExpandResultFailed)
    def test_empty_query_expand(self):
        fixtures.api.call_api(action="query")

    def test_empty_query(self):
        assert_equals(fixtures.api.call_api(action="query", expand_result=False), {"batchcomplete": ""})

    @raises(APIError)
    def test_post_action(self):
        fixtures.api.call_api(action="purge")

    def test_help(self):
        h = fixtures.api.call_api(action="help")
        assert_equals(h["mime"], "text/html")
        assert_true(isinstance(h["help"], str))
