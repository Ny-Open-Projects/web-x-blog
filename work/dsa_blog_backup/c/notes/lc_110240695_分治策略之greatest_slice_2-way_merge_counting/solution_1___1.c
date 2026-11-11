/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
 * LeetCode 110240695. 分治策略之 greatest slice — C 版（方案A：暴力枚举所有子段）
 */
#include <stdio.h> // 引入头文件

static long long max_sub_array_bf(const int *arr, int n) {
    long long best = 0;           // 把 0 存入 当前最优
    int first = 1;                // 把 1 存入 first
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        long long s = 0;          // 把 0 存入 字符串
        for (int j = i; j < n; j++) { // 让 下标 j 从 下标 i 开始计数，下标 j 小于 元素个数 就继续
            s += arr[j];              // 字符串累加 数组[下标 j]
            if (first || s > best) {
                best = s;
                first = 0;
            } // 若 first 或 字符串 超过 当前最优) { 当前最优 赋值为 字符串; first 赋值为 0; }
        }
    }
    return best; // 返回 当前最优
}

int main(void) { // 程序入口：跑内嵌自测用例
    int a0[9] = {-2, 1, -3, 4, -1,
                 2,  1, -5, 4};   // 把 { 减 2, 1, 减 3, 4, 减 1, 2, 1, 减 5, 4}; 写入 int a0[9]
    int a1[1] = {1};              // 把 {1}; 写入 int a1[1]
    int a2[3] = {-1, -2, -3};     // 把 { 减 1, 减 2, 减 3}; 写入 int a2[3]
    int a3[5] = {5, 4, -1, 7, 8}; // 把 {5, 4, 减 1, 7, 8}; 写入 int a3[5]
    if (max_sub_array_bf(a0, 9) != 6) {
        printf("case 0 failed\n");
        return 1;
    }
    if (max_sub_array_bf(a1, 1) != 1) {
        printf("case 1 failed\n");
        return 1;
    }
    if (max_sub_array_bf(a2, 3) != -1) {
        printf("case 2 failed\n");
        return 1;
    }
    if (max_sub_array_bf(a3, 5) != 23) {
        printf("case 3 failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
