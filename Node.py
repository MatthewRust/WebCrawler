class Node:

    def __init__(self, url, depth=0):
        self.url = url
        self.depth = depth
        self.links = set()

    def __repr__(self):
        return f"<Node {self.url} (depth={self.depth})>"
    
    def get_depth(self):
        return self.depth
    
    def get_url(self):
        return self.url
    
    def get_links(self):
        return self.links
    
    def set_depth(self,depth):
        self.depth = depth
        
    def set_url(self,url):
        self.url = url

    def set_links(self, links):
        self.links = links