# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

from styles import *

def renderer():
    return plt.gcf().canvas.get_renderer()

def enumerated_text(txt_list, pos, intend=50):
    "Add an enumerated text to slide."
    def f(slide):
        fig, ax = slide.fig, slide.def_ax
        x0, cur_y = pos
        tr = ax.transAxes.inverted()
        xi, yi  = tr.transform_point([intend, layout['enum.y_adv']])
        for txt in txt_list:
            t = ax.text(x0 + xi, cur_y, txt, enum_style,
                        transform=ax.transAxes)

            t_symbol = ax.text(x0, cur_y-layout['enum.offset'], ENUM_CHAR,
                               enum_char_style, transform=ax.transAxes)
            t_size_pixel = t.get_window_extent(renderer())
            t_size = ax.transAxes.inverted().transform_bbox(t_size_pixel)
            cur_y = cur_y - t_size.height - yi
    return f

def add_text(txt, pos, **kwargs):
    "Add text to the slide"
    def f(slide):
        fig, ax = slide.fig, slide.def_ax
        ax.text(pos[0], pos[1], txt, text_style, **kwargs)
    return f

def add_image(img_path, pos, va='bottom', ha='left', transform=None, zoom=1):
    "Add image to the slide"
    def f(slide):
        fig, ax = slide.fig, slide.def_ax
        image = plt.imread(img_path)
        w, h = image.shape[:2]


        ob = OffsetImage(image, zoom=zoom)

        xalign = dict(left=0, center=0.5, right=1)
        yalign = dict(bottom=0, center=0.5, right=1)
        a, b = xalign[ha], yalign[va]
        ab = AnnotationBbox(ob, pos, frameon=0, pad=0.0, box_alignment=(a, b))

        ax.add_artist(ab)
    return f

#__all__ = [add_text, add_image, enumerated_text]
