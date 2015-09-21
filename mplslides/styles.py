# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:26:43 2015

@author: Tillsten
"""
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Sans'
plt.rcParams['toolbar'] = 'None'


PIXEL_SIZE = (1280, 1024)
DPI = 120.
ZOOM = 0.5
SIZE_INCH = PIXEL_SIZE[0]/DPI, PIXEL_SIZE[1]/DPI
BACKGROUND = (0.1, 0.1, 0.1)
plt.rcParams['savefig.dpi'] = DPI

ENUM_CHAR = u'■'

text_style = {
  'fontsize': 24,
  'color': 'w',

}

big_title_style = text_style.copy()
big_title_style.update({
  'fontsize': 54,
  'fontweight': 'bold',
  'ha': 'center',
  'va': 'center'})

sub_title_style = text_style.copy()
sub_title_style.update({
  'fontsize': 30,
  'fontweight': 'normal',
  'ha': 'center',
  'va': 'top'})


enum_style = text_style.copy()
enum_style.update({
  'fontsize': 30,
  'fontweight': 'normal',
  'ha': 'left',
  'va': 'top',
  })

enum_char_style = {
  'fontsize': 15,
  'fontweight': 'normal',
  'fontname': 'StixGeneral',
  'color': enum_style['color'],
  'ha': 'left',
  'va': 'top',
  }

layout = {
  'title.pos': (0.05, 0.85),
  'bigtitle.pos': (0.5, 0.5),
  'content.top': 0.75,
  'content.bottom': 0.05,
  'content.right': 0.9,
  'content.left': 0.1,
  'content.hcenter': 0.5,
  'content.vcenter': 0.75/2.,
  'enum.offset': (0.01),
  'enum.y_adv': 40,

  }