import time
import random
import os
def shuffledeck():
    deck = ['AH','AD','AB','AS','2H','2D','2B','2S','3H','3D','3B','3S','4H','4D','4B','4S','5H','5D','5B','5S','6H','6D','6B','6S','7H','7D','7B','7S','8H','8D','8B','8S','9H','9D','9B','9S','10H','10D','10B','10S','JH','JD','JB','JS','QH','QD','QB','QS','KH','KD','KB','KS']
    random.shuffle(deck)
    return deck
def cards(card):
    if(card == 'AH'):
        print("-------")
        print("|❤   |")
        print("|  A  |")
        print("|   ❤|")
        print("-------")
    elif(card == '2H'):
        print("-------")
        print("|❤   |")
        print("|  2  |")
        print("|   ❤|")
        print("-------")
    elif (card == '3H'):
        print("-------")
        print("|❤   |")
        print("|  3  |")
        print("|   ❤|")
        print("-------")
    elif (card == '4H'):
        print("-------")
        print("|❤   |")
        print("|  4  |")
        print("|   ❤|")
        print("-------")
    elif (card == '5H'):
        print("-------")
        print("|❤   |")
        print("|  5  |")
        print("|   ❤|")
        print("-------")
    elif (card == '6H'):
        print("-------")
        print("|❤   |")
        print("|  6  |")
        print("|   ❤|")
        print("-------")
    elif (card == '7H'):
        print("-------")
        print("|❤   |")
        print("|  7  |")
        print("|   ❤|")
        print("-------")
    elif (card == '8H'):
        print("-------")
        print("|❤   |")
        print("|  8  |")
        print("|   ❤|")
        print("-------")
    elif (card == '9H'):
        print("-------")
        print("|❤   |")
        print("|  9  |")
        print("|   ❤|")
        print("-------")
    elif (card == '10H'):
        print("-------")
        print("|❤   |")
        print("|  10 |")
        print("|   ❤|")
        print("-------")
    elif (card == 'JH'):
        print("-------")
        print("|❤   |")
        print("|  J  |")
        print("|   ❤|")
        print("-------")
    elif (card == 'QH'):
        print("-------")
        print("|❤   |")
        print("|  Q  |")
        print("|   ❤|")
        print("-------")
    elif (card == 'KH'):
        print("-------")
        print("|❤   |")
        print("|  K  |")
        print("|   ❤|")
        print("-------")
    elif (card == 'AD'):
        print("-------")
        print("|♦   |")
        print("|  A  |")
        print("|   ♦|")
        print("-------")
    elif (card == '2D'):
        print("-------")
        print("|♦   |")
        print("|  2  |")
        print("|   ♦|")
        print("-------")
    elif (card == '3D'):
        print("-------")
        print("|♦   |")
        print("|  3  |")
        print("|   ♦|")
        print("-------")
    elif (card == '4D'):
        print("-------")
        print("|♦   |")
        print("|  4  |")
        print("|   ♦|")
        print("-------")
    elif (card == '5D'):
        print("-------")
        print("|♦   |")
        print("|  5  |")
        print("|   ♦|")
        print("-------")
    elif (card == '6D'):
        print("-------")
        print("|♦   |")
        print("|  6  |")
        print("|   ♦|")
        print("-------")
    elif (card == '7D'):
        print("-------")
        print("|♦   |")
        print("|  7  |")
        print("|   ♦|")
        print("-------")
    elif (card == '8D'):
        print("-------")
        print("|♦   |")
        print("|  8  |")
        print("|   ♦|")
        print("-------")
    elif (card == '9D'):
        print("-------")
        print("|♦   |")
        print("|  9  |")
        print("|   ♦|")
        print("-------")
    elif (card == '10D'):
        print("-------")
        print("|♦   |")
        print("|  10 |")
        print("|   ♦|")
        print("-------")
    elif (card == 'JD'):
        print("-------")
        print("|♦   |")
        print("|  J  |")
        print("|   ♦|")
        print("-------")
    elif (card == 'QD'):
        print("-------")
        print("|♦   |")
        print("|  Q  |")
        print("|   ♦|")
        print("-------")
    elif (card == 'KD'):
        print("-------")
        print("|♦   |")
        print("|  K  |")
        print("|   ♦|")
        print("-------")
    elif (card == 'AB'):
        print("-------")
        print("|♣️ |")
        print("|  A  |")
        print("|   ♣|")
        print("-------")
    elif (card == '2B'):
        print("-------")
        print("|♣️ |")
        print("|  2  |")
        print("|   ♣|")
        print("-------")
    elif (card == '3B'):
        print("-------")
        print("|♣️ |")
        print("|  3  |")
        print("|   ♣|")
        print("-------")
    elif (card == '4B'):
        print("-------")
        print("|♣️ |")
        print("|  4  |")
        print("|   ♣|")
        print("-------")
    elif (card == '5B'):
        print("-------")
        print("|♣️ |")
        print("|  5  |")
        print("|   ♣|")
        print("-------")
    elif (card == '6B'):
        print("-------")
        print("|♣️ |")
        print("|  6  |")
        print("|   ♣|")
        print("-------")
    elif (card == '7B'):
        print("-------")
        print("|♣️ |")
        print("|  7  |")
        print("|   ♣|")
        print("-------")
    elif (card == '8B'):
        print("-------")
        print("|♣️ |")
        print("|  8  |")
        print("|   ♣|")
        print("-------")
    elif (card == '9B'):
        print("-------")
        print("|♣️ |")
        print("|  9  |")
        print("|   ♣|")
        print("-------")
    elif (card == '10B'):
        print("-------")
        print("|♣️ |")
        print("|  10 |")
        print("|   ♣|")
        print("-------")
    elif (card == 'JB'):
        print("-------")
        print("|♣️ |")
        print("|  J  |")
        print("|   ♣|")
        print("-------")
    elif (card == 'QB'):
        print("-------")
        print("|♣️ |")
        print("|  Q  |")
        print("|   ♣|")
        print("-------")
    elif (card == 'KB'):
        print("-------")
        print("|♣️ |")
        print("|  K  |")
        print("|   ♣|")
        print("-------")
    elif (card == 'AS'):
        print("-------")
        print("|♠️ |")
        print("|  A  |")
        print("|   ♠|")
        print("-------")
    elif (card == '2S'):
        print("-------")
        print("|♠️ |")
        print("|  2  |")
        print("|   ♠|")
        print("-------")
    elif (card == '3S'):
        print("-------")
        print("|♠️ |")
        print("|  3  |")
        print("|   ♠|")
        print("-------")
    elif (card == '4S'):
        print("-------")
        print("|♠️ |")
        print("|  4  |")
        print("|   ♠|")
        print("-------")
    elif (card == '5S'):
        print("-------")
        print("|♠️ |")
        print("|  5  |")
        print("|   ♠|")
        print("-------")
    elif (card == '6S'):
        print("-------")
        print("|♠️ |")
        print("|  6  |")
        print("|   ♠|")
        print("-------")
    elif (card == '7S'):
        print("-------")
        print("|♠️ |")
        print("|  7  |")
        print("|   ♠|")
        print("-------")
    elif (card == '8S'):
        print("-------")
        print("|♠️ |")
        print("|  8  |")
        print("|   ♠|")
        print("-------")
    elif (card == '9S'):
        print("-------")
        print("|♠️ |")
        print("|  9  |")
        print("|   ♠|")
        print("-------")
    elif (card == '10S'):
        print("-------")
        print("|♠️ |")
        print("|  10 |")
        print("|   ♠|")
        print("-------")
    elif (card == 'JS'):
        print("-------")
        print("|♠️ |")
        print("|  J  |")
        print("|   ♠|")
        print("-------")
    elif (card == 'QS'):
        print("-------")
        print("|♠️ |")
        print("|  Q  |")
        print("|   ♠|")
        print("-------")
    elif (card == 'KS'):
        print("-------")
        print("|♠️ |")
        print("|  K  |")
        print("|   ♠|")
        print("-------")

def cScore(card):
    if(card[0] == 'A'):
        return 11
    elif(card[0] == '2'):
        return 2
    elif (card[0] == '3'):
        return 3
    elif (card[0] == '4'):
        return 4
    elif (card[0] == '5'):
        return 5
    elif (card[0] == '5'):
        return 5
    elif (card[0] == '6'):
        return 6
    elif (card[0] == '7'):
        return 7
    elif (card[0] == '8'):
        return 8
    elif (card[0] == '9'):
        return 9
    else:
        return 10
def draw(deck):
    card = deck[0]
    deck.pop(0)
    return card
def placeBet(money):
    print("Place your bet:")
    bet = int(input())
    while (bet <= 0 or bet > money):
        if (bet <= 0):
            print("You can't bet negative numbers!")
            print("Try again, Place your bet: ")
            bet = int(input())
        elif (bet > money):
            print("You can't bet more than what you have!")
            print(f"Money available: {money}")
            print("Try again, Place your bet: ")
            bet = int(input())
    money = money - bet
    return money,bet

def basicStrat(pCount, dCount, pAce, pDouble):
    if((not pAce) and (not pDouble)):
        basicMatrix = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Hit', 'Hit'],
            [0, 0, 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Double Down'],
            [0, 0, 'Hit', 'Hit', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],
            [0, 0, 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],
            [0, 0, 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],
            [0, 0, 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],
            [0, 0, 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand']
        ]
        return basicMatrix[pCount][dCount]
    elif(pAce and (not pDouble)):
        basicMatrix = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 'Hit', 'Hit', 'Hit', 'Double Down', 'Double Down', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Hit', 'Hit', 'Hit', 'Double Down', 'Double Down', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Hit', 'Hit', 'Double Down', 'Double Down', 'Double Down', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Hit', 'Hit', 'Double Down', 'Double Down', 'Double Down', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Hit', 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Stand', 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],
            [0, 0, 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],
            [0, 0, 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand']
        ]
        return basicMatrix[pCount-11][dCount]
    else:
        basicMatrix = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 'Split', 'Split', 'Split', 'Split', 'Split', 'Split', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Split', 'Split', 'Split', 'Split', 'Split', 'Split', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Hit', 'Hit', 'Hit', 'Split', 'Split', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, "Double Down", 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Double Down', 'Hit', 'Hit'],
            [0, 0, 'Split', 'Split', 'Split', 'Split', 'Split', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Split', 'Split', 'Split', 'Split', 'Split', 'Split', 'Split', 'Hit', 'Hit', 'Hit'],
            [0, 0, 'Split', 'Split', 'Split', 'Split', 'Split', 'Split', 'Split', 'Split', 'Split', 'Split'],
            [0, 0, 'Split', 'Split', 'Split', 'Split', 'Split', 'Stand', 'Split', 'Split', 'Stand', 'Stand'],
            [0, 0, 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],
            [0, 0, 'Split', 'Split', 'Split', 'Split', 'Split', 'Split', 'Split', 'Split', 'Split', 'Split']
        ]
        return basicMatrix[pCount/2][dCount]



if __name__ == '__main__':
    play = True
    print("This is BlackJack");
    print("BlackJack pays 3:2")
    print("How much money would you like to deposit?")
    money = int(input())
    while(play and money>0):
        dDown = False
        pAce = False
        pPair = False
        dAce = False
        blackjack = False
        pCount = 0
        dCount = 0
        bet = 0
        deck = shuffledeck()
        # Player places bet:
        money,bet = placeBet(money)
        time.sleep(1)
        # Player's first card
        print("Player's hand goes first")
        pc1 = draw(deck)
        print(cards(pc1))
        pCount += cScore(pc1)
        time.sleep(1)
        # Dealer's first card
        print("Dealer's hand")
        dc1 = draw(deck)
        dCount += cScore(dc1)
        print("X")
        time.sleep(1)
        # Second card:
        # Player's second card:
        print("Player's second card")
        pc2 = draw(deck)
        print(cards(pc2))
        pCount += cScore(pc2)
        if(pCount == 21):
            blackjack = True
            print("BLACKJACK!!!")
        time.sleep(1)
        # Dealers second card:
        print("Dealer's hand")
        dc2 = draw(deck)
        print(cards(dc2))
        dCount += cScore(dc2)
        time.sleep(1)
        # Player stands, hits:
        print("Player's cards:")
        print(cards(pc1), cards(pc2))
        print("Player's count:")
        print(pCount)
        print("Dealer's cards")
        print(f"X {cards(dc2)}")
        print("Dealer's known count:")
        print(dCount-cScore(dc1))
        time.sleep(1)
        hit = False
        if(pc1[0] == 'A' or pc2[0] == 'A'):
            pAce = True
        if(dc1[0] == 'A' or dc2[0] == 'A'):
            dAce = True
        while(pCount <21):
            if(not hit):
                print("Do you want to Hit(H), Stand(S), or Double Down(D)?")
                decision = input()
                shouldHave = basicStrat(pCount, dCount-cScore(dc1), pAce, pPair)
                if(decision == 'H'):
                    print(cards(deck[0]))
                    if (cScore(deck[0]) == 11):
                        pAce = True
                    pCount += cScore(deck[0])
                    deck.pop(0)
                    print("Player's count:")
                    print(pCount)
                    hit = True
                elif(decision == 'D'):
                    dDown = True
                    money -= bet
                    bet = 2*bet
                    print(cards(deck[0]))
                    if (cScore(deck[0]) == 11):
                        pAce = True
                    pCount += cScore(deck[0])
                    deck.pop(0)
                    print("Player's count:")
                    print(pCount)
                    break
                elif(decision == 'S'):
                    break
            else:
                print("Do you want to Hit(H) or Stand(S)?")
                shouldHave = basicStrat(pCount, dCount - cScore(dc1), pAce, pPair)
                decision = input()
                if (decision == 'H'):
                    if (cScore(deck[0]) == 11):
                        pAce = True
                    print(cards(deck[0]))
                    pCount += cScore(deck[0])
                    deck.pop(0)
                    print("Player's count:")
                    print(pCount)
                    hit = True
                elif(decision == 'S'):
                    break
        while(pAce):
            if(pCount > 21 and pAce):
                pCount -= 10
                pAce = False
                if(dDown):
                    break
                while(pCount<21):
                    print("Do you want to Hit(H) or Stand(S)?")
                    shouldHave = basicStrat(pCount, dCount - cScore(dc1), pAce, pPair)
                    decision = input()
                    if (decision == 'H'):
                        print(cards(deck[0]))
                        if(cScore(deck[0]) == 11):
                            pAce = True
                        pCount += cScore(deck[0])
                        deck.pop(0)
                        print("Player's count:")
                        print(pCount)
                        hit = True
                    elif (decision == 'S'):
                        break
            else:
                pAce = False
        time.sleep(0.75)
        if(pCount>21):
            print("Dealer wins")
            print(f"Basic Strategy indicated you should have {shouldHave}.")
            print(f"Balance: {money}")
            print("Would you like to play another hand? (Y/N)")
            answer = input()
            while (answer != "Y" and answer != "N"):
                print("Invalid input, please enter (Y/N):")
                answer = input()
            if(answer == "Y"):
                continue
            elif(answer == "N"):
                play = False
                continue
        print("Dealer opens up:")
        print(cards(dc1), cards(dc2))
        print("Dealer's count:")
        print(dCount)
        time.sleep(2)
        while(dCount<17):
            print("Dealer hits:")
            print(cards(deck[0]))
            dCount += cScore((deck[0]))
            deck.pop(0)
            print("Dealer's count:")
            print(dCount)
            time.sleep(1)
        if(dCount > 21):
            print(f"Player wins: {2*bet}")
            print(f"Basic Strategy indicated you should have {shouldHave}.")
            money += 2*bet
            print(f"Balance: {money}")
            print("Would you like to play another hand? (Y/N)")
            answer = input()
            while (answer != "Y" and answer != "N"):
                print("Invalid input, please enter (Y/N):")
                answer = input()
            if (answer == "Y"):
                continue
            elif(answer == "N"):
                play = False
                continue
        else:
            if(dCount>pCount):
                print("Dealer wins")
                print(f"Basic Strategy indicated you should have {shouldHave}.")
                print(f"Balance: {money}")
                print("Would you like to play another hand? (Y/N)")
                answer = input()
                while (answer != "Y" and answer != "N"):
                    print("Invalid input, please enter (Y/N):")
                    answer = input()
                if (answer == "Y"):
                    continue
                elif(answer == "N"):
                    play = False
                    continue
            elif(dCount == pCount):
                print("It's a tie, you get your bet back")
                print(f"Basic Strategy indicated you should have {shouldHave}.")
                money += bet
                print(f"Balance: {money}")
                print("Would you like to play another hand? (Y/N)")
                answer = input()
                while (answer != "Y" and answer != "N"):
                    print("Invalid input, please enter (Y/N):")
                    answer = input()
                if (answer == "Y"):
                    continue
                elif (answer == "N"):
                    play = False
                    continue
            elif(pCount>dCount and blackjack):
                print(f"Player wins: {2 * bet+bet}")
                money += 2 * bet+bet
                print(f"Balance: {money}")
                print("Would you like to play another hand? (Y/N)")
                answer = input()
                while (answer != "Y" and answer != "N"):
                    print("Invalid input, please enter (Y/N):")
                    answer = input()
                if (answer == "Y"):
                    continue
                elif (answer == "N"):
                    play = False
                    continue
            else:
                print(f"Player wins: {2*bet}")
                print(f"Basic Strategy indicated you should have {shouldHave}.")
                money += 2*bet
                print(f"Balance: {money}")
                print("Would you like to play another hand? (Y/N)")
                answer = input()
                while(answer != "Y" and answer != "N"):
                    print("Invalid input, please enter (Y/N):")
                    answer = input()
                if (answer == "Y"):
                    continue
                elif (answer == "N"):
                    play = False
                    continue
    if(money== 0):
        print("You're broke and lost all your money, better luck next time")






