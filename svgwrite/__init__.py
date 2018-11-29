#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: package definition file
# Created: 08.09.2010
# License: MIT License
# Copyright (c) 2010-2018  Manfred Moitzi

"""
A Python library to create SVG drawings.

SVG is a language for describing two-dimensional graphics in XML. SVG allows
for three types of graphic objects: vector graphic shapes (e.g., paths
consisting of straight lines and curves), images and text. Graphical objects
can be grouped, styled, transformed and composed into previously rendered
objects. The feature set includes nested transformations, clipping paths,
alpha masks, filter effects and template objects.

SVG drawings can be interactive and dynamic. Animations can be defined and
triggered either declarative (i.e., by embedding SVG animation elements in
SVG content) or via scripting.

.. seealso:: http://www.w3.org/TR/SVG11/intro.html#AboutSVG

a simple example::

    import svgwrite

    dwg = svgwrite.Drawing('test.svg', profile='tiny')
    dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
    dwg.add(dwg.text('Test', insert=(0, 0.2)))
    dwg.save()

SVG Version
-----------

You can only create two types of SVG drawings:

* *SVG 1.2 Tiny Profile*, use Drawing(profile= ``'tiny'``)
* *SVG 1.1 Full Profile*, use Drawing(profile= ``'full'``)

"""
# 2018-11-29: future consistent version numbers
# ---------------------------------------------
#
# version scheme for __version__: (major, minor, micro, release_level)
#
# major:
#   0 .. not all planned features done
#   1 .. all features available
#   2 .. if significant API change (2, 3, ...)
#
# minor:
#   changes with new features or minor API changes
#
# micro:
#   changes with bug fixes, maybe also minor changes
#
# release_state:
#   a .. alpha: adding new features - non public development state
#   b .. beta: testing new features - public development state
#   rc .. release candidate: testing release - public testing
#   release: public release
# examples
#
# major pre release alpha 2: VERSION = "0.9a2"; __version__ = (0, 9, 0, 'a2')
# major release candidate 0: VERSION = "0.9rc0"; __version__ = (0, 9, 0, 'rc0')
# major release: VERSION = "0.9"; __version__ = (0, 9, 0, 'release')
# 1. bug fix release beta0: VERSION = "0.9.1b0"; __version__ = (0, 9, 1, 'b0')
# 2. bug fix release: VERSION = "0.9.2"; __version__ = (0, 9, 2, 'release')

version = (1, 3, 0, 'a1')  # also update setup.py
VERSION = '1.3a1'

AUTHOR_NAME = 'Manfred Moitzi'
AUTHOR_EMAIL = 'me@mozman.at'
CYEAR = '2014-2018'

from svgwrite.drawing import Drawing
from svgwrite.utils import rgb


class Unit(object):
    """ Add units to values.
    """
    def __init__(self, unit='cm'):
        """ Unit constructor

        :param str unit: specify the unit string
        """
        self._unit = unit

    def __rmul__(self, other):
        """ add unit-string to 'other'. (e.g. 5*cm => '5cm') """
        return "%s%s" % (other, self._unit)

    def __call__(self, *args):
        """ Add unit-strings to all arguments.

        :param args: list of values
            e.g.: cm(1,2,3) => '1cm,2cm,3cm'
        """
        return ','.join(["%s%s" % (arg, self._unit) for arg in args])

cm = Unit('cm')
mm = Unit('mm')
em = Unit('em')
ex = Unit('ex')
px = Unit('px')
inch = Unit('in')
pc = Unit('pc')
pt = Unit('pt')
percent = Unit('%')
deg = Unit('deg')
grad = Unit('grad')
rad = Unit('rad')
Hz = Unit('Hz')
kHz = Unit('kHz')
