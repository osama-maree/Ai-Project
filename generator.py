import networkx as nx
import matplotlib.pyplot as plt
import random
import string
from tabulate import tabulate

def DrawGraph(randomGraph):
    G = nx.DiGraph(directed=True)
    for i in randomGraph.keys():
        for j in randomGraph[i]:
            G.add_edge(i,j,weight=randomGraph[i][j])
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 4]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 4]
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=3,edge_color='g')
    nx.draw_networkx_edges(
        G, pos, edgelist=esmall, width=2, edge_color="r", style="dashed"
    )
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.show()

#genrate random graph with random number of children and random number of parent
def generateRandomGraphAll():
    numberNode = random.randint(5, 7)#get Random number of parent
    randomGraph = {}
    visited = []
    while len(randomGraph.keys()) < numberNode:
        numberOfchild= random.randint(2, 5) #get random child for each node inside graph
        if len(randomGraph.keys()) == 0:
            randomChild = random.choice(string.ascii_uppercase)
            randomGraph[randomChild] = {}
            visited.append(randomChild)
            childadded = [randomChild]
            while len(randomGraph[randomChild]) < numberOfchild:
                randomChild2 = random.choice(string.ascii_uppercase)
                if randomChild2 not in childadded:
                    randomGraph[randomChild][randomChild2]=random.randint(1, 10)
                    childadded.append(randomChild2)
        else:
            flag = False
            for i in randomGraph:
                for j in randomGraph[i]:
                    if j not in visited and j not in randomGraph.keys():
                        flag = True
                        visited.append(j)
                        randomGraph[j] = {}
                        childadded = [j]
                        while len(randomGraph[j]) < numberOfchild:
                            randomChild2 = random.choice(string.ascii_uppercase)
                            if randomChild2 not in childadded:
                                childadded.append(randomChild2)
                                randomGraph[j][randomChild2]=random.randint(1, 10)
                        break
                if flag:
                    break
    return randomGraph

#generate random graph with number of parent and number of child from user
def generateRandomGraph():
    numberNode = int(input(('Enter number of node :')))
    numberOfchild = int(input('Enter number of child for each node:'))
    randomGraph={}
    visited=[]
    while len(randomGraph.keys())<numberNode:
            if len(randomGraph.keys())==0:
                randomChild = random.choice(string.ascii_uppercase)
                randomGraph[randomChild] = []
                visited.append(randomChild)
                childadded=[randomChild]
                while len(randomGraph[randomChild]) < numberOfchild:
                    randomChild2 = random.choice(string.ascii_uppercase)
                    if randomChild2 not in childadded :
                        randomGraph[randomChild].append(randomChild2)
                        childadded.append(randomChild2)
            else:
                flag=False
                for i in randomGraph:
                    for j in randomGraph[i]:
                        if j not in visited and j not in randomGraph.keys():
                            flag=True
                            visited.append(j)
                            randomGraph[j]=[]
                            childadded = [j]
                            while len(randomGraph[j]) < numberOfchild:
                                randomChild2 = random.choice(string.ascii_uppercase)
                                if randomChild2 not in childadded:
                                    childadded.append(randomChild2)
                                    randomGraph[j].append(randomChild2)
                            break
                    if flag:
                        break
    return randomGraph

#generate random Gn for graph wihtout Gn
def generateRandomGn(randomGraph):
    graphWithRandomGn = {}
    for i in randomGraph:
        graphWithRandomGn[i] = {}
        for j in randomGraph[i]:
            random_number = random.randint(1, 10)
            graphWithRandomGn[i][j] = random_number
    return graphWithRandomGn

#generate random Hn for graph
def generateRandomHn(randomGraph,end):
    Heuristic={}
    def getPathFromTo(start, end,path=[]):
        path.append(start)
        if start == end:
            for i in path:
                Heuristic[i]=len(path)-path.index(i)-1
        else:
            for i in randomGraph.get(start, {}).keys():
                if i not in path:
                    getPathFromTo(i,end,path)
        path.pop()
    #getPathFromTo(list(randomGraph.keys())[0],end) now work when graph is long beacouse inifinte loop occer prefer stop on random
    for i in randomGraph:
        if i not in Heuristic.keys():
            Heuristic[i]= random.randint(1, 10)
        for j in randomGraph[i]:
            if j not in Heuristic.keys():
                Heuristic[j]=random.randint(1, 10)
    return Heuristic

#to show table as graph and key
def DrawTable(graph):
    print(tabulate(graph, headers='keys',tablefmt="grid"))
# get manual graph
def getManualData():
    graph = {
        'A': {'B': 3, 'C': 5, 'D': 2},
        'B': {'E': 4, 'F': 2, 'G': 1},
        'C': {'H': 3, 'I': 1, 'J': 5, 'D': 1, 'B': 3, 'G': 2},
        'D': {'K': 2, 'L': 4, 'M': 3},
    }
    Hn = {'A': 8, 'B': 6, 'C': 7, 'D': 6, 'E': 5, 'F': 4, 'G':
        3, 'H': 2, 'I': 1, 'J': 5, 'K': 4, 'L': 3, 'M': 2}
    return (graph,Hn)


#generate random graph with shape {(A,B):5 ....etc}
def generateRandomGraphAllAnotherShape():
    numberNode = random.randint(5, 7)#get Random number of parent
    randomGraph = {}
    visited = []
    while len(randomGraph.keys()) < numberNode:
        numberOfchild= random.randint(2, 5) #get random child for each node inside graph
        if len(randomGraph.keys()) == 0:
            randomChild = random.choice(string.ascii_uppercase)
            visited.append(randomChild)
            childadded = [randomChild]
            while len(childadded) < numberOfchild+1:
                randomChild2 = random.choice(string.ascii_uppercase)
                if randomChild2 not in childadded:
                    randomGraph[(randomChild,randomChild2)]=random.randint(1, 10)
                    childadded.append(randomChild2)
        else:
            flag = False
            for j in randomGraph.keys():
                if j[1] not in visited :
                    flag = True
                    visited.append(j[1])
                    childadded = [j[1]]
                    while len(childadded) < numberOfchild+1:
                        randomChild2 = random.choice(string.ascii_uppercase)
                        if randomChild2 not in childadded:
                            childadded.append(randomChild2)
                            randomGraph[(j[1],randomChild2)]=random.randint(1, 10)
                    break
            if flag:
                break
    return randomGraph

# U can see output print(generateRandomGraphAllAnotherShape())
