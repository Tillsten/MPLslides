# -*- coding: utf-8 -*-
"""
Contains the slide classes
"""
import matplotlib.pyplot as plt
import collections
from styles import *
import content
from content import add_text

class Slide(object):
    "Basic slide object"
    background_funcs = []
    last_slide = None
    autoregister_pres = None

    def __init__(self, name=''):
        self.content = []
        if Slide.autoregister_pres is not None:
            Slide.autoregister_pres.add_slide(self)
        content.last_slide = self
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
        self.add_content(add_text(self.slide_title, layout['title.pos'],
                                  big_title_style, va='bottom', ha='left',
                                  linewidth=layout["title.width"]))
        if self.slide_subtitle is not None:
            self.add_content(add_text(self.slide_subtitle, layout['title.pos'],
                                   sub_title_style, va='top', ha='left',
                                   linewidth=layout["subtitle.width"]))


class TitleSlide(Slide):
    "Title slide"

    def __init__(self, title, subtitle=None, name=''):

        super(TitleSlide, self).__init__(name)
        self.title_text = title
        self.subtitle_text = subtitle
        self.add_content(add_text(title, layout['bigtitle.pos'],
                                  big_title_style, linewidth=35))
        if subtitle is not None:
            self.add_content(add_text(subtitle, layout['bigtitle.pos'],
                                      sub_title_style, linewidth=50))





