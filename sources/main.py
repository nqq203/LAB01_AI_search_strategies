from graph import Graph
from IOhandle import input_maze
from IOhandle import write_output
from IOhandle import print_output

if __name__ == '__main__':
    adj_list, size, start, goal = input_maze()
    g1 = Graph()
    g2 = Graph()
    g3 = Graph()
    g4 = Graph()
    g5 = Graph()
    g1.create_graph(adj_list)
    g2.create_graph(adj_list)
    g3.create_graph(adj_list)
    g4.create_graph(adj_list)
    g5.create_graph(adj_list)

    bfs = g1.breadth_first_search(start, goal)
    dfs = g2.depth_first_search(start, goal)
    ucs = g3.uniform_cost_search(start, goal)
    gbfs = g4.greedy_best_first_search(start, goal)
    Astar = g5.A_star_search(start, goal)
    
    # print(bfs)
    arg = [bfs, dfs, ucs, gbfs, Astar]
    write_output(arg)
    print_output(arg)
    