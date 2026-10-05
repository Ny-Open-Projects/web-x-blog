package com.imooc.dddq.code;

public class L200 {
    public int numIslands(char[][] grid) {
        int result = 0;
        int rows = grid.length;
        int cols = grid[0].length;
        // 辅助数组
        int [][]visited = new int[rows][cols];
        for(int i = 0; i < rows; i ++) {
            for (int j = 0; j < cols; j ++) {
                visited[i][j] = 0;
            }
        }
        for (int i = 0; i < rows; i ++) {
            for (int j = 0; j < cols; j ++) {
                if (grid[i][j] == '1' && visited[i][j] == 0) {
                    dfs(grid, i, j, visited);
                    result += 1;
                }
            }
        }
        return result;
    }

    public void dfs(char [][]grid, int i, int j, int[][] visited) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] == '0' || visited[i][j] == 1) {
            return;
        }
        visited[i][j] = 1;
        // 上
        dfs(grid, i-1, j, visited);
        // 下
        dfs(grid, i+1, j, visited);
        // 左
        dfs(grid, i, j-1, visited);
        // 右
        dfs(grid, i, j+1, visited);
    }
}
