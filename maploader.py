# -*- coding: utf-8 -*-

from terrain import Terrain, TERRAINS_HASH
import sys

class Map(object):

    def __init__(self, mapname):
        self.map = []
        self.loadmap(mapname)

    def loadmap(self, mapname):
        with open(mapname, "r") as fp:
            for line in fp:
                current_line = []
                for cell in line:
                    current_line.append({
                        'terrain' : TERRAINS_HASH.get(cell, Terrain)(),
                        })
                self.map.append(current_line)

    def get_cell(self, x, y):
        return self.map[y][x]

    def printmap(self):
        for l in self.map:
            for c in l:
                disp = "%s%s" % (c['terrain'], c.get('building', ' '))
                sys.stdout.write(disp)
            sys.stdout.write("\n")

    def register_building(self, building):
        self.map[building.y][building.x]['building'] = building
