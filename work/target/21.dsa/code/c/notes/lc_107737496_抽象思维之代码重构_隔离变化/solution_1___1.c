/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案1：螺旋矩阵递归填充）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

static int M[6][6]; // static int M[6][6];

static void fill_spiral(int num, int begin, int size) { // 定义函数/方法 fill_spiral
    if (size == 0)
        return; // 若 大小 等于 0) return;
    if (size == 1) {
        M[begin][begin] = num;
        return;
    } // 若 大小 等于 1) { M[begin][begin] 赋值为 num; return; }
    for (int j = 0; j < size - 1; j++) {
        M[begin + j][begin] = num;
        num++;
    } // 让 下标 j 从 0 开始计数，下标 j 小于 大小 减 1 就继续
    for (int j = 0; j < size - 1; j++) {
        M[begin + size - 1][begin + j] = num;
        num++;
    } // 让 下标 j 从 0 开始计数，下标 j 小于 大小 减 1 就继续
    for (int j = size - 1; j > 0; j--) {
        M[begin + j][begin + size - 1] = num;
        num++;
    } // 让 下标 j 从 大小 减 1 开始计数，下标 j 超过 0 就继续
    for (int j = size - 1; j > 0; j--) {
        M[begin][begin + j] = num;
        num++;
    } // 让 下标 j 从 大小 减 1 开始计数，下标 j 超过 0 就继续
    fill_spiral(num, begin + 1, size - 2); // fill_spiral(num, begin 加 1, 大小 减 2);
}

static void fmt_row(const int *row, int n, char *out) { // 定义函数/方法 fmt_row
    out[0] = 0;                                         // 把 0; 写入 out[0]
    char cell[8];                                       // char cell[8];
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        snprintf(cell, sizeof(cell), "%2d", row[i]); // 打印输出
        if (i)
            strcat(out, " "); // 若 下标 i) strcat(out, 「 」);
        strcat(out, cell);    // 打印输出
    }
}

int main(void) {          // 程序入口：跑内嵌自测用例
    fill_spiral(1, 0, 6); // fill_spiral(1, 0, 6);
    const char *want[6] = {
        // 把 { 写入 const char *want[6]
        " 1 20 19 18 17 16", " 2 21 32 31 30 15", " 3 22 33 36 29 14",
        " 4 23 34 35 28 13", " 5 24 25 26 27 12", " 6  7  8  9 10 11",
    };
    for (int i = 0; i < 6; i++) {        // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
        char got[64];                    // char got[64];
        fmt_row(M[i], 6, got);           // fmt_row(M[下标 i], 6, got);
        if (strcmp(got, want[i]) != 0) { // 若 strcmp(got, want[下标 i]) 不等于 0
            printf("spiral6 row %d failed: got [%s] want [%s]\n", i, got, want[i]); // 打印输出
            return 1;                                                               // 返回 1
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
