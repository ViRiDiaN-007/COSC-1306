#Assignment 4

#Trent Ishee-Dunn
#1/13/2020
#PSID:1585551

lowerBound = int(input('Enter the lower bound: '))
upperBound = int(input('Enter the upper bound: '))

numPrimes=0;primeNums=[]
for number in range(lowerBound,upperBound+1):
    prime = True
    if number <=1:
        prime = False
    for i in range(2,number):
        if number%i == 0:
            prime = False
    if prime:
        primeNums.append(number)
        numPrimes += 1
                
print('The number of prime numbers between ' + str(lowerBound) + ' and '+ str(upperBound) + ' is: ' + str(numPrimes))
print('The prime values are: ' + str(primeNums))
input()
