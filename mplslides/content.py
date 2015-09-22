# -*- coding: utf-8 -*-
from __future__ import print_function
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

from styles import *

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

def renderer():
    return plt.gcf().canvas.get_renderer()

def enumerated_text(txt_list, pos, intend=50, **kwargs):
    "Add an enumerated text to slide."
    def f(slide):
        fig, ax = slide.fig, slide.def_ax
        x0, cur_y = pos
        tr = ax.transAxes.inverted()
        xi, yi  = tr.transform_point([intend, layout['enum.y_adv']])
        for txt in txt_list:
            t = ax.text(x0 + xi, cur_y, txt, enum_style,
                        transform=ax.transAxes,  **kwargs)

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
        ob = MyOffsetImage(image, zoom=zoom)
        xalign = dict(left=0, center=0.5, right=1)
        yalign = dict(bottom=0, center=0.5, right=1)
        a, b = xalign[ha], yalign[va]
        ab = AnnotationBbox(ob, pos, frameon=0, pad=0.0, box_alignment=(a, b))
        ax.add_artist(ab)
    return f

    
#__all__ = [add_text, add_image, enumerated_text]
