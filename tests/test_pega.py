# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2022-present Ramiro Gómez <code@ramiro.org>
#
# SPDX-License-Identifier: MIT
from PIL import Image

from pega import dimensions


def test_dimensions():
    im = Image.new('RGBA', (1000, 1000))
    margins = (840, 40, 40, 840)
    dim = dimensions(im, margins)
    assert dim == (120, 120)
