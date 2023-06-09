
from algorithms import Solution
import  random
from generator import generateRandomGraphAll,generateRandomGraph,generateRandomHn,generateRandomGn,DrawGraph,getManualData
import string

ans=input('If you want to run the ready graph, enter Y,if no enter N : ')
while ans != 'Y' and ans != 'N':
    ans = input('Please enter valid choice: ')
if ans == 'Y':
    (graph,Hn)=getManualData()
    goal='G'
    l,n=2,2
    Solution(graph,Hn,goal,n,l)
    print('the Graph is:',graph)
    print('The Heuristic is:',Hn)
    print('The Goal is:',goal)
    DrawGraph(graph)
else:
    ans=input('Do you want to specify the number of children and parents and goal? if yes enter Y if no enter N and goal: ')
    while ans != 'Y' and ans != 'N':
        ans = input('Please enter valid choice: ')
    if ans == 'Y':
        randomGraph=generateRandomGraph()
        randomGraphGn=generateRandomGn(randomGraph)
        print('The Graph is:', randomGraphGn)
        DrawGraph(randomGraphGn)
        goal=input('Enter valid goal: ')
        n=int(input('input valid number child in beam search: '))
        randomHn = generateRandomHn(randomGraphGn,goal)
        print('Heuristic is: ', randomHn)
        l=random.randint(1,6)#from LDS
        Solution(randomGraphGn,randomHn,goal,n,l)
    else:
        randomGraph=generateRandomGraphAll()
        print('The Graph is:', randomGraph)
        goal,n,l=random.choice(string.ascii_uppercase),random.randint(1,3),random.randint(3,5)
        randomHn = generateRandomHn(randomGraph, goal)
        print('Heuristic is: ', randomHn)
        print('The gola is:',goal)
        Solution(randomGraph, randomHn, goal, n, l)
        DrawGraph(randomGraph)


