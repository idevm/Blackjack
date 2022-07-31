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



def getBet(maxBet: int) -> Optional[int]:
    pass

def getDeck() -> 'list[tuple]':
    pass

def displayHands(playerHand: 'list[tuple]', dealerHand: 'list[tuple]', showDealerHand: bool) -> None:
    pass

def getHandValue(cards: 'list[tuple]') -> int:
    pass

def displayCards(cards: 'list[tuple]') -> None:
    pass

def getMove(playerHand: 'list[tuple]', money: int) -> str:
    pass

if __name__ == '__main__':
    main()