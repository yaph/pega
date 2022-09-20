#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2022-present Ramiro Gómez <code@ramiro.org>
# SPDX-License-Identifier: MIT
import argparse
import sys
import timeit

from pathlib import Path

from PIL import Image

from pega import dimensions


def main():
    start_time = timeit.default_timer()
    parser = argparse.ArgumentParser(description='Paste images on top of other images.')
    parser.add_argument('base', type=argparse.FileType('rb'), default=sys.stdin,
                        help='Base image file name.')
    parser.add_argument('paste', type=str, nargs='+',
                        help='Image to paste on base image. Use wildcard to process multiple files.')
    parser.add_argument('--margins', '-m', type=int, nargs=4, default=[0, 0, 0, 0],
                        help='Top, right, bottom, and left (mnemonic: trouble) margins of pasted image relative to base image.')
    parser.add_argument('--output-dir', '-o', type=Path, help='Write result image to directory.')
    parser.add_argument('--verbose', '-v', action='store_true', help='Turn on verbose output.')
    cli_args = parser.parse_args()

    with Image.open(cli_args.base) as im_base:
        im_base.load()
    # Make sure transparent parts in pasted image are retained.
    im_base = im_base.convert('RGBA')

    for file_name in cli_args.paste:
        with Image.open(file_name) as im_paste:
            im_paste.load()

        # Create new image for each image to paste.
        im_new = im_base.copy()

        # Fit image into calculated dimensions, while preserving its aspect ratio.
        dim = dimensions(im_base, cli_args.margins)
        im_paste.thumbnail(dim)

        # If dimensions don't match, create a temporary image with correct size and center image to paste on it.
        if im_paste.size != dim:
            im_tmp = Image.new('RGBA', dim)
            x = int((dim[0] - im_paste.width) / 2)
            y = int((dim[1] - im_paste.height) / 2)
            im_tmp.paste(im_paste, box=(x, y))
            im_paste = im_tmp

        # Use `alpha_composite` because `paste` would keep transparency in pasted image.
        im_new.alpha_composite(im_paste, dest=(cli_args.margins[3], cli_args.margins[0]))
        im_new.save(cli_args.output_dir.joinpath(Path(file_name).stem + '.png'))

    cli_args.verbose and print(f'Script runtime: {timeit.default_timer() - start_time:.3f} sec', )


if __name__ == '__main__':
    main()
