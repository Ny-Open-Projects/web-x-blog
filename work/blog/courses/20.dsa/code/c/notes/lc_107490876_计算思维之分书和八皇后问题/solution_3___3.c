/* 来源：https://blog.csdn.net/tyro_java/article/details/107490876
 * LeetCode 107490876. 分书和八皇后问题 — C 版（方案3：八皇后递归 isSafe，行号 1..n）
 */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件

static int board[8];      // static int 棋盘[8];
static int sols[100][8];  // static int sols[100][8];
static int sol_count = 0; // 把 0; 写入 static int sol_count
static int N;             // static int N;

static int is_safe(int col, int row) { // 定义判定函数 is_safe
    for (int c = 0; c < col; c++) {    // 让 字符 从 0 开始计数，字符 小于 col 就继续
        if (board[c] == row || abs(board[c] - row) == abs(c - col))
            return 0;
    }
    return 1; // 返回 1
}

static void place(int col) { // 定义函数/方法 place
    if (col == N) {          // 若 col 等于 N
        for (int i = 0; i < N; i++)
            sols[sol_count][i] = board[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 N 就继续
        sol_count++;                       // sol_count 加一
        return;                            // return;
    }
    for (int row = 1; row <= N; row++) { // 让 row 从 1 开始计数，row 不超过 N 就继续
        if (is_safe(col, row)) {         // 若 is_safe(col, row
            board[col] = row;            // 把 row; 写入 board[col]
            place(col + 1);              // place(col 加 1);
        }
    }
}

static int n_queens_safe(int n) { // 定义函数/方法 n_queens_safe
    N = n;                        // 把 元素个数; 写入 N
    sol_count = 0;                // 把 0; 写入 sol_count
    place(0);                     // place(0);
    return sol_count;             // 返回 sol_count
}

int main(void) { // 程序入口：跑内嵌自测用例
    struct {
        int n;
        int count;
        int has_first;
        int first[8];
    } cases[] = {
        {8, 92, 1, {1, 5, 8, 6, 3, 7, 2, 4}},
        {1, 1, 1, {1}},
        {2, 0, 0, {0}},
        {4, 2, 1, {2, 4, 1, 3}},
    };
    for (int idx = 0; idx < 4; idx++) {          // 让 idx 从 0 开始计数，idx 小于 4 就继续
        int count = n_queens_safe(cases[idx].n); // 把 n_queens_safe(cases[idx].元素个数) 存入 计数
        if (count != cases[idx].count) {
            printf("case %d count %d\n", idx, count);
            return 1;
        }
        if (cases[idx].has_first) { // 若 cases[idx].has_first
            for (int j = 0; j < cases[idx].n;
                 j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 cases[idx].元素个数 就继续
                if (sols[0][j] != cases[idx].first[j]) {
                    printf("case %d first\n", idx);
                    return 1;
                }
            }
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
