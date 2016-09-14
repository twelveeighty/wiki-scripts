#! /usr/bin/env python3

from ws.utils import LazyProperty

class test_lazy:
    def setup(self):
        self._values = list(range(10))

    @LazyProperty
    def lazyprop(self):
        return self._values.pop(0)

    @property
    def normalprop(self):
        return self._values.pop(0)

    def test_lazyprop(self):
        assert self.lazyprop == 0
        assert self.lazyprop == 0
        del self.lazyprop
        assert self.lazyprop == 1
        assert self.lazyprop == 1

    def test_normalprop(self):
        assert self.normalprop == 0
        assert self.normalprop == 1
        assert self.normalprop == 2
        assert self.normalprop == 3
