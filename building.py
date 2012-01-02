# -*- coding: utf-8 -*-

from resources import Earth, Wood

class Building(object):
    hp = 100

    def __init__(self, map, x, y):
        self.map = map
        self.x = x
        self.y = y
        self.map.register_building(self)

    def __str__(self):
        return "]"

class Factory(Building):
    resource = None
    efficiency = 1

    def __init__(self, map, x, y):
        super(Factory, self).__init__(map, x, y)
        self.active = False
        self.determine_efficiency()

    def determine_efficiency(self):
        cell = self.map.get_cell(self.x, self.y)
        self.efficiency = self.efficiency * cell['terrain'].has_resource(self.resource)

    def __str__(self):
        return "+"

class EarthExtractor(Factory):
    resource = Earth

    def __str__(self):
        return "E"

class WoodExtractor(Factory):
    resource = Wood
