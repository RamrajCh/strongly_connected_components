""" Kosaraju's Algorithm for finding strongly connected components """

from kosaraju import *
from graph import *


G = DiGraph()

a = Vertex('Ram')
b = Vertex('Shyam')
c = Vertex('Parbati')
d = Vertex('Arjun')
e = Vertex('Raj')
f = Vertex('Bishal')
g = Vertex('Gupta')
h = Vertex('Maya')
i = Vertex('Ramina')
j = Vertex('Saugat')
k = Vertex('Gaurav')
l = Vertex('Pinky')
m = Vertex('Rojina')
n = Vertex('Yash')
o = Vertex('Dory')
p = Vertex('Krishna')
q = Vertex('Ozy')
r = Vertex('Di')

G.add_vertices([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r])

G.add_edge(a,e)
G.add_edge(b,a)
G.add_edge(b,c)
G.add_edge(b,f)
G.add_edge(c,d)
G.add_edge(e,b)
G.add_edge(e,h)
G.add_edge(f,c)
G.add_edge(g,f)
G.add_edge(g,j)
G.add_edge(h,e)
G.add_edge(h,i)
G.add_edge(i,f)
G.add_edge(i,h)
G.add_edge(j,i)
G.add_edge(j,m)
G.add_edge(k,j)
G.add_edge(l,i)
G.add_edge(m,j)
G.add_edge(m,q)
G.add_edge(n,j)
G.add_edge(o,a)
G.add_edge(p,q)
G.add_edge(q,n)
G.add_edge(q,p)
G.add_edge(q,r)
G.add_edge(r,k)
G.add_edge(g,l)
G.add_edge(l,g)

print("*"*20+" Adjacency List Graph Representation "+"*"*20)
print(G)

y = kosaraju(G)

print("*"*20+" Strongly Connected Components "+"*"*20)
for j in range(len(y)):
    if y[j] != []:
        print("Component:", j+1, " ", end=" ")
        for v in y[j]:
            print(v.value, end=" ")
        print()