# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from builtins import str

from future import standard_library

from survey.tests.models import BaseModelTest

standard_library.install_aliases()


class TestResponse(BaseModelTest):

    def test_unicode(self):
        """ Unicode generation. """
        self.assertIsNotNone(str(self.response))
