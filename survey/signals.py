# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

import django.dispatch
from future import standard_library

standard_library.install_aliases()

survey_completed = django.dispatch.Signal(providing_args=["instance", "data"])
