/* 来源：https://blog.csdn.net/tyro_java/article/details/107490876
 * LeetCode 107490876. 分书和八皇后问题 — C 版（方案7：八皇后位置对列表）
 */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件

typedef struct {  // typedef struct {
    int row, col; // int row, col;
} Pair;           // } Pair;

static Pair positions[8]; // static Pair positions[8];
static int plen = 0;      // 把 0; 写入 static int plen
static int sols[100][8];  // static int sols[100][8];
static int sol_count = 0; // 把 0; 写入 static int sol_count
static int N;             // static int N;

static int safe(int r, int c) {      // 定义函数/方法 safe
    for (int i = 0; i < plen; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 plen 就继续
        if (positions[i].row == r || abs(positions[i].row - r) == abs(positions[i].col - c))
            return 0;
    }
    return 1; // 返回 1
}

static void solve(int col) { // 定义函数/方法 solve
    if (col == N) {          // 若 col 等于 N
        for (int i = 0; i < N; i++)
            sols[sol_count][i] = positions[i].row; // 让 下标 i 从 0 开始计数，下标 i 小于 N 就继续
        sol_count++;                               // sol_count 加一
        return;                                    // return;
    }
    for (int r = 0; r < N; r++) {      // 让 右指针 从 0 开始计数，右指针 小于 N 就继续
        if (safe(r, col)) {            // 若 safe(右指针, col
            positions[plen].row = r;   // 把 右指针; 写入 positions[plen].row
            positions[plen].col = col; // 把 col; 写入 positions[plen].col
            plen++;                    // plen 加一
            solve(col + 1);            // solve(col 加 1);
            plen--;                    // plen 减一
        }
    }
}

static int n_queens_simple(int n) { // 定义函数/方法 n_queens_simple
    N = n;                          // 把 元素个数; 写入 N
    plen = 0;                       // 把 0; 写入 plen
    sol_count = 0;                  // 把 0; 写入 sol_count
    solve(0);                       // solve(0);
    return sol_count;               // 返回 sol_count
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
    for (int idx = 0; idx < 4; idx++) {            // 让 idx 从 0 开始计数，idx 小于 4 就继续
        int count = n_queens_simple(cases[idx].n); // 把 n_queens_simple(cases[idx].元素个数) 存入 计数
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
