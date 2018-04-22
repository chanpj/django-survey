# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from builtins import super

from django.views.generic import TemplateView
from future import standard_library

from survey.models import Survey

standard_library.install_aliases()



class IndexView(TemplateView):
    template_name = "survey/list.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        surveys = Survey.objects.filter(is_published=True)
        if not self.request.user.is_authenticated():
            surveys = surveys.filter(need_logged_user=False)
        context['surveys'] = surveys
        return context
