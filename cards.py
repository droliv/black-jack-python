# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 07:34:10 2021

@author: reis-
"""


import random

class Cards(object):
    def __init__(self, qt_hand, qt_players):
        self.suits = ["espadas", "coração", "paus", "copas"]
        self.ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.qt_hand = qt_hand
        self.qt_players = qt_players

        
    def shuffle(self):
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(rank + " de " + suit)
                
        random.shuffle(self.cards)
        
    def deal(self):
        self.hands = []
        for p in range(1, self.qt_players + 1):
            self.hand = []
            for i in range(1, self.qt_hand + 1):
                self.hand.append(self.cards.pop())
            self.hands.append(self.hand)
  
        return {'hands': self.hands, 'hill': self.cards}
    