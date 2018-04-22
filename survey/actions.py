# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext
from future import standard_library

standard_library.install_aliases()


def make_published(modeladmin, request, queryset):
    """
    Mark the given survey as published
    """
    count = queryset.update(is_published=True)
    message = ungettext(
        u'%(count)d survey was successfully marked as published.',
        u'%(count)d surveys were successfully marked as published',
        count
    ) % {'count': count, }
    modeladmin.message_user(request, message)
    make_published.short_description = _(u"Mark selected surveys as published")
