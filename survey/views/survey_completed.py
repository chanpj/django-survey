# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from future import standard_library

from survey.models import Survey

standard_library.install_aliases()



class SurveyCompleted(TemplateView):

    template_name = 'survey/completed.html'

    def get_context_data(self, **kwargs):
        context = {}
        survey = get_object_or_404(Survey, is_published=True, id=kwargs['id'])
        context['survey'] = survey
        return context
