'Блэкджек (двадцать одно)'

import random, sys
from typing import Optional
from webbrowser import get

DIAMONDS: str = chr(9829)
HEARTS: str  = chr(9830)
SPADES: str  = chr (9824)
CLUBS: str  = chr(9827)
BACKSIDE: str = 'backside'

def main():
    print('''
    Блэкджек
    
    Правила:
    Постарайтесь приблизиться как можно ближе к 21, не допустив "перебора". Короли, Дамы и Валеты стоят 10 очков. Тузы стоят 1 или 11 очков. Карты со 2 по 10 стоят своего номинала. Нажмите, "е" чтобы взять еще одну карту. нажмите "х", чтобы перестать брать карты. В своей первой игре вы можете удвоить ставку (нажмите "2"), чтобы увеличить ее, но должны взять еще одну карту, прежде чем закочить. В случае ничьей ставка возвращается игроку. Дилер перестает брать карты достигнув 17.
    ''')

    money: int = 5000

    while True:
        if money <= 0:
            print('Вы банкрот!\nХорошо, что это были не настоящие деньги!\nСпасибо за игру!')
            sys.exit()
        print('Баланс: ', money)
        bet: int = getBet(money)
        if bet == 0:
            print('Спасибо за игру!')
            sys.exit()
        deck: list[tuple] = getDeck()
        dealerHand: list[tuple] = [deck.pop(), deck.pop()]
        playerHand: list[tuple] = [deck.pop(), deck.pop()]
        print('Ставка: ', bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()
            if getHandValue(playerHand) > 21:
                break
            move: str = getMove(playerHand, money - bet)
            if move == '2':
                additionalBet: int = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f'Ставка выросла до {bet}')
                print(f'Ставка: {bet}')
            if move in ('Е', '2'):
                newCard: tuple[str] = deck.pop()
                rank, suit = newCard
                print(f'Вы взяли {rank} {suit}.')
                playerHand.append(newCard)
                if getHandValue(playerHand) > 21:
                    continue
            if move in ('Х', '2'):
                break
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('Дилер берет еще карту...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
                if getHandValue(dealerHand) > 21:
                    break
                input('Нажмите Enter для продолжения...')
                print('\n\n')
        displayHands(playerHand, dealerHand, True)
        playerValue: int = getHandValue(playerHand)
        dealerValue: int = getHandValue(dealerHand)
        if dealerValue > 21:
            print(f'Дилер проиграл! Вы выиграли ${bet}!')
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('Вы проиграли!')
            money -= bet
        elif playerValue > dealerValue:
            print(f'Вы выиграли ${bet}!')
            money += bet
        elif playerValue == dealerValue:
            print('Ничья, ставка возвращается вам.')
        input('Нажмите Enter для продолжения...')
        print('\n\n')


def getBet(maxBet: int, input=None) -> int:
    while True:
        print(f'Ваша ставка? (1-{maxBet}, или 0 - выход)')
        if  not input:
            inputStr: str = input('> ').upper().strip()
            if not inputStr.isdecimal():
                continue
            bet = int(inputStr)
            if 0 <= bet <= maxBet:
                return bet
        else:
            if not input.isdecimal():
                return 0
            bet = int(input)
            if 0 <= bet <= maxBet:
                return bet
            else:
                return 0


def getDeck() -> 'list[tuple]':
    deck: list[tuple] = []
    for s in (DIAMONDS, HEARTS, SPADES, CLUBS):
        for n in range(2, 11):
            deck.append((str(n), s))
        for c in ('J', 'Q', 'K', 'A'):
            deck.append((c, s))
    random.shuffle(deck)
    return deck


def displayHands(playerHand: 'list[tuple]', dealerHand: 'list[tuple]', showDealerHand: bool) -> None:
    print()
    if showDealerHand:
        print('ДИЛЕР:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('ДИЛЕР: ???')
        displayCards([BACKSIDE] + dealerHand[1:])
    print('ИГРОК:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards: 'list[tuple]') -> int:
    value: int = 0
    numberOfAces: int = 0
    for card in cards:
        rank: str = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)
    value += numberOfAces
    for _ in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value
            

def displayCards(cards: 'list[tuple]') -> None:
    rows: list[str] = ['', '', '', '', '']
    for _, card in enumerate(cards):
        rows[0] += ' ___   '
        if card == BACKSIDE:
            rows[1] += '|## |  '
            rows[2] += '|###|  '
            rows[3] += '|_##|  '
        else:
            rank, suit = card
            rows[1] += f'|{rank.ljust(2)} |  '
            rows[2] += f'| {suit} |  '
            rows[3] += f'|_{rank.rjust(2, "_")}|  '
    for row in rows:
        print(row)


def getMove(playerHand: 'list[tuple]', money: int) -> str:
    while True:
        moves: list[str] = ['(е)ще', '(х)ватит']
        if len(playerHand) == 2 and money > 0:
            moves.append('у(2)ить')
        movePrompt: str = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('Е', 'Х'):
            return move
        if move == '2' and 'у(2)двоить' in moves:
            return move


if __name__ == '__main__':
    main()