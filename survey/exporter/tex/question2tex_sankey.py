# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

import logging

from django.utils.translation import ugettext_lazy as _
from future import standard_library
from pandas.core.frame import DataFrame

from survey.exporter.tex.question2tex import Question2Tex
from survey.exporter.tex.sankey import sankey
from survey.models.question import Question

standard_library.install_aliases()


LOGGER = logging.getLogger(__name__)


class Question2TexSankey(Question2Tex):

    """
        This class permit to generate latex code directly from the Question
        object.
    """

    TEX_SKELETON = """
\\begin{figure}[h!]
    \\includegraphics[width=\\textwidth]{%s}
    \\caption{\\label{figure:q%dvsq%d}%s}
\\end{figure}
"""

    def get_caption_specifics(self):
        caption = "%s '%s' (%s) " % (
            _("for the question"),
            Question2Tex.html2latex(self.question.text),  _("left"),
        )
        caption += "%s '%s' (%s) " % (
            _("in relation with the question"),
            Question2Tex.html2latex(self.other_question.text), _("right"),
        )
        return caption

    def tex(self, other_question):
        """ Return a tikz Sankey Diagram of two questions.

        The question used during initialization will be left and down the other
        question will be right and up. Cardinality constraint used for the
        other question are the same for both question.

        See this question https://tex.stackexchange.com/questions/40159/
        in order for it to work with your latex file.

        :param Question other_question: the question we compare to. """
        if not isinstance(other_question, Question):
            msg = "Expected a 'Question' and got '{}'".format(other_question)
            msg += " (a '{}').".format(other_question.__class__.__name__)
            raise TypeError(msg)
        self.other_question = other_question
        self.cardinality = self.question.sorted_answers_cardinality(
            self.min_cardinality, self.group_together,
            self.group_by_letter_case, self.group_by_slugify, self.filter,
            self.sort_answer, other_question=other_question
        )
        q1 = []
        q2 = []
        for answer_to_q1, cardinality_to_q2 in self.cardinality.items():
            for answer_to_q2, number_of_time in cardinality_to_q2.items():
                for _ in range(number_of_time):
                    q1.append(answer_to_q1)
                    q2.append(answer_to_q2)
        df = DataFrame(data={self.question.text: q1, other_question.text: q2})
        name = "tex/q{}_vs_q{}".format(self.question.pk, other_question.pk)
        sankey(df[self.question.text], df[other_question.text], aspect=20,
               fontsize=10, figure_name=name)
        return Question2TexSankey.TEX_SKELETON % (name[4:],
                                                  self.question.pk,
                                                  other_question.pk,
                                                  self.get_caption())
