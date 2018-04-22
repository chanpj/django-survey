# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from builtins import object

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from future import standard_library

from .survey import Survey

try:
    from django.conf import settings
    if settings.AUTH_USER_MODEL:
        user_model = settings.AUTH_USER_MODEL
    else:
        user_model = User
except (ImportError, AttributeError):
    user_model = User

standard_library.install_aliases()


class Response(models.Model):

    """
        A Response object is a collection of questions and answers with a
        unique interview uuid.
    """

    created = models.DateTimeField(_("Creation date"), auto_now_add=True)
    updated = models.DateTimeField(_("Update date"), auto_now=True)
    survey = models.ForeignKey(Survey, verbose_name=_("Survey"),
                               related_name="responses")
    user = models.ForeignKey(user_model, verbose_name=_("User"), null=True,
                             blank=True)
    interview_uuid = models.CharField(_(u"Interview unique identifier"),
                                      max_length=36)

    class Meta(object):
        verbose_name = _('Set of answers to surveys')
        verbose_name_plural = _('Sets of answers to surveys')

    def __str__(self):
        msg = u"Response to {} by {}".format(self.survey, self.user)
        msg += u" on {}".format(self.created)
        return msg
