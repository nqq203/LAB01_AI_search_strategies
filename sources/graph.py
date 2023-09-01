from IOhandle import input_maze
from collections import defaultdict
from queue import PriorityQueue
import math

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.explored = []
        self.visited = {}
        self.parent = {}

    def create_graph(self, adj_list):
        for item in adj_list:
            # print(item)
            self.graph[int(item[0])].append(int(item[1]))

    def find_correct_path(self, goal):
        vertex = goal
        path = []
        while vertex is not None: 
            path.append(vertex)
            vertex = self.parent[vertex]
        path.reverse()
        return path

    def manhattan_distance(self, node, goal):
        n = math.sqrt(len(self.graph))
        return int(abs(int(node / n) - int(goal / n)) + abs(node % n - goal % n))
    
    def breadth_first_search(self, start, goal):
        frontier = []
        #set parent's node and state of node are false
        for state in self.graph:
            self.visited[state] = False
            self.parent[state] = None

        #check if start == goal -> return success
        if (start == goal):
            self.explored.append(start)
            return len(self.explored), self.explored, [start]
        
        #set the start node is true
        self.visited[start] = True
        frontier.append(start)
        
        while frontier:
            if (frontier is None):
                return None, None, None
            
            #get the first node in frontier and put it to the explored
            node = frontier.pop(0)
            self.explored.append(node)

            for vertex in self.graph[node]: #get the child node in every parents node
                if not self.visited[vertex]: #check if the node is not in explored
                    self.visited[vertex] = True
                    self.parent[vertex] = node
                    if (vertex == goal):
                        self.explored.append(vertex)
                        return len(self.explored), self.explored, self.find_correct_path(goal)
                    frontier.append(vertex)
        
    def depth_first_search(self, start, goal):
        frontier = []
        for state in self.graph:
            self.visited[state] = False
            self.parent[state] = None

        frontier.append(start)

        #check if the start == goal -> return success
        if (start == goal):
            self.explored.append(start)
            return len(self.explored), self.explored, [start]
        
        while frontier:
            if (frontier is None):
                return None, None, None

            node = frontier.pop(0)
            
            if not self.visited[node]:
                self.visited[node] = True
                self.explored.append(node)
                for vertex in self.graph[node]:
                    if not self.visited[vertex]:
                        self.parent[vertex] = node
                        frontier = [vertex, *frontier]
                    if (vertex == goal):
                        self.explored.append(vertex)
                        return len(self.explored), self.explored, self.find_correct_path(goal)
        
    
    def uniform_cost_search(self, start, goal):      
        #set state and parent node
        for state in self.graph:
            self.visited[state] = False
            self.parent[state] = None
        
        #define frontier with path_cost 
        path_cost = -1
        frontier = PriorityQueue()

        #add the first node to the frontier and set state
        frontier.put(start, path_cost + 1)
        self.visited[start] = True
        
        while not frontier.empty():
            if (frontier is None):
                return None, None, None
            
            node = frontier.get()
            self.explored.append(node) #put the node into the explored

            if (node == goal):
                return len(self.explored), self.explored, self.find_correct_path(goal)
            
            for vertex in self.graph[node]: #frontier use priory queue will help compare the cost
                if not self.visited[vertex]:
                    self.parent[vertex] = node
                    self.visited[vertex] = True
                    frontier.put(vertex, path_cost + 1)
                    path_cost += 1

        
            
    def greedy_best_first_search(self, start, goal):
        frontier = PriorityQueue()
        #set state 
        for state in self.graph:
            self.visited[state] = False    
            self.parent[state] = None    

        #initial first element 
        distance = self.manhattan_distance(start, goal)
        frontier.put(start, distance)
        self.visited[start] = True
        
        while not frontier.empty():
            if (frontier is None):
                return None, None, None
            
            node = frontier.get()
            self.explored.append(node)
            
            if (node == goal):
                return len(self.explored), self.explored, self.find_correct_path(goal)

            for vertex in self.graph[node]:
                if not self.visited[vertex]:
                    self.parent[vertex] = node
                    self.visited[vertex] = True
                    frontier.put(vertex, self.manhattan_distance(vertex, goal))

    def A_star_search(self, start, goal):
        frontier = PriorityQueue()
        #set state 
        for state in self.graph:
            self.visited[state] = False
            self.parent[state] = None

        #initial first element 
        distance = self.manhattan_distance(start, goal)
        frontier.put(start, distance)
        self.visited[start] = True

        while not frontier.empty():
            if (frontier is None):
                return None, None, None

            node = frontier.get()
            self.explored.append(node)
            
            if (node == goal):
                return len(self.explored), self.explored, self.find_correct_path(goal)
            
            for vertex in self.graph[node]:
                h_node = self.manhattan_distance(node, goal)
                h_vertex = self.manhattan_distance(vertex, goal)
                if not self.visited[vertex]:
                    self.parent[vertex] = node
                    self.visited[vertex] = True
                    frontier.put(vertex, distance - h_node + h_vertex + 1)

