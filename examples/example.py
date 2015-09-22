# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:45:43 2015

@author: Tillsten
"""
import sys
from mplslides.presentation import *
from mplslides.content import *
from mplslides.slides import *
import matplotlib.pyplot as plt

plt.close('all')

from mplslides.styles import layout as l
from example_plots import *

presentation = Presentation()
# Background is drawn on every slide
presentation.background.append(add_image('mplslides.png', ha='right',
                                 pos=(0.98, 0.02), zoom=0.2))


slide = TitleSlide('MPLslides 0.1', 'Making presentations in matplotlib')
t = add_text("Press left and right to navigate slides", (0.05, 0.05),
             va='bottom')
slide.add_content(t)
presentation.add_slide(slide)


slide = NormalSlide("Slides with Matplotlib?", 'Why would you do that?')
a = ['For fun!',
     'Problematic\nalternatives.',
     'All my figures are\ndone with mpl.']
slide.add_content(enumerated_text(a, (0.55, 0.7)))
slide.add_content(bar_plot)
presentation.add_slide(slide)



slide = NormalSlide("Features", 'Almost none!')
a = ['Pictures!',
     'Axes!',
     'Enumerated text!',
     '..which was harder\nthan its sounds.',
     r'$e^{ \pm i\theta } = \cos \theta \pm i\sin \theta$',
     'PDF export!']
slide.add_content(enumerated_text(a, (0.5, 0.7)))
slide.add_content(sine_plot)
presentation.add_slide(slide)



title = 'Code of this slide'
subtitle = 'Sorry, no code formatting!'
slide = NormalSlide(title, subtitle)
txt = """
from content import add_text
from presentation import Presentation
from slides import NormalSlide

pres = Presentation()
presentation.background.append(add_image('mpl_slide.png', ha='right',
                                 pos=(0.98, 0.02), zoom=0.4))
...
title = 'Code of this slide'
subtitle = 'Sorry, no code formatting!'
slide = NormalSlide(title, subtitle)
txt = ...the shown txt...
fontprops = dict(va='top', fontname='monospace', fontsize=15)
code_txt = add_text(txt, (0.1, 0.7), **fontprops)
slide.add_content(code_txt)
presentation.add_slide(s)
"""
fontprops = dict(va='top', fontname='Consolas', fontsize=15)
code_txt = add_text(txt, (0.1, 0.7), **fontprops)
slide.add_content(code_txt)
presentation.add_slide(slide)

slide = NormalSlide('Animated Plots', 'Only in interactive Backends')
slide.add_content(animated_plot())
presentation.add_slide(slide)


slide = NormalSlide('What sucks?', 'And why?')
t = ['Matplotlibs typesetting is very basic.',
     'Manual newlines.',
     'No <b>, <i> or other inline formatting.',
     'Layout options are still very basic.',
     'But should be easily extensible.']
slide.add_content(enumerated_text(t, (l['content.left'], l['content.top'])))
presentation.add_slide(slide)

slide = NormalSlide('What can be done?', 'Probably not by me')
t = ['One could directly use Latex for\ntext processing.',
     'Thats cheating!\nAlso why not use Beamer than...',
     'Make a fancier text class, with\nsupport for simple formatting.',
     'AUTOMATIC LINE BREAKS!',
     'Appearing and disapperaing elements\nshould also be quite doable.',
     'More content functions, smarter layout.']

txt = enumerated_text(t, (l['content.left'], l['content.top']), fontsize=28)
slide.add_content(txt)
presentation.add_slide(slide)

slide = TitleSlide('Personal conclusion', 'For the amout of code, it is quite awesome!')
presentation.add_slide(slide)


plt.show()
presentation.to_pdf('..\\example.pdf')