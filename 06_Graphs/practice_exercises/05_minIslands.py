# Problem: Given a 2D grid of W (water) and L (land), find the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

def min_island_size(grid):
    """
    Returns the size of the smallest island in a 2D grid of 'L' (land) and 'W' (water).
    If there are no islands, returns 0.
    """
    visited = set()
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    minimum = float('inf')

    def dfs(r, c, island):
        # Check bounds
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] == 'W':
            return
        if (r, c) in visited:
            return
        visited.add((r, c))
        island.add((r, c))
        # Explore all 4 directions
        dfs(r - 1, c, island)
        dfs(r + 1, c, island)
        dfs(r, c - 1, island)
        dfs(r, c + 1, island)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'L' and (i, j) not in visited:
                island = set()
                dfs(i, j, island)
                if island:
                    minimum = min(minimum, len(island))

    return minimum if minimum != float('inf') else 0

# Example usage:
if __name__ == '__main__':
    grid = [
        ['W', 'L', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'L'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'L', 'W', 'L', 'L'],
    ]
    print(min_island_size(grid))  # Example output: 4
    
    

    
