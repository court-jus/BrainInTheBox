#!/usr/bin/env python
# -*- coding: utf-8 -*-

from building import EarthExtractor
from maploader import Map
from textui import TextUI

def main():
    ml = Map("map.txt")
    ee = EarthExtractor(ml, 20, 10)
    #ml.printmap()
    ui = TextUI(ml)
    ui.run()

if __name__ == "__main__":
    main()
