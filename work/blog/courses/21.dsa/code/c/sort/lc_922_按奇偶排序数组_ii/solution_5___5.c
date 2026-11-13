/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975 */
/* LeetCode 922. 按奇偶排序数组II — C 版（方案5） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static void sort_array_by_parity_ii(const int *nums, int n,
                                    int res[]) { // 定义函数/方法 sort_array_by_parity_ii
    int sorted[4096];                            // int sorted[4096];
    for (int i = 0; i < n; i++)
        sorted[i] = nums[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    qsort(sorted, n, sizeof(int), cmp_int); // qsort(sorted, 元素个数, sizeof(int), cmp_int);
    int odd = 1, even = 0;                  // 把 1, even 赋值为 0 存入 odd
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        if (sorted[i] % 2 != 0) {
            res[odd] = sorted[i];
            odd += 2;
        } else {
            res[even] = sorted[i];
            even += 2;
        } // 否则
    }
}
int main(void) { // 程序入口：跑内嵌自测用例
    int res[64]; // int 结果[64];
    sort_array_by_parity_ii((int[]){4, 2, 5, 7}, 4,
                            res); // sort_array_by_parity_ii((int[]){4,2,5,7}, 4, 结果);
    if (res[0] != 2 || res[1] != 5 || res[2] != 4 || res[3] != 7) {
        printf("FAIL 1\n");
        return 1;
    }
    sort_array_by_parity_ii((int[]){2, 3}, 2, res); // sort_array_by_parity_ii((int[]){2,3}, 2, 结果);
    if (res[0] != 2 || res[1] != 3) {
        printf("FAIL 2\n");
        return 1;
    } // 若 结果[0] 不等于 2 或 结果[1] 不等于 3) { 输出「FAIL 2 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
