# Problem: Given a 2D grid of W (water) and L (land), find the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.


def island_count(grid):
    """
    Counts the number of islands in a 2D grid of 'L' (land) and 'W' (water).
    """
    visited = set()
    count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def dfs(r, c):
        # Check bounds
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] == 'W':
            return
        if (r, c) in visited:
            return
        visited.add((r, c))
        # Explore all 4 directions
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'L' and (i, j) not in visited:
                dfs(i, j)
                count += 1
    return count

# Example usage:
if __name__ == '__main__':
    grid = [
        ['W', 'L', 'W', 'W', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'L'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
    ]
    print(island_count(grid))  # Example output: 4
    
    

    
