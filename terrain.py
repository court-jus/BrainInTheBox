# -*- coding: utf-8 -*-

import resources
import building

class Terrain(object):
    ascii_repr = ' '
    _name = 'terrain'
    resource_types = {}
    buildable = [building.EarthExtractor, building.WoodExtractor]

    def step(self):
        pass

    def __str__(self):
        return self.ascii_repr

    def has_resource(self, res_type):
        return self.resource_types.get(res_type, 0)

    def getInfo(self):
        result  = "%s" % (self._name)
        if self.resource_types:
            result += " containing %s" % ", ".join([
                "%s %s" % (v, k._name)
                for k, v in self.resource_types.items()])
        return result

class Sea(Terrain):
    ascii_repr = '~'
    _name = 'sea'
    buildable = []

class Plain(Terrain):
    ascii_repr = '#'
    _name = 'plain'
    resource_types = {
        resources.Earth: 30,
        }

TERRAINS_HASH = {
    '~' : Sea,
    '#' : Plain,
    }
