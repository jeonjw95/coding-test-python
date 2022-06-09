import sys


class Graph:
    def __init__(self):
        self.vertex_list = []  # vertex 객체를 선형으로 저장
        self.edge_list = []  # edge 객체를 선형으로 저장

    def insert_vertex(self, v):
        self.vertex_list.append(Vertex(v))

    def insert_edge(self, d1, d2):
        v1 = self.find_vertex(d1)
        v2 = self.find_vertex(d2)
        edge = Edge(v1, v2)
        self.edge_list.append(edge)
        v1.add_incidence(edge)
        v2.add_incidence(edge)

    def find_vertex(self, v):
        for ele in self.vertex_list:
            if v == ele.get_data():
                return ele


class Vertex:
    def __init__(self, data):
        self.data = data
        self.incidence_list = []

    def add_incidence(self, edge):
        self.incidence_list.append(edge)
        self.incidence_list = sorted(self.incidence_list, key=lambda x: x.get_opposite(self).get_data())

    def get_data(self):
        return self.data

    def get_incidence(self):
        return self.incidence_list

    # def delete_incidence:

    # def delete_all_incidence:


class Edge:
    def __init__(self, v1, v2):
        self.vertex = []
        if v1.get_data() > v2.get_data():
            self.vertex.append(v2)
            self.vertex.append(v1)
        else:
            self.vertex.append(v1)
            self.vertex.append(v2)

    def get_opposite(self, v):
        if v == self.vertex[0]:
            return self.vertex[1]
        else:
            return self.vertex[0]


n, m, first = map(int, sys.stdin.readline().strip().split(' '))

graph = Graph()

for i in range(n):
    graph.insert_vertex(i+1)

for _ in range(m):
    ver1, ver2 = map(int, sys.stdin.readline().strip().split(' '))
    graph.insert_edge(ver1, ver2)

visited_dfs = []
seq_dfs = []


def dfs(ver):
    seq_dfs.append(str(ver.get_data()))
    visited_dfs.append(ver)
    for e in ver.get_incidence():
        opp = e.get_opposite(ver)
        if opp in visited_dfs:
            continue
        else:
            dfs(opp)


visited_bfs = []
seq_bfs = []


def bfs(ver):
    visited_bfs.append(ver)
    seq_bfs.append(str(ver.get_data()))
    level_list = [[ver]]
    index = 0

    while len(level_list[index]):
        level_i = []
        for top in level_list[index]:
            for bottom in top.get_incidence():
                opp = bottom.get_opposite(top)
                if opp not in visited_bfs:
                    seq_bfs.append(str(opp.get_data()))
                    visited_bfs.append(opp)
                    level_i.append(opp)
        level_list.append(level_i)
        index += 1


first_vertex = graph.find_vertex(first)
dfs(first_vertex)
bfs(first_vertex)

#for i in first_vertex.get_incidence():
#    print(i.vertex[0].get_data(), i.vertex[1].get_data())

print(" ".join(seq_dfs))
print(" ".join(seq_bfs))
