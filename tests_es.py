#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2006 Bermi Ferrer Martinez
#
# bermi a-t bermilabs - com
#
import unittest
from inflector import Inflector
from rules.spanish import Spanish


class SpanishInflectorTestCase(unittest.TestCase):
    singular_to_plural = {
        "almacén": "almacenes",
        "androide": "androides",
        "antifaz": "antifaces",
        "árbol": "árboles",
        "atlas": "atlas",
        "autobús": "autobuses",
        "base": "bases",
        "bebé": "bebés",
        "camión": "camiones",
        "casa": "casas",
        "ceutí": "ceutíes",
        "chimpancé": "chimpancés",
        "clan": "clanes",
		"convoy": "convoyes",
        "coxis": "coxis",
        "crisis": "crisis",
        "eje": "ejes",
        "espíritu": "espíritus",
        "flash": "flashes",
        "frac": "fracs",
        "gafas": "gafas",
        "hipótesis": "hipótesis",    
        "inglés": "ingleses",
        "lápiz": "lápices",
        "luz": "luces",
        "montaje": "montajes",
        "no": "noes",
        "otitis": "otitis",
        "padre": "padres",
        "país": "países",
        "papá": "papás",
        "parking": "parkings",
        "portaequipaje": "portaequipajes",
        "radiocasete": "radiocasetes",
        "show": "shows",
        #"si": "sis",
        "sí": "síes",
        "tabú": "tabúes",
        "tamiz": "tamices",
        "tanque": "tanques",
        "taxi": "taxis",
        "tijeras": "tijeras",
        "tren": "trenes",
        "virus": "virus",
    }

    def setUp(self):
        self.inflector = Inflector(Spanish)

    def tearDown(self):
        self.inflector = None

    def test_pluralize(self):
        for singular, plural in self.singular_to_plural.iteritems():
            inflector_pluralize = self.inflector.pluralize(singular)
            assert inflector_pluralize == plural, \
                'Spanish Inflector pluralize(%s) should produce "%s" and NOT "%s"' % (
                    singular, plural, inflector_pluralize)

    def test_singularize(self):
        for singular, plural in self.singular_to_plural.iteritems():
            inflector_singularize = self.inflector.singularize(plural)
            assert inflector_singularize == singular, \
                'Spanish Inflector singularize(%s) should produce "%s" and NOT "%s"' % (
                    plural, singular, inflector_singularize)


InflectorTestSuite = unittest.TestSuite()
InflectorTestSuite.addTest(SpanishInflectorTestCase("test_pluralize"))
InflectorTestSuite.addTest(SpanishInflectorTestCase("test_singularize"))
runner = unittest.TextTestRunner()
runner.run(InflectorTestSuite)
