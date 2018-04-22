# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from builtins import super

from django.views.generic import TemplateView
from future import standard_library

standard_library.install_aliases()


class ConfirmView(TemplateView):

    template_name = 'survey/confirm.html'

    def get_context_data(self, **kwargs):
        context = super(ConfirmView, self).get_context_data(**kwargs)
        context['uuid'] = kwargs['uuid']
        return context
