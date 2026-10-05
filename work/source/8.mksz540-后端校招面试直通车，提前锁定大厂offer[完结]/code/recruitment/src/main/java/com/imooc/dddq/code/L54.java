package com.imooc.dddq.code;


import java.util.ArrayList;
import java.util.List;

public class L54 {
    public List<Integer> spiralOrder(int[][] matrix) {
        // 右、下、左、上
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        List<Integer> result = new ArrayList<>();
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return result;
        }
        int rows = matrix.length;
        int cols = matrix[0].length;
        int row = 0;
        int col = 0;
        int currDirection = 0;
        // 记录被访问的节点
        boolean[][] visited = new boolean[rows][cols];
        for(int i = 0; i < rows * cols; i ++) {
            result.add(matrix[row][col]);
            visited[row][col] = true;
            // 下一个行列方向
            int nextRow = row + directions[currDirection][0];
            int nextCol = col + directions[currDirection][1];
            if(nextRow < 0 || nextRow >= rows || nextCol < 0 || nextCol >= cols || visited[nextRow][nextCol]) {
                currDirection = (currDirection + 1) % 4;
            }
            row += directions[currDirection][0];
            col += directions[currDirection][1];
        }
        return result;
    }

    public static void main(String[] args){
        int[][] matrix = {{1,2,3}, {4,5,6}, {7,8,9}};
        System.out.println(new L54().spiralOrder(matrix));
    }
}
