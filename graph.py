class Vertex:
    """ A vertex of the graph. """

    def __init__(self, value):
        self.value = value
        self.d = None
        self.f = None


class DiGraph:
    """ A simple Directed graph """

    def __init__(self): 
        self.adj = {}

    def has_vertex(self, v):
        """ Returns True if graph has vertex v """
        try:
            self.adj[v]
            return True
        except KeyError:
            return False

    def add_vertex(self, v):
        """ Adds vertex v into the graph if not already present """
        if self.has_vertex(v):
            return False
        else:
            self.adj[v] = {}
            return True
    
    def add_vertices(self, arr):
        """ Adds the vertices in arr into graph """
        for v in arr:
            self.add_vertex(v)
        return True

    def has_edge(self, start, end): 
        """ Returns True if there is an edge between start and end """
        if self.has_vertex(start) and self.has_vertex(end):
            try:
                if self.adj[start][end] is True:
                    return True
                return False
            except KeyError:
                return False
        return False

    def add_edge(self, start, end):
        """ Adds a directed edge from start to end """
        if self.has_vertex(start) and self.has_vertex(end):
            self.adj[start][end] = True
            return True
        return False

    def __str__(self):
        """ Return Adjacency List representation as str """
        str = ''
        for key, value in self.adj.items():
            str += key.value
            if value:
                for v in value.keys():
                    str += ' -> ' + v.value
            str += '\n'
        return str