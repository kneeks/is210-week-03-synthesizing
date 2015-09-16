#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

WRDCT = len('Spanish')

POS = inquisition.SPANISH.index('Spanish')

REPLCE = 'Flemish'

FLEMISH = (inquisition.SPANISH[:POS] + REPLCE + inquisition.SPANISH[POS+WRDCT:])
