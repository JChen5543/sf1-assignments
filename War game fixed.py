import random

ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")
jackpot = []
deck = [(rank, suit) for rank in ranks for suit in suits]

random.shuffle(deck)

p1 = deck[0:26]
p2 = deck[26:]

def game_round(p1, p2, jackpot): 
    while p1 and p2:    
            print(f"Player 1's card is {p1[0]}")
            print(f"Player 2's card is {p2[0]}")
            card_comparison(p1, p2, jackpot)
    if len(p1) == 0:
            print("Player 2 has won the game!")
            
    if len(p2) == 0:
            print("Player 1 has won the game!")
            




def card_comparison(p1, p2, jackpot):
    jackpot.append(p1.pop(0))
    jackpot.append(p2.pop(0))

    if ranks.index(jackpot[-2][0]) > ranks.index(jackpot[-1][0]): #we use -1 and -2, since in the case of war, we need to check the last 2 played cards instead
        p1.extend(jackpot)
        print("Player 1 has won the round!")
    elif ranks.index(jackpot[-2][0]) < ranks.index(jackpot[-1][0]):
        p2.extend(jackpot)
        print("Player 2 has won the round!")

    elif ranks.index(jackpot[-2][0]) == ranks.index(jackpot[-1][0]):
        print("WAR")
        war(jackpot)
        card_comparison(p1, p2, jackpot)
    jackpot.clear()

def war(jackpot): #a little wordy, but we need to be sure that we don't check an index out of range
    global p1
    global p2 #since p1 and p2 when at less than 4 are re-assigned, global is used to actually store that change
    
    if len(p1) >= 4 and len(p2) >= 4: #when both players have at least 4 cards
        for x in range(0, 2): #only pop 3, since card comparison will pop one anyways
            jackpot.append(p1.pop(x))
            jackpot.append(p2.pop(x))
    elif len(p1) >= 4 and len(p2) < 4:
        for x in range(0, 2):
            jackpot.append(p1.pop(x))
        
        jackpot.extend(p2)
        del(jackpot[-1])
        p2 = p2[:len(p2)]
        

    elif len(p1) < 4 and len(p2) >= 4:
        for x in range(0, 2):
            jackpot.append(p2.pop(x))
        jackpot.extend(p1)
        del(jackpot[-1])
        p1 = p1[:len(p1)]
        
    elif len(p1) < 4 and len(p2) < 4:
        jackpot.extend(p1) #adds p1
        del(jackpot[-1]) #removes the last card (the one that will be played for card comparison)
        jackpot.extend(p2) #same for p2
        del(jackpot[-1])
        p2 = p2[:len(p2)]
        p1 = p1[:len(p1)]

    
game_round(p1, p2, jackpot)
