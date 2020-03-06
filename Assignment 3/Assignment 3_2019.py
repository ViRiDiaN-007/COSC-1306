#Assignment 3

#Trent Ishee-Dunn
#1/13/2020
#PSID: 1585551

##Formatting the output
def testFormat():
    i=0
    for test in testScores:
        print('Test ' + str(i+1) + '\t',end ='')
        i+=1
        
def scoreFormat():
    i=0
    for score in testScores:
        print('   '+str(testScores[i]) + '%\t',end='')
        i+=1
def weightFormat():
    i=0
    for weight in normalWeights:
        print(f'{(weight*100):.2f}'+'%' + '\t',end='')
        i+=1


###INPUT###
testScores = []
testWeights = []
normalWeights = []
while True:
    try:
        numTests = int(input('How many tests are there? ')) 
        studentName = input("What is the student's name? ")
        break
    except ValueError:
        print('Error: Please input a number \n ----------------------')


##Appends test scores, catches above 100/below 0
for test in range(0,numTests):
    score = int(input('Test score for test ' + str(test + 1)+ ': '))
    if score > 100:
        score = 100
    elif score < 0:
        score = 0
    testScores.append(score)

print('\n')

##Appends test weights, catches above 100/below 0
for test in range(0,numTests):
    weight = int(input('Weight of test ' + str(test+1)+ ': '))
    if weight > 100:
        weight = 100
    elif weight < 0 :
        weight = 0
    testWeights.append(weight)


##normalizes the weights
normalWeight = 0
sumWeights = sum(testWeights)
normalizer = 1/sumWeights

i=0
for weight in testWeights:
    normalWeights.append(testWeights[i]*normalizer)
    i+=1

    
###PROCESSING###
print('Time to calculate some grades...\n')

##Calculates combined score
score=0
i=0
for test in testScores:
    score += testScores[i]*normalWeights[i]
    i+=1

##Letter Grade
if score >= 85:
    letterGrade = 'A'
elif score < 85 and score >= 70:
    letterGrade = 'B'
elif score < 70 and score >= 55:
    letterGrade = 'C'
elif score < 55 and score >= 40:
    letterGrade = 'D'
else:
    letterGrade = 'F'


###OUTPUT###
print('Student Name: '+studentName+'\n')   
print('\t', end = '')
testFormat()
print('\n' + 'Scores:  ',end='')
scoreFormat()
print('\n' + 'Weights: ',end='')
weightFormat()
print('\n')
print(f'End grade is {score:.2f}')
print('Letter grade is '+letterGrade)
input()
