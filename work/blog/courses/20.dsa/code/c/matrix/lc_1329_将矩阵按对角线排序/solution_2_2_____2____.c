/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381786
 * LeetCode 1329. 将矩阵按对角线排序 — C 版 */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件

#define MAXR 8 // #define MAXR 8
#define MAXC 8 // #define MAXC 8

static int cmp_int(const void *a, const void *b) { // 定义函数/方法 cmp_int
    int x = *(const int *)a,
        y = *(const int *)b;  // 把 乘 (const int 乘 )数组, y 赋值为 乘 (const int 乘 )b 存入 x
    return (x > y) - (x < y); // 返回 (x 超过 y) 减 (x 小于 y)
}

/* 方案2：优化版 —— 与 TS 事实源一致：按 r-c 分组收集对角线，升序排序，按原顺序写回（shift 取最小值）。
 * C 无内建哈希表，按对角线编号 d = r-c 从 -(cols-1) 到 rows-1 逐条收集。 */
static void diagonal_sort(int rows, int cols, int mat[][MAXC]) { // 定义函数/方法 diagonal_sort
    int buf[MAXR + MAXC];                                        // int buf[MAXR 加 MAXC];
    for (int d = -(cols - 1); d <= rows - 1;
         d++) {      // 让 d 从 减 (列数 减 1) 开始计数，d 不超过 行数 减 1 就继续
        int cnt = 0; // 把 0 存入 计数
        int r0 = d > 0 ? d : 0;           // 把 d 超过 0 ? d : 0 存入 r0
        for (int r = r0; r < rows; r++) { // 让 右指针 从 r0 开始计数，右指针 小于 行数 就继续
            int c = r - d;                // 把 右指针 减 d 存入 字符
            if (c < 0 || c >= cols)
                continue;           // 若 字符 小于 0 或 字符 不低于 列数) continue;
            buf[cnt++] = mat[r][c]; // 把 mat[右指针][字符]; 写入 buf[cnt++]
        }
        qsort(buf, (size_t)cnt, sizeof(int), cmp_int); // qsort(buf, (size_t)计数, sizeof(int), cmp_int);
        int k = 0;                                     // 把 0 存入 下标 k
        for (int r = r0; r < rows; r++) { // 让 右指针 从 r0 开始计数，右指针 小于 行数 就继续
            int c = r - d;                // 把 右指针 减 d 存入 字符
            if (c < 0 || c >= cols)
                continue;         // 若 字符 小于 0 或 字符 不低于 列数) continue;
            mat[r][c] = buf[k++]; // 把 buf[下标 k 加一 ]; 写入 mat[r][c]
        }
    }
}

int main(void) { // 程序入口：跑内嵌自测用例
    /* 与 TS 事实源内嵌用例一致 */
    int mat[MAXR][MAXC] = {{3, 3, 1, 1}, {2, 2, 1, 2}, {1, 1, 1, 2}};
    int exp[MAXR][MAXC] = {{1, 1, 1, 1}, {1, 2, 2, 2}, {1, 2, 3, 3}};
    int rows = 3, cols = 4;              // 把 3, 列数 赋值为 4 存入 行数
    diagonal_sort(rows, cols, mat);      // diagonal_sort(行数, 列数, mat);
    for (int i = 0; i < rows; i++) {     // 让 下标 i 从 0 开始计数，下标 i 小于 行数 就继续
        for (int j = 0; j < cols; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 列数 就继续
            if (mat[i][j] != exp[i][j]) { // 若 mat[下标 i][下标 j] 不等于 exp[下标 i][下标 j]
                printf("FAILED at (%d,%d): got %d want %d\n", i, j, mat[i][j], exp[i][j]); // 打印输出
                return 1;                                                                  // 返回 1
            }
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
