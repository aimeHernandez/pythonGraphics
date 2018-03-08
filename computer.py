from graphics import *

class Computer(object):
    def __init__(self, x, y, color, win):
        self.x = x
        self.y = y
        self.color = color
        self.drawComp(x, y, color, win) # place points and color here

    def drawComp(self, x, y, color, win):
        comp = Rectangle(Point(self.x, self.y), Point(self.x+100, self.y+200))
        comp.setFill(self.color)
        comp.draw(win)

class Desktop(Computer):
    def __init__(self, x, y, color, win):
        super(Desktop, self).__init__(x, y, color, win)
        self.monitor = Monitor(x, y, win) #place points here

    def drawKeyBoard(self, color, win):
        rec = Rectangle(Point(self.x+50, self.y+100), Point(self.x+50, self.y+100) )
        rec.setFill(self.color)
        rec.draw(win)

class Laptop(Computer):
    def __init__(self, x, y, color, win):
        super(Laptop, self).__init__(x, y, color, win)
        self.monitor = Monitor(x, y, win) #place points and color
        self.drawBottom(color, win) #place color

    def drawBottom(self, color, win):
        bottom = Rectangle(Point(self.x, self.y+100), Point(self.x, self.y+100))
        bottom.setFill(self.color)
        bottom.draw(win)

class Monitor(object):
    def __init__(self, x, y, win):
        self.x = x
        self.y = y
        self.drawMonitor(x, y, win) #place points

    def drawMonitor(self, x, y, win):
        monitor = Rectangle(Point(self.x, self.y), Point(self.x+200, self.y+100))
        monitor.draw(win)