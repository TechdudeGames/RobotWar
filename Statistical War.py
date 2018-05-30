import random
from blessings import Terminal
term = Terminal()
import os
import time
starttime=time.time()
os.system("clear")
debugoutput=False
cardnumdebugoutput=True
class card2():
    worth = 2
    kind=2
class card3():
    worth = 3
    kind=3
class card4():
    worth = 4
    kind=4
class card5():
    worth = 5
    kind=5
class card6():
    worth = 6
    kind=6
class card7():
    worth = 7
    kind=7
class card8():
    worth = 8
    kind=8
class card9():
    worth = 9
    kind=9
class card10():
    worth = 10
    kind=10
class cardjack():
    worth = 11
    kind='Jack'
class cardqueen():
    worth = 12
    kind='Queen'
class cardking():
    worth = 13
    kind="King"
class cardace():
    worth = 14
    kind="Ace"
cardtypes=[card2,card3,card4,card5,card6,card7,card8,card9,card10,cardjack,cardqueen,cardking,cardace]
tmp_deck=[]
for i in cardtypes:
    for l in range(0, 4):
        tmp_deck.append(i)
shuffled_deck=[]
welcome_message = '===== Welcome to Robot War ===== \n' \
                  '===== A Program that makes computer play the War Card game over and over=====\n' \
                  'Written by TechdudeGames (Brennan Romero)\n'
print(welcome_message)
p1wins = 0
p2wins = 0
draws = 0
plays = 0
while True:
    if debugoutput : print("Shuffling the cards...")
    shuffled_deck = []
    for shufflenumber in range(0, 10):
        while tmp_deck.__len__() != 0:
            index = random.randint(0, len(tmp_deck) - 1)
            selection = tmp_deck[index]
            shuffled_deck.append(tmp_deck[index])
            tmp_deck.remove(selection)
        tmp_deck = shuffled_deck
        shuffled_deck = []
    tmp_deck.reverse()
    shuffled_deck = list(tmp_deck)  # Note, the top of the list is now the last index.

    if debugoutput : print("Shuffled the cards")
    if debugoutput : print("Divying them up...")
    playerone = shuffled_deck[0:int(len(shuffled_deck) / 2)]
    playertwo = shuffled_deck[int(len(shuffled_deck) / 2):]
    if debugoutput : print("Players have their cards now.")
    if debugoutput : print("The match has now started.\n\n")
    numberofrounds = 1
    cancontinue = True
    while (len(playerone) != 0 and len(playertwo) != 0) and cancontinue:
        p1c = playerone.pop()
        p2c = playertwo.pop()
        p1cw = p1c.worth
        p2cw = p2c.worth
        if debugoutput : print("Player one's card:", p1c.kind)
        if debugoutput : print("Player two's card:", p2c.kind)
        if p1cw > p2cw:
            if debugoutput : print("Player One wins round %i" % numberofrounds)
            playerone.insert(0, p1c)
            playerone.insert(0, p2c)
        elif p2cw > p1cw:
            if debugoutput : print("Player Two wins round %i" % (numberofrounds))
            playertwo.insert(0, p2c)
            playertwo.insert(0, p1c)
        elif p2cw == p1cw:
            if debugoutput : print("Let us go to war!")
            cardpot = []
            iswinner = False
            while (True != iswinner):
                cardpot.append(p1c)
                cardpot.append(p2c)
                if playerone.__len__() < 4:
                    if playertwo.__len__() < 4:
                        if debugoutput : print("And it appears both parties ran of of cards to play.")
                        cancontinue = False
                        draws+=1
                        break
                    else:
                        if debugoutput : print("Player One has run out of cards to properly play war, therefor Player Two has won the game!")
                        p2wins += 1
                        cancontinue = False
                        break
                elif playertwo.__len__() < 4:
                    if debugoutput : print("Player Two has run out of playable cards to properly play war, therefor Player One has won the game!")
                    p1wins += 1
                    cancontinue = False
                    break
                else:
                    for i in range(0, 3):
                        cardpot.append(playerone.pop())
                        cardpot.append(playertwo.pop())
                    p1c = playerone.pop()
                    p2c = playertwo.pop()
                    p1cw = p1c.worth
                    p2cw = p2c.worth
                    if debugoutput : print("Player one's card:", p1c.kind)
                    if debugoutput : print("Player two's card:", p2c.kind)
                    if p1cw > p2cw:
                        if debugoutput : print("Player One wins the war on round %i" % numberofrounds)
                        iswinner = True
                        playerone.insert(0, p1c)
                        playerone.insert(0, p2c)
                        for card in cardpot:
                            playerone.insert(0, card)
                    elif p2cw > p1cw:
                        if debugoutput : print("Player Two wins the war on round %i" % (numberofrounds))
                        iswinner = True
                        playertwo.insert(0, p1c)
                        playertwo.insert(0, p2c)
                        for card in cardpot:
                            playertwo.insert(0, card)

        numberofrounds += 1
        with term.location(y=5):
            if cardnumdebugoutput : print("Number of cards in Player One's Deck: %i" % playerone.__len__())
            if cardnumdebugoutput : print("Number of cards in Player Two's Deck: %i \n\n" % playertwo.__len__())
    if playerone.__len__() == 0 and cancontinue == True:
        if debugoutput : print("Player Two has won the Game!")
        p2wins += 1
    elif playertwo.__len__() == 0  and cancontinue == True:
        if debugoutput : print("Player One has won the Game")
        p1wins += 1
    plays += 1
    with term.location(0,10):
        print("Player One has won %f percent of the time       " %float(p1wins*100 / plays))
        print("Player Two has won %f percent of the time       " %float(p2wins*100 / plays))
        print("There has been a draw %f percent of the time     \n" %float(draws / plays) )
        print("Player One has won %i times" %p1wins)
        print("Player Two has won %i times" %p2wins)
        print("There have been %i draws" %draws)
        print("The game has been played %i times" %plays)
        elapsted_seconds = time.time()-starttime
        days = int(elapsted_seconds//86400)
        hours = int(elapsted_seconds//3600 - days * 24)
        minutes = int(elapsted_seconds//60 - hours * 60)
        seconds = int(elapsted_seconds - minutes * 60)
        print("Time Elapsed: ", days, ":", hours, ":", minutes, ":", seconds)
