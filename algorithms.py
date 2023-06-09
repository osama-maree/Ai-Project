
#contain search algorithms DFS,BFS,UCS,Hill Climbing,Beam Search,A*
from generator import  DrawTable
import heapq

def DFS(graph,goal):
    root = list(graph.keys())[0]
    stack, temp, path, visited = [root], [], [], []
    parent = {root: None}
    while stack:
        v = stack.pop()
        visited.append(v)
        if v == goal:
            cost=0
            while parent[goal]:
                path.insert(0, goal)
                cost+=graph[parent[goal]][goal]
                goal = parent[goal]
            path.insert(0, root)
            return (path,visited,cost)
        for i in graph.get(v,{}).keys():
            if i not in visited:
                temp.append(i)
                parent[i] = v
        while temp:
            stack.append(temp.pop())
    return ('invaild goal','invalid goal','---')

def iterativeDeepSearch(graph,goal,limit):
    root = list(graph.keys())[0]
    stack, temp, path, visited = [(root,1)], [], [], []
    parent = {root: None}
    while stack:
        v,d = stack.pop()
        visited.append(v)
        if v == goal:
            cost=0
            while parent[goal]:
                path.insert(0, goal)
                cost+=graph[parent[goal]][goal]
                goal = parent[goal]
            path.insert(0, root)
            return (path,visited,cost)
        for i in graph.get(v,{}).keys():
            if i not in visited and d < limit:
                 temp.append(i)
                 parent[i] = v
        while temp:
            stack.append((temp.pop(),d+1))
    return ('cant arrive','cant arrive','---')

def depthLimitedSearch(graph,goal,limit):
    root = list(graph.keys())[0]
    stack, temp, path, visited = [(root,1)], [], [], []
    parent = {root: None}
    while stack:
        v,d = stack.pop()
        visited.append(v)
        if v == goal:
            cost=0
            while parent[goal]:
                cost += graph[parent[goal]][goal]
                path.insert(0, goal)
                goal = parent[goal]
            path.insert(0, root)
            return (path,visited,cost)

        for i in graph.get(v,{}):
            if i not in visited and d < limit:
                 temp.append(i)
                 parent[i] = v
        while temp:
            stack.append((temp.pop(),d+1))
    return ('cant arrive','cant arrive','---')
def BFS(graph,goal):
    root = list(graph.keys())[0]
    queue, temp, path, visited = [root], [], [], []
    parent = {root: None}
    while queue:
        v = queue.pop(0)
        if v in visited:
            continue
        visited.append(v)
        if v == goal:
            cost=0
            while parent[goal]:
                cost+=graph[parent[goal]][goal]
                path.insert(0, goal)
                goal = parent[goal]
            path.insert(0, root)
            return (path,visited,cost)
        for i in graph.get(v,{}).keys():
                 queue.append(i)
                 parent[i] = v
    return ('invaild goal','invalid goal','---')
def uniformCostSearch(graph,goal):
    visited =[]
    start=list(graph.keys())[0]
    priorityQueue = [(0, start, [])]
    while priorityQueue:
        (cost, node, x) = heapq.heappop(priorityQueue)#return path has smallest cost
        path=list(x)
        if node not in visited:
            visited.append(node)
            path.append(node)
            if node == goal:
                return (path,visited,cost)
            for i in graph.get(node,[]):
                if i not in visited:
                    total_cost = cost + graph[node][i]
                    heapq.heappush(priorityQueue,(total_cost, i, path))
    return ('invaild gola','invalid goal','---')

def Hill_Climbing(graph,heuristic,goal):
    start=list(graph.keys())[0]
    path,PrevNode=[(start,heuristic[start])],[heuristic[start],start]
    cost=0
    while 1:
       child=graph.get(start,[])
       PQ=[]
       if child:
           for i in child.keys():
               PQ=PQ+[(heuristic[i],i)]
           PQ.sort()
           (H,node)=PQ.pop(0)
           if H <= PrevNode[0]:
               cost+=graph[start][node]
               path=path+[(node,heuristic[node])]
               if goal == node:
                   visited=[i for (i,c) in path]
                   return (path,visited,cost)
               PrevNode=[H,node]
               start=node
           else:
               visited = [i for (i, c) in path]
               return (path,visited,'---')
       else:
           visited = [i for (i, c) in path]
           return (path,visited,'---')

def BeamSearch(graph,goal,heuristic,n):
    start=list(graph.keys())[0]
    queue=[[(start,heuristic[start],0)]]
    visited=[]
    while queue:
        path=queue.pop(0)
        node=path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            cost=0
            for i in path:
                cost+=i[2]
            return (path,visited,cost)
        else:
            PQ=[]
            for i in graph.get(node,{}).keys():
                pathnode=path + [(i,heuristic[i],graph[node][i])]
                PQ.append(pathnode)
            PQ.sort(key=lambda x:heuristic[x[-1][0]])
            for i in range(n):
                if PQ:
                   queue.append(PQ.pop(0))
                else:
                    break
        queue.sort(key=lambda x:heuristic[x[-1][0]])
    return ('invalid goal','invalid goal','---')

def greedySearch(graph,goal,heuristic):
    start=list(graph.keys())[0]
    queue=[[(start,heuristic[start],0)]]
    visited=[]
    while queue:
        path=queue.pop(0)
        node=path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            cost=0
            for i in path:
                cost+=i[2]
            return (path,visited,cost)
        else:
            for i in graph.get(node,{}).keys():
                pathnode=path + [(i,heuristic[i],graph[node][i])]
                queue.append(pathnode)
        queue.sort(key=lambda x:heuristic[x[-1][0]])
    return ('invalid goal','invalid goal','---')


#this function mySmation for sum the G(n) in A* U can see code inside AStacrSearch
def mySumation(path):
    Gn=0
    for (i,cost)in path:
        Gn+=cost
    return Gn
def AStarSearch(graph,goal,Heuristic):
    start=list(graph.keys())[0]
    queue=[[(start,0)]]
    visited=[]
    while queue:
        path=queue.pop(0)
        node=path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            Gn = 0
            for (i, cost) in path:
                Gn += cost
            return (path,visited,Gn)
        else:
            Child=graph.get(node,[])
            for i in Child:
                pathnode=path + [(i,Child[i])]
                queue.append(pathnode)
        queue.sort(key =lambda x: Heuristic[x[-1][0]] + mySumation(x))
    return ('invalid goal','invalid gola','---')

#solution for project with print table
def Solution(graph,Hn,goal,n,l):
    #uniformed Search
    pathDFS,visitedDFS,costDFS= DFS(graph,goal)
    pathDLS,visitedDLS,costDLS=depthLimitedSearch(graph,goal,l)
    pathBFS,visitedBFS,costBFS = BFS(graph,goal)
    pathUCS,visitedUCS,costUCS= uniformCostSearch(graph,goal)
    #Informed Search
    pathHC,visitedHC,costHC=Hill_Climbing(graph,Hn,goal)
    pathBS,visitedBS,costBS=BeamSearch(graph,goal,Hn,n)
    pathGS,visitedGS,coastGS=greedySearch(graph,goal,Hn)
    pathAS,visitedAS,costAS=AStarSearch(graph,goal,Hn)

    table={
    'Algorithms':['DFS','DLS','BFS','UCS','Hill Climbing','Beam Search','Greedy Search','A*'],
    'path(Solution)':[pathDFS,pathDLS,pathBFS,pathUCS,pathHC,pathBS,pathGS,pathAS],
    'Visited':[visitedDFS,visitedDLS,visitedBFS,visitedUCS,visitedHC,visitedBS,visitedGS,visitedAS],
    'Actaul Cost G(n)':[costDFS,costDLS,costBFS,costUCS,costHC,costBS,coastGS,costAS],
    }
    DrawTable(table)


