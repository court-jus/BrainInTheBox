# -*- coding: utf-8 -*-

from resources import Earth, Wood
import logging

logger = logging.getLogger("buildings")

class Building(object):
    hp = 100
    _name = "building"

    def __init__(self, cell):
        self.cell = cell

    def step(self):
        pass

    def __str__(self):
        return "]"

    def getInfo(self):
        return str(self)

class Factory(Building):
    resource = None
    efficiency = 1
    _name = "factory"

    def __init__(self, cell):
        super(Factory, self).__init__(cell)
        self.active = False
        self.determine_efficiency()

    def step(self):
        self.cell.map.game.stock[self.resource] = self.cell.map.game.stock.get(self.resource, 0) + 1
        logger.debug("added 1 to %s : %s", self.resource, self.cell.map.game.stock)

    def determine_efficiency(self):
        self.efficiency = self.efficiency * self.cell.terrain.has_resource(self.resource)

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
