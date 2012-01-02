#!/usr/bin/env python
# -*- coding: utf-8 -*-

from building import EarthExtractor
from maploader import Map

def main():
    ml = Map("map.txt")
    ee = EarthExtractor(ml, 20, 10)
    ml.printmap()
    print ee.efficiency

if __name__ == "__main__":
    main()
