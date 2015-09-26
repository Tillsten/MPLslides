# -*- coding: utf-8 -*-
from __future__ import print_function
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import textwrap
from styles import *

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

autoadd = True
last_slide = None

def renderer():
    return plt.gcf().canvas.get_renderer()

def autoadd(func):
    @wraps(func)
    def f(*args, **kwargs):
        out = func(*args, **kwargs)
        if autoadd and last_slide:
            last_slide.add_content(out)
        return out
    return f

@autoadd
def enumerated_text(txt_list, pos, **kwargs):
    "Add an enumerated text to slide."
    linewidth = kwargs.pop('linewidth', layout['enum.linewidth'])
    def f(slide):
        fig, ax = slide.fig, slide.def_ax
        if isinstance(pos, str):
            pass
        else:
            x0, cur_y = pos
        tr = ax.transAxes.inverted()
        xi, yi = tr.transform_point([layout['enum.indent'],
                                      layout['enum.y_adv']])
        for txt in txt_list:
            if isinstance(txt, str):
                t = ax.text(x0 + xi, cur_y, textwrap.fill(txt, width=linewidth),
                            enum_style, transform=ax.transAxes, **kwargs)
                t_symbol = ax.text(x0, cur_y-layout['enum.offset'], ENUM_CHAR,
                                   enum_char_style, transform=ax.transAxes)
            else:
                my_style = enum_style.cascade(parse_format_str(txt[1]))
                t = ax.text(x0, cur_y, txt[0], my_style,
                            transform=ax.transAxes,  **kwargs)
            t_size_pixel = t.get_window_extent(renderer())
            t_size = ax.transAxes.inverted().transform_bbox(t_size_pixel)

            cur_y = cur_y - t_size.height - yi

    return f

@autoadd
def add_text(txt, pos, style=text_style, **kwargs):
    "Add text to the slide"
    linewidth = kwargs.pop('linewidth', None)
    if linewidth:
        txt = textwrap.fill(txt, width=linewidth)
    def f(slide):
        fig, ax = slide.fig, slide.def_ax
        ax.text(pos[0], pos[1], txt,
                style, **kwargs)
    return f

@autoadd
def add_image(img_path, pos, va='bottom', ha='left', transform=None, zoom=1):
    "Add image to the slide"
    def f(slide):
        fig, ax = slide.fig, slide.def_ax
        image = plt.imread(img_path)
        w, h = image.shape[:2]
        ob = MyOffsetImage(image, zoom=zoom)
        xalign = dict(left=0, center=0.5, right=1)
        yalign = dict(bottom=0, center=0.5, top=1)
        a, b = xalign[ha], yalign[va]
        ab = AnnotationBbox(ob, pos, frameon=0, pad=0.0, box_alignment=(a, b))
        ax.add_artist(ab)
    return f

def parse_format_str(s):
    """Parse a str to fontproperties which will be returned as a dict.

    b is bold, i is italic, s is semibold, a number will be used
    as fontsize.
    """
    out = {}
    if s.count("b"):
        out['fontweight'] = 'bold'
    if s.count("s"):
        out['fontweight'] = 'semibold'
    if s.count("i"):
        out['fontstyle'] = 'italic'
    number = "".join([c for c in s if c in '1234567890'])
    if number != '':
        out['fontsize'] = int(number)
    return out

#__all__ = [add_text, add_image, enumerated_text]
