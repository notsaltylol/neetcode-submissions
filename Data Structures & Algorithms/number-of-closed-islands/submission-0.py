class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
        def outOfBounds(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return True

        visited = set()
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in visited and grid[i][j] == 0:
                    stack = [(i,j)]
                    edge_cell = False
                    while(len(stack) != 0):
                        m,n = stack.pop()
                        for x,y in neighbors:
                            if (m+x, n+y) not in visited and not outOfBounds(m+x,n+y) and grid[m+x][n+y] == 0:
                                stack.append((m+x,n+y))
                            if outOfBounds(m+x,n+y):
                                edge_cell = True
                        visited.add((m,n))
                    if edge_cell == False:
                        island_count += 1
        return island_count
                            


