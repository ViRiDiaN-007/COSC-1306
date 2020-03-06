
#Assignment 2

#Trent Ishee-Dunn
#1/13/2020
#PSID: 1585551

import math

name= input('Enter the name of the cake: ')
diam = int(input('Diameter of cake in inches: '))
height = int(input('Height of the cake in inches: '))
price= input('Price of the cake per cubic inch: ')
price=price.strip('$')
price=float(price)
print('\n',end='')
#Calculate volume
radius = diam/2
fdVolume = round((math.pi * math.pow(radius,2)*height),2)
totalPrice = round(fdVolume*price,2)


print('Volume:',fdVolume)
print('Price of cake is $',totalPrice,sep='')
input()


