import sys


class Graph:
    def __init__(self):
        self.vertex_list = []  # vertex 객체를 선형으로 저장
        self.edge_list = []  # edge 객체를 선형으로 저장

    def insert_vertex(self, v):
        self.vertex_list.append(Vertex(v))

    def insert_edge(self, d1, d2, weight):
        v1 = self.find_vertex(d1)
        v2 = self.find_vertex(d2)
        edge = Edge(v1, v2, weight)
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
        # self.incidence_list = sorted(self.incidence_list, key=lambda x: x.get_opposite(self).get_data())

    def get_data(self):
        return self.data

    def get_incidence(self):
        return self.incidence_list

    # def delete_incidence:

    # def delete_all_incidence:


class Edge:
    def __init__(self, v1, v2, weight):
        self.vertex = []
        self.weight = weight
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


n, m = map(int, sys.stdin.readline().strip().split(' '))


def get_parent(union_list, x):
    if union_list[x] == x:
        return x
    else:
        union_list[x] = get_parent(union_list, union_list[x])
        return union_list[x]


def union_parent(union_list, a, b):
    a = get_parent(union_list, a)
    b = get_parent(union_list, b)
    if a > b :
        union_list[a] = b
    else:
        union_list[b] = a


def find_parent(union_list, a, b):
    a = get_parent(union_list, a)
    b = get_parent(union_list, b)

    if a == b:
        return True
    else:
        return False



def kruskal():
    union_list = [i for i in range(0, n + 1)]  # index 0은 사용안함
    minimum_weight = 0
    parents = []
    sorted_weight = sorted(graph.edge_list, key=lambda x: x.weight)
    for edge in sorted_weight:
        v1 = edge.vertex[0].get_data()
        v2 = edge.vertex[1].get_data()
        if not find_parent(union_list, v1, v2):
            union_parent(union_list, v1, v2)
            minimum_weight += edge.weight
    return minimum_weight


def prim(first, n):
    union_list = [i for i in range(0, n + 1)]  # index 0은 사용안함
    incident_edges = sorted(first.get_incidence(), key=lambda x: x.weight)
    minimum_weight = 0
    edge_cnt = 0
    while edge_cnt != n-1:
        for edge in incident_edges:
            v1 = edge.vertex[0].get_data()
            v2 = edge.vertex[1].get_data()
            if not find_parent(union_list, v1, v2):
                union_parent(union_list, v1, v2)
                edge_cnt += 1
                minimum_weight += edge.weight
                for inci in edge.vertex[0].get_incidence() + edge.vertex[1].get_incidence():
                    if inci not in incident_edges:
                        incident_edges.append(inci)
                incident_edges.remove(edge)
                incident_edges = sorted(incident_edges, key=lambda x: x.weight)
                break
            else:
                incident_edges.remove(edge)
    return minimum_weight





graph = Graph()
first_vertex = None
for i in range(n):
    graph.insert_vertex(i+1)

for i in range(m):
    ver1, ver2, weight = map(int, sys.stdin.readline().strip().split(' '))
    graph.insert_edge(ver1, ver2, weight)


print(prim(graph.find_vertex(1), n))

#for i in first_vertex.get_incidence():
#    print(i.vertex[0].get_data(), i.vertex[1].get_data())