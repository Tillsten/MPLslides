# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:26:43 2015

@author: Tillsten
"""
import matplotlib.pyplot as plt
from cascadict import CascaDict



plt.rcParams['font.family'] = 'Sans'
plt.rcParams['toolbar'] = 'None'


figure_settings = dict(pixel_size = (1280, 1024),
                       dpi = 120.,
                       zoom = 0.5,
                       color = (0.1, 0.1, 0.1))

ENUM_CHAR = u'■'

text_style = CascaDict()
text_style.update({
  'fontsize': 24,
  'color': 'w',
})

big_title_style = text_style.cascade()
big_title_style.update({
  'fontsize': 54,
  'fontweight': 'bold',
  'ha': 'center',
  'va': 'bottom'})

sub_title_style = text_style.cascade()
sub_title_style.update({
  'fontsize': 30,
  'fontweight': 'normal',
  'ha': 'center',
  'va': 'top'})


enum_style = text_style.cascade()
enum_style.update({
  'fontsize': 30,
  'fontweight': 'normal',
  'ha': 'left',
  'va': 'top',
  })

enum_char_style = {
  'fontsize': enum_style['fontsize']/2-2,
  'fontweight': 'normal',
  'fontname': 'StixGeneral',
  'color': enum_style['color'],
  'ha': 'left',
  'va': 'top',
  }

layout = {
  'title.pos': (0.05, 0.85),
  'title.width': 35,
  'subtitle.width': 40,
  'bigtitle.pos': (0.5, 0.5),
  'content.top': 0.78,
  'content.bottom': 0.05,
  'content.right': 0.9,
  'content.left': 0.1,
  'content.hcenter': 0.5,
  'content.vcenter': 0.75/2.,
  'enum.offset': (0.01),
  'enum.y_adv': enum_char_style['fontsize']*0.95,
  'enum.indent': enum_char_style['fontsize']*4,
  'enum.linewidth': 21

  }
