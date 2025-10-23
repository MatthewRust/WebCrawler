from Node import Node
class Graph:
    def __init__(self):
        self.nodes = {} #dic for the nodes

    def add_node(self, url, depth=0):
        #Checks if the url is already in the dic of nodes if not add it
        if url not in self.nodes:
            self.nodes[url] = Node(url, depth)
        return self.nodes[url]
    
    def add_edge(self, from_url, to_url, depth=0):
        #Adds and edge from the from_url to the to_url making a link between two new sites 
        from_node = Node(from_url)
        to_node = self.add_node(to_url, depth if depth is not None else getattr(from_node, "depth", 0) + 1)

        if not hasattr(from_node, "links"):
            from_node.links = []
        from_node.links.add(to_node.url if hasattr(to_node, "url") else to_url)


    def __len__(self):
        return len(self.nodes)
    


graph = Graph()
