# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 08:48:23 2021

@author: reis-
"""
from cards import Cards

user_input = '0'

def count (cards):
    points = []
    for card in cards:
        if(card[0] in "JQK" or card[0] == '1'):
             points.append(10)
        elif (card[0] in "123456789"):
            points.append(int(card[0]))
    for card in cards:
        if(card[0] == "A"):
            if sum(points) <= 10:
                points.append(11)
            else:
                points.append(1)
    
    return sum(points)

def getWinner (player, dealer):
    print(dealer)
    print(count(dealer))
    print(player)
    print(count(player))
    if count(player) == 21 or count(dealer) > 21:
        print("Você venceu!")
    elif count(dealer) == 21 or count(player) > 21:
        print("Lamento, você perdeu!")
    elif count(player) > count(dealer):
        print("Você venceu!")
    else:
        print("Lamento, você perdeu!")

while True:
    
    if user_input == '0':
        cards = Cards(2, 2)
        cards.shuffle()
        dic_cards = cards.deal()
        dealer = dic_cards['hands'][0]
        player_1 = dic_cards['hands'][1]
        hill = dic_cards['hill']
    
    if count(dealer) <= 10:
        new_card = hill.pop()
        dealer.append(new_card)
    print(dealer[0])
    print(player_1)
    
    print("Escolha sua jogada:")
    print("0: abandonar rodada")
    print("1: mostrar mão")
    print("2: pedir carta")
    print("4: sair")
    user_input = input('>_ ')
    if (user_input == "0"):
        continue
    elif (user_input == "1"):
        getWinner(player_1, dealer)
        user_input = '0'
    elif(user_input == "2"):
        new_card = hill.pop()
        player_1.append(new_card)
    else:
        break





