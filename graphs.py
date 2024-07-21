class Graph:
    def __init__(self, edges):

        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]        


    def get_paths(self, start, end):
            path = start
            if start == end:
                 return [path]
            for i in self.edges[1]:
                pass

        




if __name__ == '__main__':
    routes = [
        ("Durres", "Tirane"),
        ("Durres", "Dhermi"),
        ("Tirane", "Dhermi"),
        ("Tirane", "Theth"),
        ("Dhermi", "Theth"),
        ("Theth", "Valbone"),
    ]
    graph = Graph(routes)