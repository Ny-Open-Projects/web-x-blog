/* 来源：https://blog.csdn.net/tyro_java/article/details/107490876
 * LeetCode 107490876. 分书和八皇后问题 — C 版（方案5：八皇后布尔数组标记，行号 0..n-1）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

static int col_row[8];    // static int col_row[8];
static int rows[8];       // static int 行数[8];
static int diag1[16];     // static int diag1[16];
static int diag2[16];     // static int diag2[16];
static int sols[100][8];  // static int sols[100][8];
static int sol_count = 0; // 把 0; 写入 static int sol_count
static int N;             // static int N;
static int OFFSET;        // static int OFFSET;

static void place(int col) { // 定义函数/方法 place
    if (col == N) {          // 若 col 等于 N
        memcpy(sols[sol_count], col_row,
               sizeof(int) * N); // memcpy(sols[sol_count], col_row, sizeof(int) 乘 N);
        sol_count++;             // sol_count 加一
        return;                  // return;
    }
    for (int row = 0; row < N; row++) {            // 让 row 从 0 开始计数，row 小于 N 就继续
        int d1 = col - row + OFFSET;               // 把 col 减 row 加 OFFSET 存入 d1
        int d2 = col + row;                        // 把 col 加 row 存入 d2
        if (rows[row] && diag1[d1] && diag2[d2]) { // 若 行数[row] 且 diag1[d1] 且 diag2[d2]
            col_row[col] = row;                    // 把 row; 写入 col_row[col]
            rows[row] = 0;                         // 把 0; 写入 rows[row]
            diag1[d1] = 0;                         // 把 0; 写入 diag1[d1]
            diag2[d2] = 0;                         // 把 0; 写入 diag2[d2]
            place(col + 1);                        // place(col 加 1);
            rows[row] = 1;                         // 把 1; 写入 rows[row]
            diag1[d1] = 1;                         // 把 1; 写入 diag1[d1]
            diag2[d2] = 1;                         // 把 1; 写入 diag2[d2]
        }
    }
}

static int n_queens_bool(int n) {                // 定义函数/方法 n_queens_bool
    N = n;                                       // 把 元素个数; 写入 N
    OFFSET = n - 1;                              // 把 元素个数 减 1; 写入 OFFSET
    memset(rows, 1, sizeof(int) * n);            // memset(行数, 1, sizeof(int) 乘 元素个数);
    memset(diag1, 1, sizeof(int) * (2 * n - 1)); // memset(diag1, 1, sizeof(int) 乘 (2 乘 元素个数 减 1));
    memset(diag2, 1, sizeof(int) * (2 * n - 1)); // memset(diag2, 1, sizeof(int) 乘 (2 乘 元素个数 减 1));
    sol_count = 0;                               // 把 0; 写入 sol_count
    place(0);                                    // place(0);
    return sol_count;                            // 返回 sol_count
}

int main(void) { // 程序入口：跑内嵌自测用例
    struct {
        int n;
        int count;
        int has_first;
        int first[8];
    } cases[] = {
        {8, 92, 1, {0, 4, 7, 5, 2, 6, 1, 3}},
        {1, 1, 1, {0}},
        {2, 0, 0, {0}},
        {4, 2, 1, {1, 3, 0, 2}},
    };
    for (int idx = 0; idx < 4; idx++) {          // 让 idx 从 0 开始计数，idx 小于 4 就继续
        int count = n_queens_bool(cases[idx].n); // 把 n_queens_bool(cases[idx].元素个数) 存入 计数
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
