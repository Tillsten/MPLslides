# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:45:43 2015

@author: Tillsten
"""
from presentation import *
from content import *
from slides import *

import matplotlib.pyplot as plt
plt.close('all')

from styles import layout as l

presentation = Presentation()
# Background is drawn on every slide
presentation.background.append(add_image('mplslides.png', ha='right',
                                 pos=(0.98, 0.02), zoom=0.4))

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
def bar_plot(slide):
    with plt.style.context('dark_background'):
        rect = [l['content.left'], l['content.bottom']+0.1, 0.35, 0.5]
        ax = slide.fig.add_axes(rect)
        ax.patch.set_color('None')
        ax.bar([0, 1], [7, 13], fc='w', ec='w')
        fd = dict( ha='center', fontsize=16, color='k', va='top')
        ax.text(0.4, 7-0.1, "Apple", **fd)
        ax.text(1.4, 13-0.1, "Organges", **fd)
        ax.set_ylim(0, 15)
        ax.set_ylabel('Magnesium [mg / 100 g]', fontsize=18)
        ax.grid(1, axis='y', linestyle='-', alpha=0.5)
        for i in ['top', 'right', 'bottom']:
            ax.spines[i].set_visible(0)
            d = {i: False}
            ax.tick_params(**d)
        ax.xaxis.set_ticks([])
        ax.margins(x=0.1)
slide.add_content(bar_plot)
presentation.add_slide(slide)



slide = NormalSlide("Features", 'Almost none!')
a = ['Pictures!',
     'Axes!',
     'Enumerated text!',
     '..which was harder\nthan its sounds.',
     'PDF export!']
slide.add_content(enumerated_text(a, (0.5, 0.7)))
def sine_plot(slide):
    x = np.linspace(0, 10)
    with plt.style.context('dark_background'):
        ax = slide.fig.add_axes([0.07, 0.45, 0.4, 0.3])
        ax.plot(x, np.sin(x), lw=2)
        ax.set(xlabel='Time', ylabel='Amp')

        ax2 = slide.fig.add_axes([0.07, 0.07, 0.4, 0.3])
        def fcn(x, y):
            return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
        n = 20
        x = np.linspace(-3, 3, 4 * n)
        y = np.linspace(-3, 3, 3 * n)
        X, Y = np.meshgrid(x, y)
        ax2.contourf(fcn(X, Y), 20, cmap='bone', aspect='auto')
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



slide = NormalSlide('What sucks?', 'And why?')
t = ['Matplotlibs typesetting is very basic.',
     'Manual newlines.',
     'No <b>, <i> or other inline formatting.',
     'Layout options are still very basic.',
     'But should be easily extensible.']
slide.add_content(enumerated_text(t, (l['content.left'], l['content.top'])))
presentation.add_slide(slide)


#plt.show()
presentation.to_pdf('example2.pdf')