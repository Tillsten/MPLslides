# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 21:21:40 2015

@author: Tillsten
"""

from mplslides.content import enumerated_text, add_image
from mplslides.presentation import Presentation
from mplslides.slides import TitleSlide, NormalSlide
import matplotlib.pyplot as plt

pres = Presentation()
s = TitleSlide("Hello", "World")
pres.add_slide(s)

s = NormalSlide('Hello World!', 'Second Page')
txt = enumerated_text(['Foo', 'Bar', '123'], (0.1, 0.75))
img = add_image('mplslides.png', (0.05,0.05), zoom=0.5)
s.add_content([txt, img])
pres.add_slide(s)

plt.show()