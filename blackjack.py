'Блэкджек (двадцать одно)'

import random, sys
from typing import Optional

DIAMONDS: str = chr(9829)
HEARTS: str  = chr(9830)
SPADES: str  = chr (9824)
CLUBS: str  = chr(9827)
BACKSIDE: str = 'backside'

def main():
    print('''Блэкджек
    
    Правила:
    Постарайтесь приблизиться как можно ближе к 21, не допустив "перебора". Короли, Дамы и Валеты стоят 10 очков. Тузы стоят 1 или 11 очков. Карты со 2 по 10 стоят своего номинала. Нажмите, "е" чтобы взять еще одну карту. нажмите "х", чтобы перестать брать карты. В своей первой игре вы можете удвоить ставку (нажмите "2"), чтобы увеличить ее, но должны взять еще одну карту, прежде чем закочить. В случае ничьей ставка возвращается игроку. Дилер перестает брать карты достигнув 17.''')

    money: int = 5000



def getBet(maxBet: int, input=None) -> Optional[int]:
    bet = input
    if input is None:
        bet = input('> ')
    if 0 < bet <= maxBet:
        return bet
    else:
        print('Bad bet!')


def getDeck() -> 'list[tuple]':
    deck = []
    for s in (DIAMONDS, HEARTS, SPADES, CLUBS):
        for n in range(2, 11):
            deck.append((str(n), s))
        for c in ('J', 'Q', 'K', 'A'):
            deck.append((c, s))
    return deck


def displayHands(playerHand: 'list[tuple]', dealerHand: 'list[tuple]', showDealerHand: bool) -> None:
    pass


def getHandValue(cards: 'list[tuple]') -> int:
    val = 0
    for i in cards:
        for c in i[0]:
            if c == 'J' or c == 'Q' or c == 'K':
                val += 10
            elif c == 'A':
                val += 1
            else:
                val += int(c)
    return val
            

def displayCards(cards: 'list[tuple]') -> None:
    pass


def getMove(playerHand: 'list[tuple]', money: int) -> str:
    pass


if __name__ == '__main__':
    main()