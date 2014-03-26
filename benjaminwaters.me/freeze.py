#!/usr/bin/env python
# encoding: utf-8

from app import app
from flask_frozen import Freezer


def freeze():
    freezer = Freezer(app)
    freezer.freeze()

if __name__ == '__main__':
    freeze()
