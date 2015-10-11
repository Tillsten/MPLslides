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
from mplslides.styles import layout as l
from example_plots import *

presentation = Presentation()
Slide.autoregister_pres = presentation
# Background is drawn on every slide
presentation.background.append(image('mplslides.png', ha='right',
                                 pos=(0.98, 0.02), zoom=0.2))

slide = TitleSlide('MPLslides 0.1', 'Making presentations in matplotlib')
t = text("Press left and right to navigate slides", (0.05, 0.05),
             va='bottom')
slide.add_content(t)

slide = NormalSlide("Slides with Matplotlib?", 'Why would you do that?')
a = ['For fun!',
     'Problematic alternatives.',
     'All my figures are done with matplotlib anyways.']
slide.add_content(listed_text(a, (0.55, 0.7)))
slide.add_content(bar_plot)

slide = NormalSlide("Features", 'Almost none!')
a = ['Pictures!',
     'Axes!',
     'Enumerated text!',
     '...which was harder than\nits sounds.',
     r'$e^{\pm i\theta}=\cos\theta\pm i\sin\theta$',
     'PDF export!']
slide.add_content(listed_text(a, (0.5, 0.7), linewidth=80))
slide.add_content(sine_plot)

title = 'Code of this slide'
subtitle = 'Sorry, no code formatting!'
slide = NormalSlide(title, subtitle)
txt = """
from content import text
from presentation import Presentation
from slides import NormalSlide

pres = Presentation()
presentation.background.append(image('mpl_slide.png', ha='right',
                                 pos=(0.98, 0.02), zoom=0.4))
...
title = 'Code of this slide'
subtitle = 'Sorry, no code formatting!'
slide = NormalSlide(title, subtitle)
txt = ...the shown txt...
fontprops = dict(va='top', fontname='monospace', fontsize=15)
code_txt = text(txt, (0.1, 0.7), **fontprops)
slide.add_content(code_txt)
presentation.add_slide(s)
"""
fontprops = dict(va='top', fontname='Consolas', fontsize=15)
code_txt = text(txt, (0.1, 0.7), **fontprops)
slide.add_content(code_txt)

slide = NormalSlide('Animated Plots', 'Only in interactive Backends')
slide.add_content(animated_plot())

slide = NormalSlide('What sucks?', 'And why?')
t = ['Matplotlibs typesetting is very basic.',
     'Manual newlines.',
     'No <b>, <i> or other inline formatting.',
     'Layout options are still very basic.',
     'But should be easily extensible.']
slide.add_content(listed_text(t, (l['content.left'], l['content.top']),
                                  linewidth=50))


slide = NormalSlide('What can be done?', 'Probably not by me')
t = ['One could directly use Latex for text processing.',
     'Thats cheating!\nAlso why not use Beamer than...',
     'Make a fancier text class, with support for simple formatting.',
     'AUTOMATIC LINE BREAKS!',
     'Appearing and disapperaing elements should also be quite doable.',
     'More content functions, smarter layout.']

txt = listed_text(t, (l['content.left'], l['content.top']), fontsize=30,
                      linewidth=40)
slide.add_content(txt)

slide = TitleSlide('Personal conclusion', 'For the amout of code, it is quite awesome!')
plt.show()
presentation.to_pdf('..\\example.pdf')