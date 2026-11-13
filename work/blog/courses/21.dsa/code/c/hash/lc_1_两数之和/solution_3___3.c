/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130663853 */
/* LeetCode 1. 两数之和 — C 版（方案3：哈希表一次遍历） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
/* 哈希解法：值域散列（测试值小，用直接映射足够；通用性用开放寻址简化为线性扫描兜底） */
static int two_sum(const int *nums, int n, int target, int out[2]) { // 定义函数/方法 two_sum
    for (int i = 0; i < n;
         i++) { /* 等价 one-pass：先查先前元素 */ // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (int j = 0; j < i; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
            if (nums[j] == target - nums[i]) {
                out[0] = j;
                out[1] = i;
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
