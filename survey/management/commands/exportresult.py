# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

import logging

from django.utils import translation
from future import standard_library

from survey.exporter.csv import Survey2Csv
from survey.exporter.tex.configuration import Configuration
from survey.exporter.tex.survey2tex import Survey2Tex
from survey.management.survey_command import SurveyCommand

standard_library.install_aliases()

LOGGER = logging.getLogger(__name__)


class Command(SurveyCommand):

    """
        See the "help" var.
    """

    help = u"""This command permit to export all survey in the database as csv
               and tex."""

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument('--configuration-file', '-c', type=str,
                            help='Path to the tex configuration file.')
        parser.add_argument(
            '--force', "-f", action="store_true", help='Force the generation, '
            'even if the file already exists. Default is False.'
        )
        parser.add_argument(
            '--csv', action="store_true",
            help='Export as csv. Default is False.'
        )
        parser.add_argument(
            '--tex', action="store_true",
            help='Export as tex. Default is False.'
        )
        parser.add_argument(
            '--pdf', action="store_true",
            help='Equivalent to --tex but we will also try to compile the pdf.'
        )
        parser.add_argument(
            '--language', help='Permit to change the language used for '
            'generation (default is defined in the settings).'
        )

    def check_nothing_at_all(self, options):
        SurveyCommand.check_nothing_at_all(self, options)
        if not options["csv"] and not options["tex"] and not options["pdf"]:
            exit("Nothing to do : add option --tex or --pdf, --csv,  or both.")

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)
        translation.activate(options.get("language"))
        for survey in self.surveys:
            LOGGER.info("Generating results for '%s'", survey)
            exporters = []
            if options["csv"]:
                exporters.append(Survey2Csv(survey))
            if options["tex"] or options["pdf"]:
                configuration_file = options.get("configuration_file")
                if configuration_file is None:
                    msg = "No configuration file given, using default values."
                    LOGGER.warning(msg)
                configuration = Configuration(configuration_file)
                exporters.append(Survey2Tex(survey, configuration))
            for exporter in exporters:
                if options["force"] or exporter.need_update():
                    exporter.generate_file()
                    if options["pdf"] and type(exporter) is Survey2Tex:
                        exporter.generate_pdf()
                else:
                    LOGGER.info("\t- %s's %s were already generated use the "
                                "--force (-f) option to generate anyway.",
                                survey, exporter._get_X())
