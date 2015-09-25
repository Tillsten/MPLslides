# -*- coding: utf-8 -*-
"""
Contains the slide classes
"""
import matplotlib.pyplot as plt
import collections
from styles import *

class Slide(object):
    "Basic slide object"
    background_funcs = []
    autoregister_pres = None

    def __init__(self, name=''):
        self.content = []
        if Slide.autoregister_pres is not None:
            Slide.autoregister_pres.add_slide(self)

    def add_content(self, c):
        if not isinstance(c, collections.Iterable):
            c = [c]
        self.content+= c

    def draw_background(self):
        for f in self.background:
            f(self)

    def draw_foreground(self):
        for f in self.content:
            f(self)

    def draw(self):
        if not hasattr(self, 'fig'):
            fsettings = dict(figsize=SIZE_INCH, facecolor=BACKGROUND, dpi=DPI)
            self.fig = plt.figure(**fsettings)
        self.fig.clear()
        self.def_ax = self.fig.add_axes([0, 0, 1, 1])
        self.def_ax.set_axis_off()
        self.draw_background()
        self.draw_foreground()


class NormalSlide(Slide):
    "Basic content slide with title and optional subtitle"

    def __init__(self, slide_title, slide_subtitle=None, name=''):
        super(NormalSlide, self).__init__(name=name)
        self.slide_title = slide_title
        self.slide_subtitle = slide_subtitle
        self.left_content = []

    def draw_foreground(self):
        super(NormalSlide, self).draw_foreground()
        xpos, ypos = layout['title.pos']
        self.title = self.fig.text(xpos, ypos, self.slide_title,
                                   big_title_style, va='bottom', ha='left')
        if self.slide_subtitle is not None:
                    self.title = self.fig.text(xpos, ypos, self.slide_subtitle,
                                   sub_title_style, va='top', ha='left')




class TitleSlide(Slide):
    "Title slide"

    def __init__(self, title, subtitle=None, name=''):

        super(TitleSlide, self).__init__(name)
        self.title_text = title
        self.subtitle_text = subtitle

    def draw_foreground(self):
        super(TitleSlide, self).draw_foreground()
        x, y = layout['bigtitle.pos']
        self.title = self.fig.text(x, y, self.title_text, big_title_style,
                                   va='bottom')
        if self.subtitle_text is not None:
            self.sub_title = self.fig.text(x, y, self.subtitle_text,
                                           sub_title_style)

