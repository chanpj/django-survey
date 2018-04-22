# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from future import standard_library

from survey.views.confirm_view import ConfirmView
from survey.views.index_view import IndexView
from survey.views.survey_completed import SurveyCompleted
from survey.views.survey_detail import SurveyDetail

standard_library.install_aliases()

__all__ = ["SurveyCompleted", "IndexView", "ConfirmView", "SurveyDetail"]
