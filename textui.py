# -*- coding: utf-8 -*-

import urwid
import sys

DEBUG_EVENTS = False

class UiMsgDispatcher(object):

    def __init__(self):
        self.listeners = []

    def register(self, listener):
        self.listeners.append(listener)

    def unregister(self, listener):
        if listener in self.listeners:
            self.listeners.remove(listener)

    def publish(self, emitter, message):
        for listener in self.listeners:
            listener.receiveMessage(emitter, message)

class MapWidget(urwid.WidgetWrap):

    def __init__(self, map, uimd = None):
        self.map = map
        self.uimd = uimd
        self.selection = (None, None)
        self.display_widget = urwid.Text(self.getText())
        super(MapWidget, self).__init__(self.display_widget)

    def getText(self):
        result = []
        w, h = self.map.getSize()
        sx, sy = self.selection
        for y in range(h):
            line = []
            for x in range(w):
                c = self.map.get_cell(x, y)
                t = c.terrain._name
                if x == sx and y == sy:
                    t = "selected"
                line.append((t, str(c.getBuilding())))
            result.extend(line)
            result.append("\n")
        # Remove the last \n
        result = result[:-1]
        return result

    def selectable(self):
        return True

    def keypress(self, size, key):
        if DEBUG_EVENTS:
            sys.stderr.write("UH kp %s %s\n" % (size, key))
            sys.stderr.flush()
        return key

    def mouse_event(self, size, event, button, x, y, focus):
        self.selection = x,y
        w, h = self.map.getSize()
        if x >= w or x < 0 or y >= h or y < 0:
            return
        self.display_widget.set_text(self.getText())
        cell = self.map.get_cell(x,y)
        if self.uimd and event == 'mouse press':
            self.uimd.publish(self, ["item selected on map", cell])
        if DEBUG_EVENTS:
            sys.stderr.write("UH me %s\n" % ([size, event, button, x, y, focus],))
            sys.stderr.flush()

class InformationsTextWidget(urwid.Text):

    def receiveMessage(self, emitter, message):
        if message[0] == "item selected on map":
            self.set_text(message[1].getInfo())

class TextUI(object):

    palette = [
        # Name          fg      bg  settingsmono fg             bg
        ('sea',         '',     '',     '',     '#abd',     '#266'),
        ('plain',       '',     '',     '',     '#c83',     '#755'),
        ('selected',    '',     '',     '',     '#dff',     'g31' ),
        ]

    def __init__(self, map):
        uimd = UiMsgDispatcher()
        self.map = MapWidget(map, uimd)
        title = urwid.Text("Brain in the box")
        self.menu = self.generateMenu()
        self.submenu = None
        self.informations = InformationsTextWidget("info here")
        uimd.register(self.informations)
        uimd.register(self)
        pile = urwid.Pile([title, self.menu, self.informations])
        cols = urwid.Columns([self.map, pile])
        fill = urwid.Filler(cols)
        self.ml = urwid.MainLoop(fill, self.palette, unhandled_input = self.unhandled_input)
        self.ml.screen.set_terminal_properties(colors=256)

    def run(self):
        self.ml.run()

    def generateMenu(self):
        menuitems = []
        menuitems.append(urwid.Button("Game"))
        menuitems.append(urwid.Button("Stock"))
        menuitems.append(urwid.Button("Help"))
        return urwid.Pile([urwid.Columns(menuitems)])

    def unhandled_input(self, input):
        if DEBUG_EVENTS:
            sys.stderr.write("UH input %s\n" % (input,))
            sys.stderr.flush()
        if input in ('q', 'Q'):
            raise urwid.ExitMainLoop()
        #txt.set_text(repr(input))

    def setSubMenu(self, widget):
        if self.submenu is None and widget is not None:
            self.submenu = widget
            self.menu.widget_list.append(widget)
            return
        if self.submenu is not None and widget is None:
            self.menu.widget_list.pop(-1)
            self.submenu = None
            return
        if self.submenu is not None and widget is not None:
            if self.submenu == widget:
                return
            self.setSubMenu(None)
            self.setSubMenu(widget)
    def receiveMessage(self, emitter, message):
        if message[0] == "item selected on map":
            cell = message[1]
            self.setSubMenu(urwid.Button("clic"))

