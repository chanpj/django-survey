# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.utils.translation import ugettext_lazy as _
from future import standard_library

from survey.exporter.tex.question2tex import Question2Tex

standard_library.install_aliases()


class Question2TexRaw(Question2Tex):

    """
        This class permit to generate latex code directly from the Question
        object.
    """

    TEX_SKELETON = """
\\begin{quote}
%s
\\end{quote} \hfill (%s n\\textsuperscript{o}%s)
"""

    def tex(self):
        """ Return all the answer as quote in latex. """
        raw_answers = ""
        for i, answer in enumerate(self.cardinality):
            if answer:
                raw_answers += Question2TexRaw.TEX_SKELETON % (
                    answer, _("Participant"), i
                )
        return raw_answers
