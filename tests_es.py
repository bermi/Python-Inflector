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
        "árbol": "árboles",
        "clan": "clanes",
        "camión": "camiones",
        "autobús": "autobuses",
        "clan": "clanes",
        "tren": "trenes",
        "espíritu": "espíritus",
        "chimpancé": "chimpancés",
        "casa": "casas",
        "padre": "padres",
        "papá": "papás",
        "atlas": "atlas",
        "virus": "virus",
        "ceutí": "ceutíes",
        "tabú": "tabúes",
        "frac": "frac",
        "show": "shows",
        "parking": "parkings",
        "árbol": "árboles",
        "tijeras": "tijeras",
        "gafas": "gafas",
        "país": "países",
        "luz": "luces",
        "almacén": "almacenes",
        "inglés": "ingleses",
        "flashes": "flash",
        "montajes": "montaje",
        "portaequipajes": "portaequipaje",
        "ejes": "eje",
        "lápices": "lápiz",
        "antifaces": "antifaz",
        "bases": "base"
    }

    def setUp(self):
        self.inflector = Inflector(Spanish)

    def tearDown(self):
        self.inflector = None

    def test_pluralize(self):
        for singular in self.singular_to_plural.keys():
            assert self.inflector.pluralize(singular) == self.singular_to_plural[singular], \
                'Spanish Inlector pluralize(%s) should produce "%s" and NOT "%s"' % (
                singular, self.singular_to_plural[singular], self.inflector.pluralize(singular))

    def test_singularize(self):
        for singular in self.singular_to_plural.keys():
            assert self.inflector.singularize(self.singular_to_plural[singular]) == singular, \
                'Spanish Inlector singularize(%s) should produce "%s" and NOT "%s"' % (
                self.singular_to_plural[singular], singular, self.inflector.singularize(self.singular_to_plural[singular]))


InflectorTestSuite = unittest.TestSuite()
InflectorTestSuite.addTest(SpanishInflectorTestCase("test_pluralize"))
InflectorTestSuite.addTest(SpanishInflectorTestCase("test_singularize"))
runner = unittest.TextTestRunner()
runner.run(InflectorTestSuite)
