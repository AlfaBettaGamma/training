class Vertex:    def __init__(self, val):        self.Value = val        self.Hit = Falseclass SimpleGraph:    def __init__(self, size):        self.max_vertex = size        self.m_adjacency = [[0] * size for _ in range(size)]        self.vertex = [None] * size    def AddVertex(self, v):        # ваш код добавления новой вершины        # с значением value        # в свободное место массива vertex        for idx in range(self.vertex.__len__()):            if self.vertex[idx] is None:                self.vertex[idx] = Vertex(v)                break    # здесь и далее, параметры v -- индекс вершины    # в списке  vertex    def RemoveVertex(self, v):        # ваш код удаления вершины со всеми её рёбрами        assert v <= self.max_vertex - 1        self.vertex[v] = None        for i in range(self.max_vertex):            if i == v:                pass            else:                self.RemoveEdge(v, i)        self.m_adjacency[v] = [0] * self.max_vertex    def IsEdge(self, v1, v2):        # True если есть ребро между вершинами v1 и v2        if self.m_adjacency[v1][v2] == 1:            return True        return False    def AddEdge(self, v1, v2):        # добавление ребра между вершинами v1 и v2        if self.vertex[v1] is not None and self.vertex[v2] is not None:            self.m_adjacency[v1][v2] = 1            self.m_adjacency[v2][v1] = 1    def RemoveEdge(self, v1, v2):        # удаление ребра между вершинами v1 и v2        self.m_adjacency[v1][v2] = 0        self.m_adjacency[v2][v1] = 0    def PrintAllAdjacency(self):        print('Vertext:')        for vert in self.vertex:            if vert != None:                print(vert.Value,' ', end ='')            else:                print('None ', end='')        print()        print('m_adjacency:')        for i in self.m_adjacency:            for j in i:                print ("{:4d}".format(j), end ="")            print()    def BreadthFirstSearch(self, VFrom, VTo):        if self.vertex[VFrom] is None or self.vertex[VTo] is None:            return []        for v in self.vertex:            if v is not None:                v.Hit = False        queue = []        path = {}        x = VFrom        self.vertex[x].Hit = True        path[x] = [x]        while True:            if self.IsEdge(x, VTo):                p = path[x].copy()                p.append(VTo)                path[VTo] = p                path.pop(x)                break            adj_found = False            for i in range(self.max_vertex):                if self.IsEdge(x, i) and not self.vertex[i].Hit:                    adj_found = True                    self.vertex[i].Hit = True                    queue.append(i)                    p = path[x].copy()                    p.append(i)                    path[i] = p            if adj_found:                path.pop(x)            if len(queue) == 0:                return []            else:                x = queue.pop(0)        vertex_path = []        for i in path[VTo]:            vertex_path.append(self.vertex[i])        return vertex_pathmy_graph = SimpleGraph(9)my_graph.AddVertex('A')my_graph.AddVertex('B')my_graph.AddVertex('C')my_graph.AddVertex('D')my_graph.AddVertex('E')my_graph.AddVertex('F')my_graph.AddVertex('G')my_graph.AddVertex('H')my_graph.AddVertex('I')my_graph.AddEdge(0,6)my_graph.AddEdge(6,0)my_graph.AddEdge(6,7)my_graph.AddEdge(7,6)my_graph.AddEdge(6,3)my_graph.AddEdge(3,6)my_graph.AddEdge(3,4)my_graph.AddEdge(4,3)my_graph.AddEdge(0,8)my_graph.AddEdge(8,0)my_graph.AddEdge(8,5)my_graph.AddEdge(8,2)my_graph.AddEdge(2,8)my_graph.AddEdge(2,1)my_graph.AddEdge(1,2)#my_graph.RemoveEdge(0, 3)#my_graph.RemoveEdge(3, 1)my_graph.PrintAllAdjacency()path = my_graph.BreadthFirstSearch(4,1)for item in path:    print(item.Value, ' ', end='')#print()