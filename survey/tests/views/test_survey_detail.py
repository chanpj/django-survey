# -*- coding: utf-8 -*-


from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.urls.base import reverse
from future import standard_library

from survey.tests import BaseTest

standard_library.install_aliases()


class TestSurveyDetail(BaseTest):

    def test_survey_result(self):
        """ We need logging for survey detail if the survey need login. """
        response = self.client.get(reverse("survey-detail", args=(2,)))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("survey-detail", args=(1,)))
        self.assertEqual(response.status_code, 302)
        self.login()
        response = self.client.get(reverse("survey-detail", args=(2,)))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("survey-detail", args=(1,)))
        self.assertEqual(response.status_code, 200)
