# -*- coding: utf-8 -*-

import resources

class Terrain(object):
    ascii_repr = ' '
    resource_types = {}

    def __str__(self):
        return self.ascii_repr

    def has_resource(self, res_type):
        return self.resource_types.get(res_type, 0)

class Sea(Terrain):
    ascii_repr = '~'

class Plain(Terrain):
    ascii_repr = '#'
    resource_types = {
        resources.Earth: 30,
        }

TERRAINS_HASH = {
    '~' : Sea,
    '#' : Plain,
    }
