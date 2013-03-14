#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2006 Bermi Ferrer Martinez
#
# bermi a-t bermilabs - com
#
import unittest
from inflector import Inflector, English


class EnglishInflectorTestCase(unittest.TestCase):
    singular_to_plural = {
        "search": "searches",
        "switch": "switches",
        "fix": "fixes",
        "box": "boxes",
        "process": "processes",
        "address": "addresses",
        "case": "cases",
        "stack": "stacks",
        "wish": "wishes",
        "fish": "fish",

        "category": "categories",
        "query": "queries",
        "ability": "abilities",
        "agency": "agencies",
        "movie": "movies",

        "archive": "archives",

        "index": "indices",

        "wife": "wives",
        "safe": "saves",
        "half": "halves",

        "move": "moves",

        "salesperson": "salespeople",
        "person": "people",

        "spokesman": "spokesmen",
        "man": "men",
        "woman": "women",

        "basis": "bases",
        "diagnosis": "diagnoses",

        "datum": "data",
        "medium": "media",
        "analysis": "analyses",

        "node_child": "node_children",
        "child": "children",

        "experience": "experiences",
        "day": "days",

        "comment": "comments",
        "foobar": "foobars",
        "newsletter": "newsletters",

        "old_news": "old_news",
        "news": "news",

        "series": "series",
        "species": "species",

        "quiz": "quizzes",

        "perspective": "perspectives",

        "ox": "oxen",
        "photo": "photos",
        "buffalo": "buffaloes",
        "tomato": "tomatoes",
        "dwarf": "dwarves",
        "elf": "elves",
        "information": "information",
        "equipment": "equipment",
        "bus": "buses",
        "status": "statuses",
        "mouse": "mice",

        "louse": "lice",
        "house": "houses",
        "octopus": "octopi",
        "virus": "viri",
        "alias": "aliases",
        "portfolio": "portfolios",

        "vertex": "vertices",
        "matrix": "matrices",

        "axis": "axes",
        "testis": "testes",
        "crisis": "crises",

        "rice": "rice",
        "shoe": "shoes",

        "horse": "horses",
        "prize": "prizes",
        "edge": "edges"
    }

    def setUp(self):
        self.inflector = Inflector(English)

    def tearDown(self):
        self.inflector = None

    def test_pluralize(self):
        for singular, plural in self.singular_to_plural.iteritems():
            inflector_pluralize = self.inflector.pluralize(singular)
            assert inflector_pluralize == plural, \
                'English Inflector pluralize(%s) should produce "%s" and NOT "%s"' % (
                    singular, plural, inflector_pluralize)

    def test_singularize(self):
        for singular, plural in self.singular_to_plural.iteritems():
            inflector_singularize = self.inflector.singularize(plural)
            assert inflector_singularize == singular, \
                'English Inflector singularize(%s) should produce "%s" and NOT "%s"' % (
                    plural, singular, inflector_singularize)


InflectorTestSuite = unittest.TestSuite()
InflectorTestSuite.addTest(EnglishInflectorTestCase("test_pluralize"))
InflectorTestSuite.addTest(EnglishInflectorTestCase("test_singularize"))
runner = unittest.TextTestRunner()
runner.run(InflectorTestSuite)
