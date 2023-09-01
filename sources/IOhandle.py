#handle input
def input_maze():
    adjacency_list = []
    size = int()
    goal = int()
    start = int()
    with open('../input/input.txt', 'r') as read_file:
        index = 0
        for line in read_file:
            if (index == 0):
                size = int(line)
            elif (index == 1):
                start = int(line.split()[0])
                goal = int(line.split()[1])
            else:
                adjacency_list.append(line.split())
            index += 1
        return adjacency_list, size, start, goal
    
#handle output
def write_output(arg):
    with open ("../output/output.txt", "w") as write_file:
        name = str()
        write_file.write("                          TEST MAZE\n\n\n")
        for index in range(5):
            if (index == 0):
                name = "Breadth-first Search"
            elif (index == 1):
                name = "Depth-first Search"
            elif (index == 2):
                name = "Uniform Cost Search"
            elif (index == 3):
                name = "Greedy Best First Search"
            else:
                name = "Graph search A*"
            time_maze, explored, path_found = arg[index]
            write_file.write("                --------" + name + "-------\n")
            write_file.write("The time escape: " + str(time_maze) + "\n")
            write_file.write("List of nodes explored: " + str(explored) + "\n")
            write_file.write("Path found.: " + str(path_found) + "\n\n")

#print the output to console
def print_output(arg):
    name = str()
    print("                          TEST MAZE\n\n\n")
    for index in range(5):
        if (index == 0):
            name = "Breadth-first Search"
        elif (index == 1):
            name = "Depth-first Search"
        elif (index == 2):
            name = "Uniform Cost Search"
        elif (index == 3):
            name = "Greedy Best First Search"
        else:
            name = "Graph search A*"
        time_maze, explored, path_found = arg[index]
        print("                --------" + name + "-------\n")
        print("The time escape: " + str(time_maze) + "\n")
        print("List of nodes explored: " + str(explored) + "\n")
        print("Path found.: " + str(path_found) + "\n\n")