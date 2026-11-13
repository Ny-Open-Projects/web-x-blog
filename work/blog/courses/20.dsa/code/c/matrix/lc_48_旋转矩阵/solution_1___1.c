/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134032039
 * LeetCode 48. 旋转矩阵 — C 版 */
#include <stdio.h> // 引入头文件

#define MAXN 8 // #define MAXN 8

/* 方案1：先沿主对角线转置，再逐行左右翻转（原地修改） */
static void rotate(int n, int mat[MAXN][MAXN]) { // 定义函数/方法 rotate
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (int j = i + 1; j < n; j++) { // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 元素个数 就继续
            int tmp = mat[i][j];   // 把 mat[下标 i][下标 j] 存入 临时变量
            mat[i][j] = mat[j][i]; // 把 mat[下标 j][下标 i]; 写入 mat[i][j]
            mat[j][i] = tmp;       // 把 临时变量; 写入 mat[j][i]
        }
    }
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (int j = 0, k = n - 1; j < k;
             j++, k--) { // 让 下标 j 从 0, 下标 k 赋值为 元素个数 减 1 开始计数，下标 j 小于 下标 k 就继续
            int tmp = mat[i][j];   // 把 mat[下标 i][下标 j] 存入 临时变量
            mat[i][j] = mat[i][k]; // 把 mat[下标 i][下标 k]; 写入 mat[i][j]
            mat[i][k] = tmp;       // 把 临时变量; 写入 mat[i][k]
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
