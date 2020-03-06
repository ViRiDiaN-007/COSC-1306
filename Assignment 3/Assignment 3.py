
#Name:
#Date:
#PSID:
import time

testScores=[]
weights=[]
normalWeights=[]

end=True
while  end:
    for num in range(3):
        score = int(input('Enter the score for test '+str(num+1)+': '))
        
        if score>100 : score=100
        if score<0 : score=0
    
        testScores.append(score)
        weight = int(input('Enter the weight of test '+str(num+1)+': '))
        weights.append(weight)
        
    ##Ends if weights dont add up to 100   
    if sum(weights) != 100:
        print('Weights do not add to 100. Program Ending.')
        break
    
    ##normalizes the weights
    sumWeights = sum(weights)
    normalizer = 1/sumWeights

    for weight in weights:
        normalWeights.append(weight*normalizer)

    ##Calculates combined score
    finalGrade=0
    i=0
    for test in testScores:
        finalGrade += test*normalWeights[i]
        i+=1

    ##Letter Grade
    if finalGrade >= 85:
        letterGrade = 'A'
    elif finalGrade < 85 and finalGrade >= 70:
        letterGrade = 'B'
    elif finalGrade < 70 and finalGrade >= 55:
        letterGrade = 'C'
    elif finalGrade < 55 and finalGrade >= 40:
        letterGrade = 'D'
    else:
        letterGrade = 'F'

    ###OUTPUT###
    print(f'End grade is {finalGrade:.2f}')
    print('Letter Grade: ' + letterGrade)
    ans = input('Program complete. Press "Q" to quit, or any key to continue: ')
    if ans.lower() == 'q':
        print('Thank you. The program will close in 5 seconds')
        time.sleep(5)
        break
    else:
        print("Let's continue \n")
        testScores.clear()
        weights.clear()
        normalWeights.clear()
        pass

