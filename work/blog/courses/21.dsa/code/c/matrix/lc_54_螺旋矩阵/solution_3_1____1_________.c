/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134026430
 * LeetCode 54. 螺旋矩阵 — C 版 */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件

#define MAXC 8 // #define MAXC 8

/* 四边界逐层收缩；*returnSize 返回结果长度 */
static int *spiral_order(int rows, int cols, int mat[][MAXC], int *returnSize) {
    *returnSize = 0;
    if (rows == 0 || cols == 0)
        return NULL; // 若 行数 等于 0 或 列数 等于 0，直接返回 NULL
    int *result =
        malloc(sizeof(int) *
               (size_t)(rows * cols)); // 把 malloc(sizeof(int) 乘 (size_t)(行数 乘 列数)); 写入 int *result
    int top = 0, bottom = rows - 1, left = 0, right = cols - 1, cnt = 0;
    while (top <= bottom && left <= right) { // 循环，直到不满足「top 不超过 bottom 且 左边界 不超过 右边界」
        for (int i = left; i <= right; i++)
            result[cnt++] = mat[top][i]; // 让 下标 i 从 左边界 开始计数，下标 i 不超过 右边界 就继续
        top++;                           // top 加一
        for (int i = top; i <= bottom; i++)
            result[cnt++] = mat[i][right]; // 让 下标 i 从 top 开始计数，下标 i 不超过 bottom 就继续
        right--;                           // 右边界 减一
        if (top <= bottom) {               // 若 top 不超过 bottom
            for (int i = right; i >= left; i--)
                result[cnt++] = mat[bottom][i]; // 让 下标 i 从 右边界 开始计数，下标 i 不低于 左边界 就继续
            bottom--;                           // bottom 减一
        }
        if (left <= right) { // 若 左边界 不超过 右边界
            for (int i = bottom; i >= top; i--)
                result[cnt++] = mat[i][left]; // 让 下标 i 从 bottom 开始计数，下标 i 不低于 top 就继续
            left++;                           // 左边界 加一
        }
    }
    *returnSize = cnt;
    return result; // 返回 结果
}

int main(void) { // 程序入口：跑内嵌自测用例
    /* 与 TS 事实源内嵌用例一致：3x3 螺旋 */
    int mat[3][MAXC] = {
        {1, 2, 3}, {4, 5, 6}, {7, 8, 9}}; // 把 {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}; 写入 int mat[3][MAXC]
    int exp[9] = {1, 2, 3, 6, 9, 8, 7, 4, 5}; // 把 {1, 2, 3, 6, 9, 8, 7, 4, 5}; 写入 int exp[9]
    int sz = 0;                               // 把 0 存入 sz
    int *got = spiral_order(3, 3, mat, &sz);  // 把 spiral_order(3, 3, mat, 按位与 sz); 写入 int *got
    if (sz != 9) {                            // 若 sz 不等于 9
        printf("FAILED: size=%d\n", sz);      // 打印输出
        free(got);                            // free(got);
        return 1;                             // 返回 1
    }
    for (int i = 0; i < 9; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 9 就继续
        if (got[i] != exp[i]) {   // 若 got[下标 i] 不等于 exp[下标 i]
            printf("FAILED at %d: got %d want %d\n", i, got[i], exp[i]); // 打印输出
            free(got);                                                   // free(got);
            return 1;                                                    // 返回 1
        }
    }
    free(got);        // free(got);
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
