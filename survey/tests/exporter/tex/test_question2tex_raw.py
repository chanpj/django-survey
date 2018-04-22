# -*- coding: utf-8 -*-


from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from future import standard_library

from survey.exporter.tex.question2tex_raw import Question2TexRaw
from survey.tests.management.test_management import TestManagement

standard_library.install_aliases()


class TestQuestion2TexRaw(TestManagement):

    def test_raw_tex(self):
        """ We can create a raw chart. """
        question = self.survey.questions.get(text="Aèbc?")
        expected = ["1é", "1", "1a", "1b", "1e", "1ë"]
        container = Question2TexRaw(question).tex()
        for i in expected:
            self.assertIn(i, container)
