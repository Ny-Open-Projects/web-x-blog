/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134032039
 * LeetCode 48. 旋转矩阵 — C 版 */
#include <stdio.h> // 引入头文件

#define MAXN 8 // #define MAXN 8

/* 方案3：先上下翻转行，再沿主对角线转置（与 TS 事实源 solution_3 一致） */
static void rotate(int n, int mat[MAXN][MAXN]) { // 定义函数/方法 rotate
    for (int i = 0; i < n / 2; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 除以 2 就继续
        for (int j = 0; j < MAXN; j++) { /* 交换整行 */ // 让 下标 j 从 0 开始计数，下标 j 小于 MAXN 就继续
            int tmp = mat[i][j];                        // 把 mat[下标 i][下标 j] 存入 临时变量
            mat[i][j] = mat[n - 1 - i][j]; // 把 mat[元素个数 减 1 减 下标 i][下标 j]; 写入 mat[i][j]
            mat[n - 1 - i][j] = tmp;       // 把 临时变量; 写入 mat[n - 1 - i][j]
        }
    }
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (int j = 0; j < i; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
            int tmp = mat[i][j];      // 把 mat[下标 i][下标 j] 存入 临时变量
            mat[i][j] = mat[j][i];    // 把 mat[下标 j][下标 i]; 写入 mat[i][j]
            mat[j][i] = tmp;          // 把 临时变量; 写入 mat[j][i]
        }
    }
}

int main(void) { // 程序入口：跑内嵌自测用例
    struct {
        int n;
        int in[MAXN][MAXN];
        int exp[MAXN][MAXN];
    } tests[] = {
        {3, {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, {{7, 4, 1}, {8, 5, 2}, {9, 6, 3}}},
        {4,
         {{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}},
         {{15, 13, 2, 5}, {14, 3, 4, 1}, {12, 6, 8, 9}, {16, 7, 10, 11}}},
    };
    for (int t = 0; t < 2; t++) { // 让 另一字符串 从 0 开始计数，另一字符串 小于 2 就继续
        rotate(tests[t].n, tests[t].in); // rotate(tests[另一字符串].元素个数, tests[另一字符串].in);
        for (int i = 0; i < tests[t].n;
             i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 tests[另一字符串].元素个数 就继续
            for (int j = 0; j < tests[t].n;
                 j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 tests[另一字符串].元素个数 就继续
                if (tests[t].in[i][j] != tests[t].exp[i][j]) {
                    printf("case %d failed at (%d,%d): got %d want %d\n", t, i, j, tests[t].in[i][j],
                           tests[t].exp[i][j]);
                    return 1; // 返回 1
                }
            }
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
