/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066015 */
/* LeetCode 41. 缺失的第一个正数 — C 版（方案14） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static int first_missing_positive(const int *nums, int n) { // 定义函数/方法 first_missing_positive
    if (n == 0)
        return 1;          // 若 元素个数 等于 0，直接返回 1
    int pos[4096], pn = 0; // 把 0; 写入 int pos[4096], pn
    for (int i = 0; i < n; i++)
        if (nums[i] > 0)
            pos[pn++] = nums[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    if (pn == 0)
        return 1;                         // 若 pn 等于 0，直接返回 1
    qsort(pos, pn, sizeof(int), cmp_int); // qsort(pos, pn, sizeof(int), cmp_int);
    if (pos[0] != 1)
        return 1;                      // 若 pos[0] 不等于 1，直接返回 1
    for (int i = 0; i < pn - 1; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 pn 减 1 就继续
        if (pos[i + 1] - pos[i] > 1)
            return pos[i] + 1; // 若 pos[下标 i 加 1] 减 pos[下标 i] 超过 1，直接返回 pos[下标 i] 加 1
    }
    return pos[pn - 1] + 1; // 返回 pos[pn 减 1] 加 1
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (first_missing_positive((int[]){1, 2, 0}, 3) != 3) {
        printf("FAIL 1\n");
        return 1;
    }
    if (first_missing_positive((int[]){3, 4, -1, 1}, 4) != 2) {
        printf("FAIL 2\n");
        return 1;
    }
    if (first_missing_positive((int[]){7, 8, 9, 11, 12}, 5) != 1) {
        printf("FAIL 3\n");
        return 1;
    }
    if (first_missing_positive(NULL, 0) != 1) {
        printf("FAIL 4\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
