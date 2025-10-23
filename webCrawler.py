import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
from Graph import Graph
from urllib.parse import urldefrag

class webCrawler():
    def __init__(self, start_url, max_depth=2):
        self.start_url = start_url
        self.max_depth = max_depth
        self.graph = Graph()
        self.visited = set()

    def normalize(self, link):
        link, _ = urldefrag(link)
        return link.rstrip("/")

    def crawl(self):
        #setting up the queeu and the first item in the queue and the first node in the graph that has depth of 0 as its the starting node 
        queue = deque([(self.start_url, 0)])
        self.graph.add_node(self.start_url, 0)

        while(queue):
            url, depth = queue.popleft()
            #checks if we should keep going down by making sure we arent at max depth and that the url we are going to go to hasnt alreadt been visited
            if depth > self.max_depth or url in self.visited:
                continue

            self.visited.add(url)
            node = self.graph.nodes.get(url) or self.graph.add_node(url, depth)

            try:
                response = requests.get(url, timeout=5)
                soup = BeautifulSoup(response.text, 'html.parser')
                if soup.title:
                    node.title = soup.title.string
                else:
                    node.title = 'No Title'

                links = [
                    urljoin(url, a['href'])
                    for a in soup.find_all('a', href=True)
                    ]
            except Exception as e:
                print(f"Skipping {url}: {e}")
                continue
            
            for link in links:
                parsed = urlparse(link)
                if parsed.scheme in ("http", "https"):
                    link = self.normalize(link)
                    self.graph.add_node(link, depth +1)
                    self.graph.add_edge(url, link, depth+1)
                    if link not in self.visited and depth +1 <= self.max_depth:
                        queue.append((link, depth+1))


        print("craw complete " + str(len(self.graph)) + " pages found")
        return self.graph


            



crawler = webCrawler("https://www.geeksforgeeks.org/", max_depth=2)
graph = crawler.crawl()

# Example: Print the first 5 nodes and their links
for i, (url, node) in enumerate(graph.nodes.items()):
    print(url, "->", list(node.links)[:5])
    if i > 5:
        break
