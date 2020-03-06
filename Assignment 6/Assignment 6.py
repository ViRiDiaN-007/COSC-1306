import math
    
#returns the knn and their labels
def getNeighbors(indexTracker,labels,cut,data):
    neighbors=[]
    neighborLabels=[]
    for point in indexTracker:
        if point[0]<=cut:
            neighbors.append(data[point[1]])
            neighborLabels.append(labels[point[1]])
    return neighbors,neighborLabels
    
#Returns the final group
def getVote(neighbors,neighborLabels):
    count0=0
    count1=0
    for label in neighborLabels:
        if label==0:
            count0+=1
        else:
            count1+=1
    if count0>count1:
        return 0
    elif count0==count1:
        return 'Error: Counts are equal'
    else:
        return 1
    
#returns distance between two points
def dist(p1,p2):
    x1=p1[0]
    y1=p1[1]
    x2=p2[0]
    y2=p2[1]
    distance = math.sqrt(math.pow(x2-x1,2)+(math.pow(y2-y1,2)))
    return distance

#Given Dataset
def getData():
    return [
        [8,8],[2,8],[3,7],
        [3,4],[2,6],[3,5],
        [6,5],[7,3],[7,5]]

#Labels for each point in the dataset
def getLabels():
    return[1,0,0,0,0,0,1,1,1]

#Distance of each point
def getDist(dataList,test):
    dList=[]
    indexTracker=[]
    for index,element in enumerate(dataList):
        indexTracker.append([round(dist(element,test),2),index])
        dList.append(round(dist(element,test),2))
    return dList,indexTracker

#sorts the dlist
def sortDist(dList):
    sList=sorted(dList)
    return sList

#gets cutoff value
def getCut(sList,k):
    cut=(sList[k-1]+sList[k])/2
    return cut


#Main
data=getData()
labels=getLabels()
print('Data Set\n',data)
print('\nLabel Set\n',labels)
k=int(input('\nEnter the K value: '))

end=False
while not end:   
    #get the test point
    test=[]
    test.append(int(input('Enter x value: ')))
    test.append(int(input('Enter y value: ')))
    
    #get distance list, sorted list, cutoff value, unpack neighbors and labels
    dList,indexTracker=getDist(data,test)
    sList=sortDist(dList)
    cut=getCut(sList,k)
    neighbors,neighborLabels=getNeighbors(indexTracker,labels,cut,data)
    
    #print out variables
    print('\nDistance from test to all points:\n',dList)
    print('\nSorted List:\n',sList)
    print('\nKNN and their groups:\n',neighbors,'\n',neighborLabels)
    print(f'\n\nTest {test} belongs to group: ',getVote(neighbors,neighborLabels))
    
    #repeat until quit
    question=input('\nWould you like to test more cases? [Y/N]: ')
    if question.lower()=='n':
        end=True
