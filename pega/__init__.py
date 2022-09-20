# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2022-present Ramiro Gómez <code@ramiro.org>
#
# SPDX-License-Identifier: MIT


def dimensions(im, margins):
    return im.width - margins[1] - margins[3], im.height - margins[0] - margins[2]