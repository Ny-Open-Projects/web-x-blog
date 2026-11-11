/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130663853 */
/* LeetCode 1. 两数之和 — C 版（方案1：暴力双循环） */
#include <stdio.h>                                                   // 引入头文件
static int two_sum(const int *nums, int n, int target, int out[2]) { // 定义函数/方法 two_sum
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (int j = i + 1; j < n; j++) { // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 元素个数 就继续
            if (nums[i] + nums[j] == target) {
                out[0] = i;
                out[1] = j;
                return 2;
            }
        }
    }
    return 0; // 返回 0
}
int main(void) { // 程序入口：跑内嵌自测用例
    int out[2];  // int out[2];
    if (two_sum((int[]){2, 7, 11, 15}, 4, 9, out) != 2 || out[0] != 0 || out[1] != 1) {
        printf("FAIL 1\n");
        return 1;
    }
    if (two_sum((int[]){3, 2, 4}, 3, 6, out) != 2 || out[0] != 1 || out[1] != 2) {
        printf("FAIL 2\n");
        return 1;
    }
    if (two_sum((int[]){3, 3}, 2, 6, out) != 2 || out[0] != 0 || out[1] != 1) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
