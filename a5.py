def graph(n,links):
    m = len(links)
    output = [[] for i in range(n)]
    for i in range(m):
        # (weight,vertex)
        output[links[i][0]].append((links[i][2],links[i][1]))
        output[links[i][1]].append((links[i][2],links[i][0]))
    return output
path = []
def pathtaken(parent, source, target):   
    if (target == source):
        path.append(target)
        return 
    pathtaken(parent, source, parent[target])
    path.append(target)
def maxCapacityPath(Graph, source, target):
    check = [-1]*len(Graph)
    max_capacity = [-10**9]*(len(Graph))
    parent = [0]*len(Graph)
    container = []
    container.append((0, source))
    max_capacity[source] = 10**9
    container = sorted(container)
    while (len(container)>0):
        temp = container[-1]
        current_src = temp[1]
        del container[-1]
        if check[current_src]!=0:
            for vertex in Graph[current_src]:
                capacity = max(max_capacity[vertex[1]], min(max_capacity[current_src], vertex[0]))
                if (capacity > max_capacity[vertex[1]]):
                    max_capacity[vertex[1]] = capacity
                    parent[vertex[1]] = current_src
                    container.append((capacity, vertex[1]))
                    container = sorted(container)
            check[current_src]=0
    pathtaken(parent, source, target)
    return max_capacity[target],path
def findMaxCapacity(n,links,s,t):
    global path
    path = []
    grph = graph(n,links)
    output = maxCapacityPath(grph, s, t) 
    return output







