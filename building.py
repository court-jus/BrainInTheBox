# -*- coding: utf-8 -*-

from resources import Earth, Wood

class Building(object):
    hp = 100
    _name = "building"

    def __init__(self, map, x, y):
        self.map = map
        self.x = x
        self.y = y
        self.map.register_building(self)

    def __str__(self):
        return "]"

    def getInfo(self):
        return str(self)

class Factory(Building):
    resource = None
    efficiency = 1
    _name = "factory"

    def __init__(self, map, x, y):
        super(Factory, self).__init__(map, x, y)
        self.active = False
        self.determine_efficiency()

    def determine_efficiency(self):
        cell = self.map.get_cell(self.x, self.y)
        self.efficiency = self.efficiency * cell.terrain.has_resource(self.resource)

    def __str__(self):
        return "+"

    def getInfo(self):
        return "%s producing %s at %s efficiency" % (self._name, self.resource._name, self.efficiency)

class EarthExtractor(Factory):
    resource = Earth
    _name = "earth extractor"

    def __str__(self):
        return "E"

class WoodExtractor(Factory):
    resource = Wood
    _name = "wood extractor"
