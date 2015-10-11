# -*- coding: utf-8 -*-
from __future__ import print_function
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

from .styles import *
from .utils import DocWrapper
from functools import wraps

class MyOffsetImage(OffsetImage):
    def get_extent(self, renderer):
        if self._dpi_cor:
            dpi_cor = renderer.points_to_pixels(1.)
        else:
            dpi_cor = 1.
        zoom = self.get_zoom() * dpi_cor
        data = self.get_data()
        ny, nx = data.shape[:2]
        w, h = nx * zoom, ny * zoom
        return w, h, 0, 0


autoadd = False
last_slide = None

def renderer():
    return plt.gcf().canvas.get_renderer()


def axify(func, pos):
    def f(slide):
        ax = slide.fig.add_axes(pos)
        func(ax)
    return f



import re, textwrap
def linewrap(text, width=70, **kwargs):
    s = [textwrap.fill(s, width=width) + '\n' for s in text.splitlines()]
    s[-1] = s[-1][:-1]
    return ''.join(s)

def autoadd(func):
    @wraps(func)
    def f(*args, **kwargs):
        auto = kwargs.pop('auto', autoadd)
        from .slides import Slide
        out = func(*args, **kwargs)
        if auto and Slide.last_slide:
            Slide.last_slide.add_content(out)
        return out
    return f


def draw_list_symbol(ax, x, y, number, style):
    ax.text(x, y - layout['enum.offset'], ENUM_CHAR,
            enum_char_style, transform=ax.transAxes)


def draw_list_number(ax, x, y, number, style):
    ax.text(x, y, number, style, transform=ax.transAxes)


@autoadd
def listed_text(txt_list, pos, **kwargs):
    "Add an enumerated text to slide."
    linewidth = kwargs.pop('linewidth', layout['enum.linewidth'])
    enum = kwargs.pop('enumerate', False)

    def f(slide):
        fig, ax = slide.fig, slide.def_ax
        if isinstance(pos, str):
            pass
        else:
            x0, cur_y = pos
        tr = ax.transAxes.inverted()
        xi, yi = tr.transform_point([layout['enum.indent'],
                                     layout['enum.y_adv']])
        for i, txt in enumerate(txt_list):
            if not isinstance(txt, str):
                my_style = enum_style.cascade(parse_format_str(txt[1]))
                txt = txt[0]
            else:
                my_style = enum_style
            aw = my_style.pop('autowrap', True)
            if aw:
                print(txt)
                txt = linewrap(txt, width=linewidth)
            if my_style.pop('enum', True):
                draw_list_symbol(ax, x0, cur_y, i, my_style)
                txi = xi
            else:
                txi = 0
            t = ax.text(x0 + txi, cur_y, txt, my_style, transform=ax.transAxes,  **kwargs)
            t_size_pixel = t.get_window_extent(renderer())
            t_size = ax.transAxes.inverted().transform_bbox(t_size_pixel)
            cur_y = cur_y - t_size.height - yi
    return f


@autoadd
def text(txt, pos, style=text_style, **kwargs):
    "Add text to the slide"
    linewidth = kwargs.pop('linewidth', None)
    if linewidth:
        txt = linewrap(txt, width=linewidth)
    def f(slide):
        fig, ax = slide.fig, slide.def_ax
        ax.text(pos[0], pos[1], txt,
                style, **kwargs)
    return f


@autoadd
def image(img_path, pos, va='bottom', ha='left', transform=None, zoom=1):
    "Add image to the slide"
    def f(slide):
        fig, ax = slide.fig, slide.def_ax
        image = plt.imread(img_path)
        w, h = image.shape[:2]
        ob = MyOffsetImage(image, zoom=zoom, dpi_cor=0)
        xalign = dict(left=0, center=0.5, right=1)
        yalign = dict(bottom=0, center=0.5, top=1)
        a, b = xalign[ha], yalign[va]
        ab = AnnotationBbox(ob, pos, frameon=0, pad=0.0, box_alignment=(a, b))
        ax.add_artist(ab)
    return f


def parse_format_str(s):
    """Parse a str to fontproperties which will be returned as a dict.

    b is bold, i is italic, s is semibold, a number will be used
    as fontsize, aw disables autowrap, e disables the enumaration.
    """
    out = {}
    if s.count("b"):
        out['fontweight'] = 'bold'
    if s.count("aw"):
        out['autowrap'] = False
    if s.count("s"):
        out['fontweight'] = 'semibold'
    if s.count("i"):
        out['fontstyle'] = 'italic'
    if s.count('e'):
        out['enum'] = False
    number = "".join([c for c in s if c in '1234567890'])
    if number != '':
        out['fontsize'] = int(number)
    return out

__all__ = ['text', 'image', 'listed_text', 'axify']
