import numpy as np

testarr = np.loadtxt("kosarajuTest6.txt").tolist()

temp = []
for edge in testarr:
    temp.extend(edge)
curLabel= len(list(set(temp)))

isexplored = {}
dist = {}
scc = {}
numSCC = 0

def Toposort(dag):
    for edge in dag:
        v = edge[0]
        if isexplored.get(v) is None:
            DFS_Topo(dag, v)


def DFS_Topo(dag, s):
    global curLabel
    isexplored[s] = 1
    for edge in dag:
        if edge[0] == s:
            v = edge[1]
            if isexplored.get(v) is None:
                DFS_Topo(dag, v)
    dist[s] = curLabel
    curLabel -= 1


def DFS_SCC(dag, s):
    isexplored[s] = 1
    scc[s] = numSCC
    for edge in dag:
        if edge[0] == s:
            v = edge[1]
            if isexplored.get(v) is None:
                DFS_SCC(dag, v)


def Kosaraju(dag):
    rev_dag = [[edge[1], edge[0]] for edge in dag]
    Toposort(rev_dag)
    global isexplored
    isexplored = {}
    global numSCC
    global dist
    dist = dict(sorted(dist.items(), key=lambda item: item[1]))
    for key in dist.keys():
        if isexplored.get(key) is None:
            numSCC += 1
            DFS_SCC(dag, key)


Kosaraju(testarr)
print(scc)
