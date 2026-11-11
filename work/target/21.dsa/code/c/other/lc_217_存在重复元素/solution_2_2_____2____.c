/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135038527 */
/* LeetCode 217. 存在重复元素 — C 版（方案2） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static int contains_duplicate(const int *nums, int n) { // 定义函数/方法 contains_duplicate
    if (n <= 1)
        return 0;                          // 若 元素个数 不超过 1，直接返回 0
    int *sorted = malloc(sizeof(int) * n); // 把 malloc(sizeof(int) 乘 元素个数); 写入 int *sorted
    for (int i = 0; i < n; i++)
        sorted[i] = nums[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    qsort(sorted, n, sizeof(int), cmp_int); // qsort(sorted, 元素个数, sizeof(int), cmp_int);
    int dup = 0;                            // 把 0 存入 dup
    for (int i = 1; i < n; i++)
        if (sorted[i] == sorted[i - 1]) {
            dup = 1;
            break;
        }         // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
    free(sorted); // free(sorted);
    return dup;   // 返回 dup
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (!contains_duplicate((int[]){1, 2, 3, 1}, 4)) {
        printf("FAIL 1\n");
        return 1;
    }
    if (contains_duplicate((int[]){1, 2, 3, 4}, 4)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
