import numpy as np
INF = np.Infinity

def floydWarshallForCalculateAllUsedEdges (graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    used_edges = [[True for i in range(len(dist[0]))] for i in range (len(dist[0]))]
    V = len(dist[0])
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF or i==j:
                used_edges[i][j] = False
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist [k][j]:
                    used_edges[i][j] = False
                    dist[i][j] = dist[i][k] + dist [k][j]
    count = 0
    for i in range(V):
        for j in range(V):
            if used_edges[i][j]==True:
                count = count + 1
    return count/2
    #printSolution(dist)
    #printUsedEdges(used_edges)


def get_min(nodes):
    minimum = INF
    index = 0
    for i,node in enumerate(nodes):
        if node[1] < minimum:
            index = i

    return index
    
def Disjkstra (graph,s):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    V = len(dist[0])
    nodes = [[i,INF,[None]] for i in range(V)]
    nodes[s][1]=0
    lista=[[s,0,[None]]]
    while len(lista)>0:
        #current = lista.pop(0)
        current = lista.pop(get_min(lista))
        for i in range(V):
            if i != current[0]:
                if dist[current[0]][i] < INF and nodes[i][1] >= nodes[current[0]][1] + dist[current[0]][i]:
                    if nodes[i][1] == nodes[current[0]][1] + dist[current[0]][i]:
                        nodes[i][1] = nodes[current[0]][1] + dist[current[0]][i]
                        nodes[i][2].append(current[0])
                    else:
                        nodes[i][2] = [current[0]]
                        nodes[i][1] = nodes[current[0]][1] + dist[current[0]][i]
                        lista.append(nodes[i])
    return nodes


def solution1(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    solution_matrix = [[0 for i in range(len(dist[0]))] for i in range (len(dist[0]))] #this is new 
    
    V = len(dist)
    for i in range(V):
        temp = Disjkstra(dist,i)
        for j in range(V):
            used_nodes = [False for i in range (len(dist[0]))]
            pathSeeker(j,temp,used_nodes, i, j, solution_matrix)
    return solution_matrix
    
    
# def pathSeeker (current, nodes, used_edges, left, right, sol):
#     if nodes[current][2].__contains__(None):
#         return
#     else:
#          for i in nodes[current][2]:
#             if not used_edges[i][current]:
#                 #used_edges[current][i] = True 
#                 used_edges[i][current] = True
#                 sol[left][right] += 1
#             pathSeeker(i,nodes,used_edges, left, right, sol)
            
def pathSeeker (current, nodes, used_nodes, left, right, sol):
    if nodes[current][2].__contains__(None):
        return
    else:
         for i in nodes[current][2]:
            sol[left][right] += 1
            if not used_nodes[i]:
                used_nodes[i] = True
                pathSeeker(i,nodes,used_nodes, left, right, sol)


# A utility function to print the solution
def printSolution(dist):
    V = V = len(dist[0])
    for i in range(V):
        for j in range(V):
            if dist[i][j]==INF:
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == V-1:
                print()

# A utility function to print the solution
def printUsedEdges(dist):
    V = V = len(dist[0])
    for i in range(V):
        for j in range(V):
            print("%7d\t" % (dist[i][j]), end=' ')
            if j == V-1:
                print()




def floydWarshall(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    V = len(dist[0])
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist [k][j]:
                    dist[i][j] = dist[i][k] + dist [k][j]
    return dist

def solution2(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    V = len(dist[0])
    fw = floydWarshall(dist)
    used_vertex = [[[] for i in range(V)] for i in range(V)]
    incoming_edges_to_j = [[0 for i in range(V)] for i in range(V)]
    edges_involved = [[0 for i in range(V)] for i in range(V)]
    
    for i in range(V):
        for j in range(V):
            if(i!=j):
                for k in range(V):
                    
                    if fw[i][j] == fw[i][k] + fw[k][j] and k!=i:
                        used_vertex[i][j].append(k)
                    if fw[i][j] == fw[i][k] + dist[k][j] and k!=j:
                        incoming_edges_to_j[i][j] = incoming_edges_to_j[i][j] + 1
            
    for i in range(V):
        for j in range(V):
            for v in used_vertex[i][j]:
                edges_involved[i][j] = edges_involved[i][j] + incoming_edges_to_j[i][v]
                
    return edges_involved
    
    
graph1 = [[0, 5, INF, 10],
		  [5, 0, 3, INF],
		  [INF, 3, 0, 1],
		  [10, INF, 1, 0]
			]

graph2 = [[0, 1, INF, INF,INF],
		  [1, 0, 1, 1,INF],
		  [INF, 1, 0, INF,1],
		  [INF, 1, INF, 0,1],
          [INF,INF,1,1,0]
			]

# a = solution1(graph2)
# b = solution2(graph2)
# printUsedEdges(a)
# print()
# printUsedEdges(b)
