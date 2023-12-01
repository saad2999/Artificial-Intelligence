import heapq

class Node:
    def __init__(self, position, cost=0, heuristic=0, parent=None):
        self.position = position
        self.cost = cost
        self.heuristic = heuristic
        self.parent = parent

    def __lt__(self, other):
        return self.heuristic < other.heuristic

def best_first_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def heuristic(node):
        return abs(node.position[0] - goal[0]) + abs(node.position[1] - goal[1])

    open_set = [Node(start, heuristic=heuristic(Node(start)))]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.position == goal:
            path = []
            while current_node:
                path.insert(0, current_node.position)
                current_node = current_node.parent
            return path

        closed_set.add(current_node.position)

        for direction in directions:
            new_x, new_y = current_node.position[0] + direction[0], current_node.position[1] + direction[1]

            if not is_valid(new_x, new_y) or grid[new_x][new_y] == 1 or (new_x, new_y) in closed_set:
                continue

            new_node = Node((new_x, new_y), current_node.cost + 1, heuristic=heuristic(Node((new_x, new_y))), parent=current_node)
            heapq.heappush(open_set, new_node)

    return None  # No path found

# Example usage:
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = best_first_search(grid, start, goal)
print(path)
