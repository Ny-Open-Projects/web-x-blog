/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440 */
/* LeetCode 215. 数组中的第K个最大元素 — C 版（方案5） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
static int cmp_desc(const void *a, const void *b) { return *(const int *)b - *(const int *)a; }
static int find_kth_largest(const int *nums, int n, int k) { // 定义函数/方法 find_kth_largest
    int *a = malloc(sizeof(int) * n); // 把 malloc(sizeof(int) 乘 元素个数); 写入 int *a
    for (int i = 0; i < n; i++)
        a[i] = nums[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    qsort(a, n, sizeof(int), cmp_desc); // qsort(数组, 元素个数, sizeof(int), cmp_desc);
    int r = a[k - 1];                   // 把 数组[下标 k 减 1] 存入 右指针
    free(a);                            // free(数组);
    return r;                           // 返回 右指针
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (find_kth_largest((int[]){3, 2, 1, 5, 6, 4}, 6, 2) != 5) {
        printf("FAIL 1\n");
        return 1;
    }
    if (find_kth_largest((int[]){3, 2, 3, 1, 2, 4, 5, 5, 6}, 9, 4) != 4) {
        printf("FAIL 2\n");
        return 1;
    }
    if (find_kth_largest((int[]){1}, 1, 1) != 1) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
