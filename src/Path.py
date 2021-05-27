import math

def createGraph(lst):
    ''' 
    Args:
    lst: A list of tuples of the form [((LowerPoint), (UpperPoint))]
    which represents the list of empty nodes in the octree 

    Returns:
    A Graph in the for of dictionary, such that 
    the key of the dictionary is a node, and its
    values are its neighbours 
    '''
    Graph = dict()

    for i in range(len(lst)):
        if lst[i] not in Graph:
            Graph[lst[i]] = list()
        p1, p2 = lst[i]
        for j in range(i, len(lst)):
            p3, p4 = lst[j]
            if checkNeighbour(p1, p2, p3, p4):
                Graph[lst[i]].append(lst[j])
                if lst[j] not in Graph:
                    Graph[lst[j]] = list()
                Graph[lst[j]].append(lst[i])

    for i in lst:
        if Graph[i] == [] or Graph[i] == None:
            del Graph[i]
    return Graph

def checkNeighbour(p1, p2, p3, p4):

    c1 = ((p2[0]+p1[0])/2, (p2[1]+p1[1])/2 , (p2[2]+p1[2])/2 )
    c2 = ( (p4[0]+p3[0])/2, (p4[1]+p3[1])/2, (p4[2]+p3[2])/2 )

    x1 =  math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2 + (c2[2] - c1[2])**2)
    x2 = math.sqrt((c1[0] - p1[0])**2 + (c1[1] - p1[1])**2 + (c1[2] - p1[2])**2) + math.sqrt((c2[0] - p3[0])**2 + (c2[1] - p3[1])**2 + (c2[2] - p3[2])**2)

    return x1 == x2


def getDistance(p1, p2, p3, p4) -> float:

    c1 = ((p2[0]+p1[0])/2, (p2[1]+p1[1])/2 , (p2[2]+p1[2])/2 )
    c2 = ( (p4[0]+p3[0])/2, (p4[1]+p3[1])/2, (p4[2]+p3[2])/2 )

    x1 =  math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2 + (c2[2] - c1[2])**2)

    return x1

def getDistancePointToRegion(point, region):
    ''' point = (x, y, z)
        region = ((x1, y1, z1), (x2, y2, z2))
    '''

    c = ((region[0][0] + region[1][0])/2 , (region[0][1] + region[1][1])/2, (region[0][2] + region[1][2])/2)

    return math.sqrt( (point[0] - c[0])**2 + (point[1] - c[1])**2 + (point[2] - c[2])**2  )


def getClosestEmptyRegion(Graph, point) -> tuple:
    
    _min = math.inf
    region = None 

    for i in Graph.keys():
        if getDistancePointToRegion(point, i) < _min:
            region = i
            _min = getDistancePointToRegion(point, i)

    return region
'''
def createGraph(lst):

    

    Args:
    lst: A list of tuples of the form [((LowerPoint), (UpperPoint))]
    which represents the list of empty nodes in the octree 

    Returns:
    A Graph in the for of dictionary, such that 
    the key of the dictionary is a node, and its
    values are its neighbours 
    
    Graph = dict()

    for i in range(len(lst)):
        if lst[i] not in Graph:
            Graph[lst[i]] = list()
        p1, p2 = lst[i]
        for j in range(len(lst)):
            p3, p4 = lst[j]
            if checkNeighbour(p1, p2, p3, p4):
                Graph[lst[i]].append(lst[j])
    
    for i in Graph:
        if Graph[i] == [] or Graph[i] == None:
            del Graph[i]
    return Graph
'''

def getEdges(Graph : dict):
    
    edges = list()
    for node in Graph:
        for i in node:
            #edges.append[(node , i , getDistance(node[0], node[1], i[0], i[1]))]
            edges.append((node , i))
            
    return edges 



def FindPath(Graph, StartingPoint, Goal, check ,path) -> list:
    
    check.add(StartingPoint)

    path.append(StartingPoint)

    if StartingPoint == Goal:
        return True 

    for i in Graph[StartingPoint]:
        if i not in check:
            if FindPath(Graph, i, Goal, check, path):
                return True

    path.pop()

    return False

def minNode(Q):
    
    _min = Q[0]
    for i in Q:
        if i[2]< _min[2]:
            _min = i
    return _min

def Q_update(Q,a,b,n):
    
    for i in Q:
        if i[1]==b:
            i[0]=a
            i[2]= n

def FindShortestPath(Graph, start, end):
    
    visited = list()
    d = dict()
    Q = list()
    r = list()

    for i in Graph.keys():
        if start == i:
            d[i]= 0
            Q.append([i,i,0])
        else:
            d[i] = math.inf
            Q.append([None, i, d[i]])

    while Q:
        v = minNode(Q)
        r.append(v)
        visited.append(v[1])
        Q.remove(v)

        for i in Graph[v[1]]:
            if i not in visited:
                if d[v[1]] + getDistance(v[1][0], v[1][1], i[0], i[1]) < d[i]:
                    d[i] = d[v[1]] + getDistance(v[1][0], v[1][1], i[0], i[1])
                    Q_update(Q,v[1],i,d[i])
        
    result = []
    v = end
    while v!=start:
        for i in r:
            if i[1]==v:
                result.insert(0,i[0])
                v = i[0]
    return result




