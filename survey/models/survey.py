# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from builtins import object

from django.db import models
from django.utils.translation import ugettext_lazy as _
from future import standard_library

standard_library.install_aliases()


class Survey(models.Model):

    name = models.CharField(_("Name"), max_length=400)
    description = models.TextField(_("Description"), )
    is_published = models.BooleanField(_("Users can see it and answer it"),)
    need_logged_user = models.BooleanField(_("Only authenticated users can see it and answer it"),)
    display_by_question = models.BooleanField(_("Display by question"),)
    template = models.CharField(_("Template"), max_length=255, null=True, blank=True)

    class Meta(object):
        verbose_name = _('survey')
        verbose_name_plural = _('surveys')

    def __str__(self):
        return self.name

    def latest_answer_date(self):
        """ Return the latest answer date.

        Return None is there is no response. """
        min_ = None
        for response in self.responses.all():
            if min_ is None or min_ < response.updated:
                min_ = response.updated
        return min_

    @models.permalink
    def get_absolute_url(self):
        return ('survey-detail', [self.pk])
