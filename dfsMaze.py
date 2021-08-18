
# Node class
class Node:
    # Constructor
    def __init__(self, pos:(), parent:()):
        self.pos = pos
        self.parent = parent
    # Node Comaprision
    def __eq__(self, other):
        return self.pos == other.pos

# Write Characters to displaa the final output
def writeChars(dict, w, h, **kwargs):
    for b in range(h):
        for a in range(w):
            print(draw(dict, (a, b), kwargs), end='')
        print()

#Write Chars
def draw(dict, pos, kwargs):
    # Get the dict value(associated character)
    value = dict.get(pos)
    # Check if we should print the path, else print value associated in dict 
    if 'path' in kwargs and pos in kwargs['path']: value = '+'
    if 'goal' in kwargs and pos == kwargs['goal']: value = '.'
    return value 

# Depth First Search
def DFS(dict, start, goal):
    
    # nonVisited and visited cords 
    # Implementation of Stack Using List
    nonVisited = []
    visited = []
    # Create a start node and an goal node
    startNode = Node(start, None)
    goalNode = Node(goal, None)
    nonVisited.append(startNode)
    path = []

    # Loop until the nonVisited list is empty
    while len(nonVisited) > 0:
        # Get the Last inserted node(LIFO Implementation)
        currentNode = nonVisited.pop(-1)
        # Add the current node to the visited list
        visited.append(currentNode)
        
        # If we are at destination
        if currentNode == goalNode:
            while currentNode != startNode:
                path.append(currentNode.pos)
                currentNode = currentNode.parent
            return path

        (a, b) = currentNode.pos
        # Get closestNodes
        closestNodes = [(a-1, b), (a, b+1), (a+1, b), (a, b-1) ]
        # Loop closestNodes
        for node in closestNodes:
            # Get value from dict
            charVal = dict.get(node)
            # if node is wall
            if(charVal == '%'):
                continue
            # Create a new node
            closest = Node(node, currentNode)
            # if node is already visited
            if(closest in visited):
                continue
            #if node is not visted
            if (closest not in nonVisited):
                nonVisited.append(closest)
    # Return None
    return path

# Entry Point
def main():
    #dictionary to store cordinates and associated chars as key:value respectively
    dict = {}
    start,goal = None, None
    width,height = 0, 0
    CharArr = [] 
    hasMoreLine = True

    #take Input from User to read File
    print()
    print("Press 'A' to run code using tinyMaze.txt")
    print()
    print("Press 'B' to run code using mediumMaze.txt")
    print()
    print("Press 'C' to run code using bigMaze.txt")
    print()
    charsForFile = input("Enter Character 'A' or 'B' or 'C': ")
    print()
    FiletoRead=''
    if(charsForFile=="A" or charsForFile=="a"):
        FiletoRead = 'tinyMaze.txt'
    elif(charsForFile=="B" or charsForFile=="b"):
        FiletoRead = 'mediumMaze.txt'
    elif(charsForFile=="C" or charsForFile=="c"):
        FiletoRead = 'bigMaze.txt'            
    else:
        print("By defgault it will use tinyMaze.txt file") 
        FiletoRead = 'tinyMaze.txt'
    # Open a file to read chars
    file = open(FiletoRead, 'r')

    # Read till last line
    while hasMoreLine:
        # Get chars of single line and add it to CharArr    
        CharArr = [str(i) for i in file.readline().strip()]
        width = len(CharArr) if width == 0 else width
        if len(CharArr)==0:
            hasMoreLine = False    
        # Add chars to dict
        for k in range(len(CharArr)):
            dict[(k, height)] = CharArr[k]
            if(CharArr[k] == 'P'):
                start = (k, height)
            elif(CharArr[k] == '.'):
                goal = (k, height)
        
        # increment in heigh of dict
        if(len(CharArr) > 0):
            height += 1
        
    # Close File
    file.close()
    # Finding path using DFS for pacman
    path = DFS(dict, start, goal)
    print()
    writeChars(dict, width, height,path=path,goal=goal)
    print()
    
# To run main metod
if __name__ == "__main__": main()
