# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np
from matplotlib.offsetbox import OffsetImage

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
        ob = OffsetImage(image, zoom=zoom, dpi_cor=False)
        w, h, x, d =  ob.get_extent(renderer())
        tw, th = fig.get_size_inches()*fig.dpi

        if transform is None:
            trans = fig.transFigure
        else:
            trans = transform
        pix_pos = trans.transform(pos)

        if ha == 'right':
            x_pos = pix_pos[0] - w
        elif ha == 'center':
            x_pos = pix_pos[0] - w/2.
        else:
            x_pos = pix_pos[0]

        if va == 'top':
            y_pos = pix_pos[1] - h
        elif va == 'center':
            y_pos = pix_pos[1] - h/2.
        else:
            y_pos = pix_pos[1]

        ob.set_offset([x_pos, y_pos])
        fig.artists.append(ob)
    return f

#__all__ = [add_text, add_image, enumerated_text]
