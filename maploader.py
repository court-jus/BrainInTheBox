# -*- coding: utf-8 -*-

from terrain import Terrain, TERRAINS_HASH
import sys
import logging
logger = logging.getLogger("map")

class MapCell(object):

    def __init__(self, map, terrain_class):
        self.map = map
        self.terrain = terrain_class()
        self.building = None

    def step(self):
        self.terrain.step()
        if self.building:
            self.building.step()

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
    
    def canBuild(self):
        if self.building:
            return False
        return self.terrain.buildable

    def build(self, what):
        self.building = what(self)

class Map(object):

    def __init__(self, game, mapname):
        self.game = game
        self.map = []
        self.loadmap(mapname)

    def loadmap(self, mapname):
        with open(mapname, "r") as fp:
            for line in fp:
                current_line = []
                for cell in line.rstrip():
                    current_line.append(MapCell(self, TERRAINS_HASH.get(cell, Terrain)))
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

    def step(self):
        logger.debug("Map step : %s", self)
        for line in self.map:
            for cell in line:
                cell.step()
