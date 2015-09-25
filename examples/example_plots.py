# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:16:32 2018

@author: Tillsten
"""

import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
from mplslides.styles import layout as l

def plot_income(ax):
    census = np.loadtxt('census.dat')
#Year Households, Median-current$ Median-2011$  Mean-current$ Mean-2011$
    with plt.style.context('dark_background'):
        ax.locator_params(nbins=5)
        l1, = ax.plot(census[:, 0], census[:, 3]/1000, lw=3)
        l2, = ax.plot(census[:, 0], census[:, 5]/1000, lw=3)
        ax.set_ylabel('1000$', fontsize=15)
        ax.set_xlabel('Year', fontsize=15)
        twax = ax.twinx()
        l3, = twax.plot(census[:, 0], census[:, 3]/census[:, 5], lw=3, color='r')
        twax.set_ylabel("Ratio Median/Mean", fontsize=15)
        ax.text(2001, 68, 'Mean', fontsize=18, color=l2.get_color())
        ax.text(2001, 55, 'Median', fontsize=18, color=l1.get_color())
        ax.text(2002, 41, 'Ratio', fontsize=18, color=l3.get_color())
        twax.locator_params(nbins=4)
        ax.autoscale(1, 'x', 1)

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

def sine_plot(slide):
    x = np.linspace(0, 10)
    with plt.style.context('dark_background'):
        ax = slide.fig.add_axes([0.07, 0.45, 0.33, 0.3])
        plot_income(ax)
        ax.set_title('Household income USA')
        ax2 = slide.fig.add_axes([0.07, 0.07, 0.33, 0.3])
        def fcn(x, y):
            return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
        n = 20
        x = np.linspace(-3, 3, 4 * n)
        y = np.linspace(-3, 3, 3 * n)
        X, Y = np.meshgrid(x, y)
        ax2.contourf(fcn(X, Y), 20, cmap='bone', aspect='auto')


def animated_plot():
    def f(slide):
        fig, ax = slide.fig, slide.def_ax
        with plt.style.context('dark_background'):
            ax = fig.add_axes([0.1, 0.15, 0.8, 0.6])
            x = np.linspace(0, 50, 500)
            l, = ax.plot([], [], animated=True)
        interval = 1000/26
        ax.set_xlim(0, 50)
        ax.set_ylim(-1, 1)
        fig.canvas.draw()
        slide.back = fig.canvas.copy_from_bbox(ax.bbox)
        #No nonlocal in py2
        class Nonlocal:
            t = 0

        def update():
            Nonlocal.t = Nonlocal.t + interval
            t = Nonlocal.t
            y = .5*np.sin(x + t/100.) + .5*np.sin(x + 1.05*t/100.)
            l.set_data(x, y)
            fig.canvas.restore_region(slide.back)
            ax.draw_artist(l)
            fig.canvas.update()

        slide.timer = fig.canvas.new_timer(interval=interval)
        slide.timer.add_callback(update)
        slide.timer.start()
    return f
