from collections import deque

def find_path(grid, start, goal):
    queue = deque()
    queue.append(start)
    parent = {}
    visited = set()
    visited.add(start)
    while queue:
        current = queue.popleft()
        if current == goal:
            break
        row, col = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            new_pos = (new_row, new_col)
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and new_pos not in visited and grid[new_row][new_col] == 0:
                visited.add(new_pos)
                parent[new_pos] = current
                queue.append(new_pos)

    # Reconstruct the path from start to goal
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    return path

#driver code
grid = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)

path = find_path(grid, start, goal)
print(path)