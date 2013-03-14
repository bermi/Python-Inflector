#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
# Copyright (c) 2006 Bermi Ferrer Martinez
# Copyright (c) 2006 Carles Sadurní Anguita
#
# bermi a-t bermilabs - com
#
# See the end of this file for the free software, open source license
# (BSD-style).

import re
from base import Base
import utils


class Spanish (Base):
    '''
    Inflector for pluralize and singularize Spanish nouns.
    '''

    irregular_words = {
        u'base': u'bases',
        u'carácter': u'caracteres',
        u'champú': u'champús',
        u'curriculum': u'currículos',
        u'espécimen': u'especímenes',
        u'jersey': u'jerséis',
        u'memorándum': u'memorandos',
        u'menú': u'menús',
        u'no': u'noes',
        u'país': u'países',
        u'referéndum': u'referendos',
        u'régimen': u'regímenes',
        u'sándwich': u'sándwiches',
        #u'si': u'sis', # Nota musical ALERTA: ¡provoca efectos secundarios!
        u'taxi': u'taxis', 
        u'ultimátum': u'ultimatos',
        }

    # These words either have the same form in singular and plural, or have no singular form at all
    non_changing_words = [
        u'lunes', u'martes', u'miércoles', u'jueves', u'viernes',
        u'paraguas', u'tijeras', u'gafas', u'vacaciones', u'víveres',
        u'cumpleaños', u'virus', u'atlas', u'sms', u'hummus',
    ]


    def pluralize(self, word):
        '''
        Pluralizes Spanish nouns.
        Input string can be Unicode (e.g. u"palabra"), or a str encoded in UTF-8 or Latin-1.
        Output string will be encoded the same way as the input.
        '''

        word, origType = utils.unicodify(word)  # all internal calculations are done in Unicode

        rules = [
            [u'(?i)([aeiou])x$', u'\\1x'],
            # This could fail if the word is oxytone.
            [u'(?i)([áéíóú])([ns])$', u'|1\\2es'],
            [u'(?i)(^[bcdfghjklmnñpqrstvwxyz]*)an$', u'\\1anes'],  # clan->clanes
            [u'(?i)([áéíóú])s$', u'|1ses'],
            [u'(?i)(^[bcdfghjklmnñpqrstvwxyz]*)([aeiou])([ns])$', u'\\1\\2\\3es'],  # tren->trenes
            [u'(?i)([aeiouáéó])$', u'\\1s'],  # casa->casas, padre->padres, papá->papás
            [u'(?i)([aeiou])s$', u'\\1s'],    # atlas->atlas, virus->virus, etc.
            [u'(?i)([éí])(s)$', u'|1\\2es'],  # inglés->ingleses
            [u'(?i)z$', u'ces'],              # luz->luces
            [u'(?i)([íú])$', u'\\1es'],       # ceutí->ceutíes, tabú->tabúes
            [u'(?i)(ng|[wckgtp])$', u'\\1s'], # Anglicismos como puenting, frac, crack, show (En que casos podría fallar esto?)
            [u'(?i)$', u'es']  # ELSE +es (v.g. árbol->árboles)
        ]

        lower_cased_word = word.lower()

        for uncountable_word in self.non_changing_words:
            if lower_cased_word[-1 * len(uncountable_word):] == uncountable_word:
                return utils.deunicodify(word, origType)

        for irregular_singular, irregular_plural in self.irregular_words.iteritems():
            match = re.search(u'(?i)(' + irregular_singular + u')$', word, re.IGNORECASE)
            if match:
                result = re.sub(u'(?i)' + irregular_singular + u'$', match.expand(u'\\1')[0] + irregular_plural[1:], word)
                return utils.deunicodify(result, origType)

        for rule in rules:
            match = re.search(rule[0], word, re.IGNORECASE)
            if match:
                groups = match.groups()
                replacement = rule[1]
                if re.match(u'\|', replacement):
                    for k in range(1, len(groups)):
                        replacement = replacement.replace(u'|' + unicode(
                            k), self.string_replace(groups[k - 1], u'ÁÉÍÓÚáéíóú', u'AEIOUaeiou'))

                result = re.sub(rule[0], replacement, word)
                # Esto acentúa los sustantivos que al pluralizarse se
                # convierten en esdrújulos como esmóquines, jóvenes...
                match = re.search(u'(?i)([aeiou]).{1,3}([aeiou])nes$', result)

                if match and len(match.groups()) > 1 and not re.search(u'(?i)[áéíóú]', word):
                    result = result.replace(match.group(0), self.string_replace(
                        match.group(1), u'AEIOUaeiou', u'ÁÉÍÓÚáéíóú') + match.group(0)[1:])

                return utils.deunicodify(result, origType)

        return utils.deunicodify(word, origType)


    def singularize(self, word):
        '''
        Singularizes Spanish nouns.
        Input string can be Unicode (e.g. u"palabras"), or a str encoded in UTF-8 or Latin-1.
        Output string will be encoded the same way as the input.
        '''

        word, origType = utils.unicodify(word)  # all internal calculations are done in Unicode

        rules = [
            [ur'(?i)^([bcdfghjklmnñpqrstvwxyz]*)([aeiou])([ns])es$', u'\\1\\2\\3'],
            [ur'(?i)([aeiou])([ns])es$', u'~1\\2'],
            [ur'(?i)shes$', u'sh'],             # flashes->flash
            [ur'(?i)oides$', u'oide'],          # androides->androide
            [ur'(?i)(sis|tis|xis)$', u'\\1'],   # crisis, apendicitis, praxis
            [ur'(?i)(é)s$', u'\\1'],            # bebés->bebé
            [ur'(?i)(ces)$', u'z'],             # luces->luz
            [ur'(?i)([^e])s$', u'\\1'],         # casas->casa
            [ur'(?i)([bcdfghjklmnñprstvwxyz]{2,}e)s$', u'\\1'],  # cofres->cofre
            [ur'(?i)([ghñptv]e)s$', u'\\1'],    # llaves->llave, radiocasetes->radiocasete
            [ur'(?i)jes$', u'je'],              # ejes->eje
            [ur'(?i)ques$', u'que'],            # tanques->tanque
            [ur'(?i)es$', u'']                  # ELSE remove _es_  monitores->monitor
        ]

        lower_cased_word = word.lower()

        for uncountable_word in self.non_changing_words:
            if lower_cased_word[-1 * len(uncountable_word):] == uncountable_word:
                return utils.deunicodify(word, origType)

        for irregular_singular, irregular_plural in self.irregular_words.iteritems():
            match = re.search(u'(' + irregular_plural + u')$', word, re.IGNORECASE)
            if match:
                result = re.sub(u'(?i)' + irregular_plural + u'$', match.expand(u'\\1')[0] + irregular_singular[1:], word)
                return utils.deunicodify(result, origType)

        for rule in rules:
            match = re.search(rule[0], word, re.IGNORECASE)
            if match:
                groups = match.groups()
                replacement = rule[1]
                if re.match(u'~', replacement):
                    for k in range(1, len(groups)):
                        replacement = replacement.replace(u'~' + unicode(
                            k), self.string_replace(groups[k - 1], u'AEIOUaeiou', u'ÁÉÍÓÚáéíóú'))

                result = re.sub(rule[0], replacement, word)
                # Esta es una posible solución para el problema de dobles
                # acentos. Un poco guarrillo pero funciona
                match = re.search(u'(?i)([áéíóú]).*([áéíóú])', result)

                if match and len(match.groups()) > 1 and not re.search(u'(?i)[áéíóú]', word):
                    result = self.string_replace(
                        result, u'ÁÉÍÓÚáéíóú', u'AEIOUaeiou')

                return utils.deunicodify(result, origType)

        return utils.deunicodify(word, origType)


# Copyright (c) 2006 Bermi Ferrer Martinez
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software to deal in this software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of this software, and to permit
# persons to whom this software is furnished to do so, subject to the following
# condition:
#
# THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THIS SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THIS SOFTWARE.

