#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

WORDCNT = len('Spanish')

POS = inquisition.SPANISH.index('Spanish')

REPLACE = 'Flemish'

FLEMISH = inquisition.SPANISH[:POS] + REPLACE + inquisition.SPANISH[POS+WORDCNT:]

print FLEMISH
