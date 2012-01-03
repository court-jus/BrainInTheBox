# -*- coding: utf-8 -*-

from terrain import Terrain, TERRAINS_HASH
import sys

class MapCell(object):

    def __init__(self, terrain_class):
        self.terrain = terrain_class()
        self.building = None

    def getRepr(self):
        return "%s%s" % (self.terrain, self.getBuilding())

    def getInfo(self):
        result = [self.terrain.getInfo()]
        if self.building:
            result.append(self.building.getInfo())
        return "\n".join(result)

    def getBuilding(self, default = " "):
        if not self.building:
            return default
        return self.building

class Map(object):

    def __init__(self, mapname):
        self.map = []
        self.loadmap(mapname)

    def loadmap(self, mapname):
        with open(mapname, "r") as fp:
            for line in fp:
                current_line = []
                for cell in line.rstrip():
                    current_line.append(MapCell(TERRAINS_HASH.get(cell, Terrain)))
                self.map.append(current_line)

    def get_cell(self, x, y):
        return self.map[y][x]

    def getSize(self):
        return len(self.map[0]), len(self.map)

    def printmap(self):
        for l in self.map:
            for c in l:
                sys.stdout.write(c.getRepr())
            sys.stdout.write("\n")

    def register_building(self, building):
        self.map[building.y][building.x].building = building
