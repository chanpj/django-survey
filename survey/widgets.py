# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from builtins import object

from django import forms
from django.template.loader import render_to_string
from future import standard_library

standard_library.install_aliases()



class ImageSelectWidget(forms.widgets.Widget):

    class Media(object):
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js',
            'http://maps.googleapis.com/maps/api/js?sensor=false',
            'js/survey.js',
        )

    def render(self, name, value, *args, **kwargs):
        template_name = "survey/forms/image_select.html"
        choices = []
        for index, choice in enumerate(self.choices):
            if choice[0] != '':
                value, img_src = choice[0].split(":", 1)
                choices.append({
                    'img_src': img_src,
                    'value': value,
                    'full_value': choice[0],
                    'index': index
                })
        context = {'name': name, 'choices': choices}
        html = render_to_string(template_name, context)
        return html
