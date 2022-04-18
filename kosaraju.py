time = 0
def dfs_visit(G, s, parent, stack):
    """ Recursively explore all childrens of s """
    global time
    time += 1
    s.d = time

    for v in G.adj[s]:
        if v not in parent:
            parent[v] = s
            dfs_visit(G, v, parent, stack)

    time += 1
    s.f = time
    stack.append(s)


def dfs(G, stack):
    """ Explore the whole graph using Depth First Search """
    parent = {}
    stack = []

    for vertex in list(G.adj.keys()):
        if vertex not in parent:
            parent[vertex] = None
            dfs_visit(G, vertex, parent, stack)

    return stack


def dfs_single_visit(adj_list, v, visited, stack):
    """ Recursively visits all the children of v """
    for u in adj_list[v]:
        if u not in visited:
            visited[u] = v
            dfs_single_visit(adj_list, u, visited, stack)
    stack.append(v)

def kosaraju(G):    
    """ Kosaraju's Algorithm for finding strongly connected components. """
    # get vertices based on their finishing time in decreasing order
    stack = dfs(G, [])
    
    # Reverse edges of the graph G
    rev_adj = {}

    for vertex in G.adj.keys():
        rev_adj[vertex] = {}

    for vertex in G.adj.keys():
        for u in G.adj[vertex]:
            rev_adj[u][vertex] = True


    # Traverse graph by popping vertices out from the stack
    visited = {}
    components = []
    i = 0

    while stack != []:
        v = stack.pop()
        # if v is already visited skip iteration
        if v in visited:
            continue
        # otherwise find all the vertices it can reach and put them into components
        else:
            components.append([])
            if v not in visited:
                visited[v] = True
                dfs_single_visit(rev_adj, v, visited, components[i])
            
            components.append([])
            i += 1
    
    return components