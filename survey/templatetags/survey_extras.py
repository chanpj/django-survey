# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django import template
from future import standard_library

standard_library.install_aliases()

register = template.Library()


def collapse_form(form, category):
    """ Permit to return the class of the collapsible according to errors in
    the form. """
    categories_with_error = set()
    for field in form:
        if field.errors:
            categories_with_error.add(field.field.widget.attrs["category"])
    if category.name in categories_with_error:
        return "in"
    return ""

register.filter('collapse_form', collapse_form)


class CounterNode(template.Node):

    def __init__(self):
        self.count = 0

    def render(self, context):
        self.count += 1
        return self.count


@register.tag
def counter(parser, token):
    return CounterNode()
