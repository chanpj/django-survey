# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.conf.urls import url
from future import standard_library

from survey.views import ConfirmView, IndexView, SurveyCompleted, SurveyDetail
from survey.views.survey_result import serve_result_csv

standard_library.install_aliases()


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='survey-list'),
    url(r'^(?P<id>\d+)/', SurveyDetail.as_view(), name='survey-detail'),
    url(r'^csv/(?P<pk>\d+)/', serve_result_csv, name='survey-result'),
    url(r'^(?P<id>\d+)/completed/', SurveyCompleted.as_view(),
        name='survey-completed'),
    url(r'^(?P<id>\d+)-(?P<step>\d+)/', SurveyDetail.as_view(),
        name='survey-detail-step'),
    url(r'^confirm/(?P<uuid>\w+)/', ConfirmView.as_view(),
        name='survey-confirmation'),
]
