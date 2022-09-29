from operator import index
import random

#icons = ["🍅","🍓","🫐","🍒","🍋","🌶"]
reelicons = ["6","6","6","6","6","6","5","5","5","5","5","4","4","4","4","3","3","3","2","2","1"] #These are all strings!!

balance = 199
lost = 1
won = 0

outcome = []
their_currency = "£"



def reels(no_of_reels, reelicons, outcome, their_currency, balance, lost, won):
    outcome = []
    for i in range(no_of_reels):
        random.shuffle(reelicons)
        reel = reelicons[1]
        print(reel)
        outcome.append(reel)
    print("Balance:", balance,"  lost:", lost, "   won:", won)
    #print(outcome)
    #print("\n    ",len(outcome))
    if outcome[0] == outcome[1] and outcome[1] == outcome[2]:  
        
        #won_cash = win(outcome)           

        if outcome[0] == "1" :
            cash_won = 9000                                
        elif outcome[0] == "2" :
            cash_won = 1000                                
        elif outcome[0] == "3" :
            cash_won = 300                                
        elif outcome[0] == "4" :
            cash_won = 100                                
        elif outcome[0] == "5" :
            cash_won = 60                                
        elif outcome[0] == "6" :
            cash_won = 30
        won += int(cash_won)
        balance += cash_won
        print("Win!\n You've Won " + their_currency + str(cash_won) + ". " + "Your balance is " + their_currency + str(balance))
        
    else:
        print("House wins")
        lost += 1
        print("lost:", lost)
       
    return outcome



  
    reels(3, reelicons, outcome, their_currency, balance, lost, won)
    balance -= 1
    
    next = input()


# Three 6's ~1/42   £30
# Three 5's ~1/75   £60
# Three 4's ~1/145  £100
# Three 3's ~1/343  £300
# Three 2's ~1/1158 £1000
# Three 1's ~1/9261 £9000

def prbcalc(freq, reels, tot_icons):
    """ 
    num = freq ** reels 
    den = tot_icons ** reels
    prob = num / den
    #prob = prob * 100
    
    """
    num = freq ** reels 
    den = tot_icons ** reels
    bans = den / num
    bans = int(round(bans, 0))
    prob = "1/" + str(bans)
    return prob

#print(prbcalc(1, 3, 21))




"""

class win(outcome):
    if outcome[0] == 1 :
        cash_won = 9000
    if outcome[0] == 2 :
        cash_won = 1000
    if outcome[0] == 3 :
        cash_won = 300
    if outcome[0] == 4 :
        cash_won = 100
    if outcome[0] == 5 :
        cash_won = 60
    if outcome[0] == 6 :
        cash_won = 30
    
"""






