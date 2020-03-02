    #Create deck of 52 cards
val=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits=['spades', 'hearts', 'clubs', 'diamonds']
deck=[]
i=0
j=0
index=0
dealt=[]
score=0
hit=False
D=False
cc=0
HF=True
PW=True
DW=True

def points(dealt):
    global index
    global score
    figir=['J','Q','K']


    dealt.append(deck[index])
    if dealt[index][1]=='A':
        score=ace(score,D)
    elif dealt[index][1] in figir:
        score=score+10
    else:
        score=score+int(dealt[(len(dealt)-1)][1])
    index=index+1
    return score


def ace(score,D):
    if D==False:
        print('You were dealt an ace')
        l=input('Do you want the ace to be a 1 or an 11?')
        if l=='1':
            score=score+1
        else:
            score=score+11
    else:
        a=score+11
        if a>21:
            score=score+1
        else:
            score=score+11
    return score


#initialise deck
while i<4:
    for j in range(0,13):
        card=[suits[i],val[j]]
        deck.append(card)
    i=i+1



#shuffle deck
import random
random.shuffle(deck)

#print(deck)
print('''                                   BLACKJACK
                 First to 21 wins, can you beat the dealer?
                 ''')

input('PRESS ENTER TO BE DEALT CARDS')



#Deal 2 cards
for cc in range(0,1):
    points(dealt)
    deck.pop(0)
    score=points(dealt)
    cc+=1

for peup in range(0,cc):
    deck.pop(0)

print()
print()

print('your cards:',dealt)

while HF==True:
    print('Your current score is:', score)
    print('1.Hit me!         2.Stand')
    hit=input()
    if hit=='2':
        HF=False
    else:
        cc+=1
        print('You got:',deck[index])
        dealt.append(deck[index])
        if deck[index][1] == 'A':
            ace(score,D)
            score=ace(score,D)
        else:
            points(dealt)
        print('Your score is',score)
        if score > 21:
            print("YOU LOST")
            HF=False
            PW=False
        if score == 21:
            break

for p in range(0,(cc+1)):
    deck.pop(0)

if score == 21:
    print('BLACKJACK! YOU WIN!!!')



print()
print()
input('[Press enter key to give the dealer his cards]')
print()
print()

#DEALER
index=0
score=0
Dscore=0
AC=0
dealt=[]
D=True

while index<2:
    points(dealt)

    Dscore=points(dealt)

print("Dealer's cards:",dealt)
print("Dealer' score:",Dscore)

while Dscore<16:
        print('Dealer has less than 16')
        input()
        Dscore=points(dealt)
        print("Dealer's cards:", dealt)
        print("Dealer's score:",Dscore)

if score>21:
    DW=False


#conclusion
if PW==True and DW==True:
    if score>Dscore:
        print("Outcome:YOU WIN")
    elif score<Dscore:
        print("Dealer wins")
    else:
        print("Outcome:DEALER WINS")
elif PW==True and DW==False:
    print("Outcome:YOU WIN")
elif PW==False and DW==True:
    print("Outcome:YOU LOSE")
elif PW==False and DW==False:
    print("Outcome:Draw?")
