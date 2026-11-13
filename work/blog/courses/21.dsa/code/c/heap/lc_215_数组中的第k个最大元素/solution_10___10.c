/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440 */
/* LeetCode 215. 数组中的第K个最大元素 — C 版（方案10） */
#include <stdio.h>                                           // 引入头文件
static int find_kth_largest(const int *nums, int n, int k) { // 定义函数/方法 find_kth_largest
    int a[4096];                                             // int 数组[4096];
    for (int i = 0; i < n; i++)
        a[i] = nums[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (int i = n - 1; i > n - 1 - k;
         i--) { // 让 下标 i 从 元素个数 减 1 开始计数，下标 i 超过 元素个数 减 1 减 下标 k 就继续
        for (int j = 0; j < i; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
            if (a[j] > a[j + 1]) {
                int t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
        }
    }
    return a[n - k]; // 返回 数组[元素个数 减 下标 k]
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
