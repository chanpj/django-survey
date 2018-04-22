# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

import logging
from builtins import open
from datetime import datetime

from future import standard_library

LOGGER = logging.getLogger(__name__)

standard_library.install_aliases()


class LatexFile(object):

    """ Permit to handle the content of a LatexFile """

    def __init__(self, document_class, document_option=None, header=None,
                 intro=None, footer=None, date=None, **kwargs):
        LOGGER.debug("Creating a document skeleton with document_class=%s, "
                     "document_option=%s", document_class, document_option)
        self.document_class = document_class
        self.text = ""
        self.document_option = self.set_value(document_option)
        self._header = self.set_value(header)
        self.intro = self.set_value(intro)
        self._footer = self.set_value(footer)
        if date is None:
            date = datetime.now().strftime("%B %d, %Y")
        self.date = date

    def set_value(self, value):
        """ Return the value we need for null text. """
        if value is None:
            return ""
        return value

    @property
    def header(self):
        """ Return the header of a .tex file.

        :rtype: String """
        header = u"\\documentclass"
        if self.document_option:
            header += u"[{}]".format(self.document_option)
        header += u"{%s}\n" % self.document_class
        header += u"\date{%s}\n" % self.date
        header += u"%s\n" % self._header
        header += u"\\begin{document}\n"
        header += u"%s\n" % self.intro
        return header

    @property
    def footer(self):
        """ Return the footer of a .tex file.

        :rtype: String """
        end = """
\\end{document}
"""
        if self._footer:
            return self._footer + end
        else:
            return end

    def save(self, path):
        """ Save the document on disk. """
        with open(path, 'wb') as tex_file:
            tex_file.write(self.document.encode("UTF-8"))

    @property
    def document(self):
        """ Return the full text of the LatexFile.

        :rtype: String"""
        return u"{}{}{}".format(self.header, self.text, self.footer)
