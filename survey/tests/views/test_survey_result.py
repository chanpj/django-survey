# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.urls.base import reverse
from future import standard_library

from survey.tests.management.test_management import TestManagement

standard_library.install_aliases()


class TestSurveyResult(TestManagement):

    def test_survey_result(self):
        """ We need logging for survey result if the survey need login. """
        url = reverse("survey-result", args=(2,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("survey-result", args=(1,)))
        self.assertEqual(response.status_code, 302)
        self.login()
        response = self.client.get(reverse("survey-result", args=(2,)))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("survey-result", args=(1,)))
        self.assertEqual(response.status_code, 200)
