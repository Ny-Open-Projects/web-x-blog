package com.imooc.dddq.code;

import java.util.ArrayList;
import java.util.List;

public class L51 {
    public List<List<String>> solveNQueens(int n) {
        // 1. n x n 棋盘初始化
        char[][] board = new char[n][n];
        for(int i = 0; i < n; i ++) {
            for(int j = 0; j < n; j ++) {
                board[i][j] = '.';
            }
        }
        List<List<String>> result = new ArrayList<>();
        backtrack(board, 0, n, result);
        return result;
    }

    /**
     * result = []
     * def backtrack(路径, 选择列表):
     * 	if 满足结束条件:
     * 		result.add(路径)
     * 		return
     * 	for 选择 in 选择列表:
     * 		做选择
     * 		backtrack(路径, 选择列表)
     * 		撤销选择
     */
    public void backtrack( char[][]board, int row, int n, List<List<String>> result) {
        // if 满足结束条件
        if(row == n) {
            result.add(arrayToList(board));
            return;
        }
        // for 选择 in 选择列表
        for (int col = 0; col < n; col ++) {
            if(! isValid(row, col, board)) {
                continue;
            }
            board[row][col] = 'Q';
            backtrack(board, row+1, n, result);
            board[row][col] = '.';
        }
    }

    // 把数组转换成列表满足题目要求
    public List<String> arrayToList(char[][] board) {
        List<String> list = new ArrayList<>();
        for(int i = 0; i < board.length; i ++) {
            StringBuilder builder = new StringBuilder();
            for(int j = 0; j < board.length; j++) {
                builder.append(board[i][j]);
            }
            list.add(builder.toString());
        }
        return list;
    }

    // 判断当前位置(row, col)的皇后是否合法
    public boolean isValid(int row, int col, char[][]board){
        // 行
        for(int tmpCol = 0; tmpCol < board.length; tmpCol ++) {
            if (board[row][tmpCol] == 'Q'){
                return false;
            }
        }
        // 列
        for(int tmpRow = 0; tmpRow < board.length; tmpRow ++) {
            if(board[tmpRow][col] == 'Q') {
                return false;
            }
        }
        // 45度角
        for(int i = row-1, j = col + 1; i >= 0 && j <= board.length-1; i --, j ++) {
            if(board[i][j] == 'Q') {
                return false;
            }
        }
        // 135度角
        for(int i = row-1, j = col - 1; i >= 0 && j >= 0; i --, j --) {
            if(board[i][j] == 'Q') {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args){
        int n = 4;
        System.out.println(new L51().solveNQueens(n));
    }
}
