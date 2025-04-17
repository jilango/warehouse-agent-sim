import heapq

def a_star(start, goal, grid):
    """Returns a list of coordinates forming the shortest path from start to goal."""
    rows, cols = grid.shape
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current, grid):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []  # No path found


def heuristic(a, b):
    """Manhattan distance heuristic for grid movement."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(pos, grid):
    """Returns walkable neighboring positions (up, down, left, right)."""
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = grid.shape

    for dr, dc in directions:
        nr, nc = pos[0] + dr, pos[1] + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr, nc] != -1:  # Not an obstacle
                neighbors.append((nr, nc))
    return neighbors


def reconstruct_path(came_from, current):
    """Rebuild path from end to start."""
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
