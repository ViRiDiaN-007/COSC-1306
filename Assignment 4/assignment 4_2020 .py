
#Assignment 4

import random

count=0
sums=[]
numTimes={2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}

def logo():
    print('''
  ___  _          ___         _          _    _ _ _ _         
 |   \(_)__ ___  | _ \_ _ ___| |__  __ _| |__(_) (_) |_ _  _  
 | |) | / _/ -_) |  _/ '_/ _ \ '_ \/ _` | '_ \ | | |  _| || | 
 |___/|_\__\___| |_| |_| \___/_.__/\__,_|_.__/_|_|_|\__|\_, | 
                                                        |__/
                                                        ''')
def rollDice():
    die1,die2=random.randint(1,6),random.randint(1,6)
    return die1,die2

while count <1000:
    sums.append(sum(rollDice()))
    count+=1

    
for num in numTimes:
    for item in sums:
        if item == num:
            numTimes[num]+=1
logo()
print('\t+---------------------------------------+')
for num in numTimes:
    print(f'\t|\tSum = {num} showed up {numTimes[num]} times\t|')
print('\t+---------------------------------------+')
input()

