# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from future import standard_library

from survey.models.category import Category
from survey.tests import BaseTest

standard_library.install_aliases()


class TestCategory(BaseTest):

    def test_unicode(self):
        """ Unicode is not None and do not raise error. """
        cat = Category.objects.all()[0]
        self.assertIsNotNone(cat)

    def test_slugify(self):
        """ Slugify is not None and do not raise error. """
        cat = Category.objects.all()[0]
        self.assertIsNotNone(cat.slugify())
