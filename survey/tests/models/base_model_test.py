# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from future import standard_library

from survey.models import Answer, Question, Response, Survey
from survey.tests import BaseTest

standard_library.install_aliases()


class BaseModelTest(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        self.survey = Survey.objects.create(
            name="Internal Test Survey", is_published=True,
            need_logged_user=False, display_by_question=False
        )
        self.response = Response.objects.create(survey=self.survey)
        self.questions = []
        self.answers = []
        self.data = [
            [Question.TEXT, "Mytext", None],
            [Question.SHORT_TEXT, "Mytext", None],
            [Question.RADIO, "Yes", "Yes, No, Maybe"],
            [Question.SELECT, "No", "Yes, No, Maybe"],
            # [Question.SELECT_IMAGE,Answer, "TODO" ,None],
            [Question.SELECT_MULTIPLE, "Yes", "Yes, No, Maybe"],
            [Question.INTEGER, 42, None],
            [Question.SELECT_MULTIPLE, "[u'2', u'4']", "2, 4, 6"],
        ]
        for i, data in enumerate(self.data):
            qtype, answer_body, answer_choices = data
            question = Question.objects.create(
                text="{} question ?".format(qtype), choices=answer_choices,
                order=i + 1, required=True, survey=self.survey,
                type=qtype,
            )
            self.questions.append(question)
            answer = Answer(
                response=self.response, question=question, body=answer_body
            )
            self.answers.append(answer)
