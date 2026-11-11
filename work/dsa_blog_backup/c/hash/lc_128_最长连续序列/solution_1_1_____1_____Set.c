/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135167108 */
/* LeetCode 128. 最长连续序列 — C 版（方案1） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static int longest_consecutive(const int *nums, int n) { // 定义函数/方法 longest_consecutive
    if (n == 0)
        return 0;                          // 若 元素个数 等于 0，直接返回 0
    int *sorted = malloc(sizeof(int) * n); // 把 malloc(sizeof(int) 乘 元素个数); 写入 int *sorted
    for (int i = 0; i < n; i++)
        sorted[i] = nums[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    qsort(sorted, n, sizeof(int), cmp_int); // qsort(sorted, 元素个数, sizeof(int), cmp_int);
    int best = 1, streak = 1;               // 把 1, streak 赋值为 1 存入 当前最优
    for (int i = 1; i < n; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
        if (sorted[i] == sorted[i - 1])
            continue; // 若 sorted[下标 i] 等于 sorted[下标 i 减 1]) continue;
        if (sorted[i] == sorted[i - 1] + 1)
            streak++; // 若 sorted[下标 i] 等于 sorted[下标 i 减 1] 加 1) streak 加一 ;
        else
            streak = 1; // 否则
        if (streak > best)
            best = streak; // 若 streak 超过 当前最优) 当前最优 赋值为 streak;
    }
    free(sorted); // free(sorted);
    return best;  // 返回 当前最优
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (longest_consecutive((int[]){100, 4, 200, 1, 3, 2}, 6) != 4) {
        printf("FAIL 1\n");
        return 1;
    }
    if (longest_consecutive((int[]){0, 3, 7, 2, 5, 8, 4, 6, 0, 1}, 10) != 9) {
        printf("FAIL 2\n");
        return 1;
    }
    if (longest_consecutive(NULL, 0) != 0) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
