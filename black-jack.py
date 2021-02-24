# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 08:48:23 2021

@author: reis-
"""


from cards import Cards

cards = Cards(2, 3)

cards.shuffle()

print(cards.deal())

