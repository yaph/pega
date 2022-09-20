# pega

A command line tool for pasting images on top of other images.

## Installation

```console
pip install pega
```

## Sample Commands

Paste 1 image on base image.

    python pega/cli.py tests/images/base-1000x1000-m100-0-200-0.png tests/images/green-tree-python-226553_1920.jpg

For all JPEG files in directory create a new image with the JPEG pasted on the base image.

    python pega/cli.py tests/images/base-1000x1000-m100-0-200-0.png tests/images/*.jpg

Specify margins of pasted image relative to base and output directory.

    python pega/cli.py tests/images/base-1000x1000-m100-0-200-0.png tests/images/green-tree-python-226553_1920.jpg \
        --margins 140 40 240 40 --output-dir tests/output/

## FIXME

This command fails with the exception: "ValueError: images do not match"

    python pega/cli.py tests/images/base-1000x1000-m100-0-200-0.png tests/images/base-1000x1000-m100-0-200-0.png --margins 840 40 40 840 --output-dir tests/output/

## Credits

Test images:

* [green-tree-python-226553_1920.jpg](https://pixabay.com/photos/226553)
* [line-660781_1920.jpg](https://pixabay.com/photos/660781)
* [snake-1285354_640.jpg](https://pixabay.com/photos/1285354)
* [snake-37585_640.png](https://pixabay.com/photos/37585/)

## License

`pega` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
