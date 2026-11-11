/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133970744 */
/* LeetCode 51. N皇后 — C 版（方案3） */
#include <stdio.h>                  // 引入头文件
#include <stdlib.h>                 // 引入头文件
#include <string.h>                 // 引入头文件
static int cols_g[16], n_g;         // static int cols_g[16], n_g;
static char boards[256][16][17];    // static char boards[256][16][17];
static int boards_n;                // static int boards_n;
static int ok(int row, int col) {   // 定义函数/方法 ok
    for (int r = 0; r < row; r++) { // 让 右指针 从 0 开始计数，右指针 小于 row 就继续
        if (cols_g[r] == col || abs(r - row) == abs(cols_g[r] - col))
            return 0;
    }
    return 1; // 返回 1
}
static void dfs(int row) {              // 定义函数/方法 dfs
    if (row == n_g) {                   // 若 row 等于 n_g
        for (int r = 0; r < n_g; r++) { // 让 右指针 从 0 开始计数，右指针 小于 n_g 就继续
            for (int c = 0; c < n_g; c++)
                boards[boards_n][r][c] =
                    (cols_g[r] == c) ? 'Q' : '.'; // 让 字符 从 0 开始计数，字符 小于 n_g 就继续
            boards[boards_n][r][n_g] = '\0';      // 把 '\0'; 写入 boards[boards_n][r][n_g]
        }
        boards_n++; // boards_n 加一
        return;     // return;
    }
    for (int col = 0; col < n_g; col++) { // 让 col 从 0 开始计数，col 小于 n_g 就继续
        if (ok(row, col)) {               // 若 ok(row, col
            cols_g[row] = col;            // 把 col; 写入 cols_g[row]
            dfs(row + 1);                 // dfs(row 加 1);
        }
    }
}
static int solve_n_queens(int n) { // 定义函数/方法 solve_n_queens
    n_g = n;
    boards_n = 0;    // 把 元素个数; boards_n 赋值为 0; 写入 n_g
    dfs(0);          // dfs(0);
    return boards_n; // 返回 boards_n
}
int main(void) {               // 程序入口：跑内嵌自测用例
    int n = solve_n_queens(4); // 把 solve_n_queens(4) 存入 元素个数
    if (n != 2) {
        printf("FAIL cnt=%d\n", n);
        return 1;
    } // 若 元素个数 不等于 2) { 输出「FAIL 计数 赋值为 对…取模 d 」, 元素个数); return 1; }
    if (strcmp(boards[0][0], ".Q..") != 0 || strcmp(boards[0][3], "..Q.") != 0) {
        printf("FAIL b1\n");
        return 1;
    }
    if (strcmp(boards[1][0], "..Q.") != 0) {
        printf("FAIL b2\n");
        return 1;
    }
    if (solve_n_queens(1) != 1) {
        printf("FAIL 2\n");
        return 1;
    }                 // 若 solve_n_queens(1) 不等于 1) { 输出「FAIL 2 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
