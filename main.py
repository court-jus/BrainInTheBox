#!/usr/bin/env python
# -*- coding: utf-8 -*-

from building import EarthExtractor
from maploader import Map
from textui import TextUI

import logging
logging.basicConfig(filename = "bib.log", level = logging.DEBUG)

class BrainInTheBox(object):

    def __init__(self):
        self.stock = {}
        self.map = Map(self, "map.txt")

def main():
    game = BrainInTheBox()
    #ee = EarthExtractor(ml, 20, 10)
    #ml.printmap()
    ui = TextUI(game)
    ui.run()

if __name__ == "__main__":
    main()
