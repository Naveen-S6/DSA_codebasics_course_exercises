class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.dic = {}

        for node, end in self.edges:
            if node in self.dic:
                self.dic[node].append(end)
            else:
                self.dic[node] = [end]
        import pprint
        print("The routes in dictonary format")
        pprint.pprint(self.dic)

    def get_paths(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.dic:
            return []
        paths = []
        for node in self.dic[start]:
            if node not in path:
                new_paths = self.get_paths(node,end,path)
                for i in new_paths:
                    paths.append(i)

        return paths

    def get_shortest_path(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.dic:
            return None
        shortest_path = None
        for node in self.dic[start]:
            if node not in path:
                sp = self.get_shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

    def get_longest_path(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.dic:
            return None
        longest_path = None
        for node in self.dic[start]:
            if node not in path:
                lp = self.get_longest_path(node,end,path)
                if lp:
                    if longest_path is None or len(lp) > len(longest_path):
                        longest_path = lp

        return longest_path

if __name__ == "__main__":
    routes = [("Vellore","Chennai"),("Vellore","Bangalore"),("Chennai","Bangalore"),("Chennai","Mumbai"),
              ("Chennai","Delhi"),("Bangalore","Mumabi"),("Bangalore","Delhi"),("Mumabi","Delhi"),("Madurai","Chennai")]

    route_graph = Graph(routes)
    start = "Vellore"
    end = "Delhi"
    print(f"Shortest route possible from {start} to {end}:",route_graph.get_shortest_path(start,end))
    print(f"Longest route possible from {start} to {end}:", route_graph.get_longest_path(start, end))
