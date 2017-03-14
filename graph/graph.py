from example import G,G_dir

class Graph:
    def __init__(self,G):
        self.G = G
        self.visited = dict()
        self.traversal = []
        self.init_visited()
        #print self.visited

    def init_visited(self):
        for key in self.G.keys():
            self.visited[key] = False
 
    def dfs(self):
        for key in self.G.keys():
            if not self.visited[key]:
                self.explore(key)

    def explore(self,key):
        self.visited[key] = True
        self.traversal.append(key)
        neighbors = self.G[key]
        for n in neighbors:
            if not self.visited[n]:
                self.explore(n)
