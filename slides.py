# -*- coding: utf-8 -*-
"""
Contains the slide classes
"""
import matplotlib.pyplot as plt
from styles import *

PIXEL_SIZE = (1280, 1024)
DPI = 96.
ZOOM = 0.5
SIZE_INCH = PIXEL_SIZE[0]/DPI, PIXEL_SIZE[1]/DPI
BACKGROUND = 'white'

def renderer():
    plt.gcf().canvas.renderer


class Slide(object):
    "Basic slide object"

    background_funcs = []

    def __init__(self, name=''):
        self.fig = plt.figure(figsize=SIZE_INCH, facecolor=BACKGROUND,
                              dpi=DPI)

        #self.fig.canvas.mpl_connect('resize_event', lambda x: self.draw())
        self.content = []

    def draw_background(self):
        for f in self.background_funcs:
            f(self)

    def draw_foreground(self):
        for f in self.content:
            f(self)

    def draw(self):
        self.fig.clear()
        self.def_ax = self.fig.add_axes([0, 0, 1, 1])
        self.def_ax.set_axis_off()
        self.draw_background()
        self.draw_foreground()


class NormalSlide(Slide):
    "Basic content slide with title"

    def __init__(self, slide_title, name=''):
        super(NormalSlide, self).__init__(name=name)
        self.slide_title = slide_title
        self.left_content = []

    def draw_foreground(self):
        super(NormalSlide, self).draw_foreground()
        self.title = self.fig.text(0.04, 0.8, self.slide_title,
                                   big_title_style, va='bottom', ha='left')


class TitleSlide(Slide):
    "Title slide"

    def __init__(self, title, subtitle=None, name=''):

        super(TitleSlide, self).__init__(name)
        self.title_text = title
        self.subtitle_text = subtitle

    def draw_foreground(self):

        self.title = self.fig.text(0.5, 0.5, self.title_text, big_title_style,
                                   va='bottom')
        if self.subtitle_text is not None:
            self.sub_title = self.fig.text(0.5, 0.5, self.subtitle_text,
                                           sub_title_style)

