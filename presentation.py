# -*- coding: utf-8 -*-
"""
Contains the presentation class.
"""
from styles import *
import matplotlib.pyplot as plt


class Presentation(object):
    """
    Prensentation class containg the the slides.
    Also handles the figure.
    """
    def __init__(self):
        
        self.background = []
        self.slides = []
        self.current_slide = 0
        self.fig = plt.figure(figsize=SIZE_INCH, facecolor=BACKGROUND,
                              dpi=DPI)
        self.fig.show()
        self.fig.canvas.mpl_connect('resize_event', lambda x: self.draw())
        self.fig.canvas.mpl_connect('key_press_event', self.next_slide)
    
    def add_slide(self, slide):
        self.slides.append(slide)

    def next_slide(self, event):        
        if event.key == 'right':
            self.current_slide = (self.current_slide + 1)%len(self.slides)
            self.draw()
        if event.key == 'left':
            self.current_slide = (self.current_slide - 1)%len(self.slides)
            self.draw()
        
    def draw(self):        
        if len(self.slides) > 0:
            slide = self.slides[self.current_slide]            
            slide.fig = self.fig
            slide.background = self.background
            slide.draw()
            self.fig.canvas.draw()
            
    def to_pdf(self):
        from matplotlib.backends.backend_pdf import PdfPages
        pdf_pages = PdfPages('mplslides.pdf')
        tmp = self.current_slide
        for i, s in enumerate(self.slides):
            self.current_slide = i
            self.draw()
            pdf_pages.savefig(self.fig)        
        pdf_pages.close()
        self.current_slide = tmp
        self.draw()


if __name__ == '__main__':
    pass