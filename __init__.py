# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage
from styles import *
from slides import *

PIXEL_SIZE = (1280, 1024)
DPI = 96.
ZOOM = 0.5
SIZE_INCH = PIXEL_SIZE[0]/DPI, PIXEL_SIZE[1]/DPI
BACKGROUND = 'white'

plt.rcParams['font.family'] = 'Myriad Pro'
plt.rcParams['toolbar'] = 'None'
plt.rcParams['savefig.dpi'] =DPI
plt.close('all')


def enumerated_text(txt_list, pos, intend=10):
    def f(slide):
        fig, ax = slide.fig, slide.def_ax
        x0, y0 = pos
        cur_y = y0
        xi, yi  = ax.transAxes.inverted().transform_point([intend, 50])
        for txt in txt_list:
            ax.text(0.2 + xi, cur_y, txt, enum_style, ha='left')
            cur_y += yi
    return f


def add_image(img_path, pos, zoom=1):
    def f(slide):
        fig, ax = slide.fig, slide.def_ax
        image = plt.imread(img_path)
        w, h = image.shape[:2]
        ob = OffsetImage(image, zoom=zoom, dpi_cor=False)
        w, h, x, d =  ob.get_extent(renderer)
        tw, th = fig.get_size_inches()*fig.dpi
        ob.set_offset([tw-w-30, th-h-30])
        fig.artists.append(ob)
    return f

Slide.background_funcs.append(add_image('logo.png', pos=[0.9, 0.9], zoom=0.4))
a = ['Hallo leute', 'Wixxer', 'Doppel\nArsch']

#t = TitleSlide('The primary photoreaction of\n channelrhodopsin I',
#               'Studied by femtosecond VIS-pump-VIS-probe\n and -IR-probe spectroscopy')

s = NormalSlide("Channelrhodopsin")
s.content.append(enumerated_text(a, (0.5, 0.5)))
s.draw()
plt.show()