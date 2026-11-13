/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
 * LeetCode 110240695. 分治策略之 greatest slice — C 版（方案B：增量扫描）
 */
#include <stdio.h> // 引入头文件

static long long max_sub_array_ic(const int *arr, int n) {
    if (n == 0)
        return 0;                 // 若 元素个数 等于 0，直接返回 0
    long long gs = arr[0];        // 把 数组[0] 存入 gs
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        long long s = 0;          // 把 0 存入 字符串
        for (int j = i; j < n; j++) { // 让 下标 j 从 下标 i 开始计数，下标 j 小于 元素个数 就继续
            s += arr[j];              // 字符串累加 数组[下标 j]
            if (gs < s)
                gs = s; // 若 gs 小于 字符串) gs 赋值为 字符串;
        }
    }
    return gs; // 返回 gs
}

int main(void) {                          // 程序入口：跑内嵌自测用例
    int a0[7] = {-2, 1, -3, 4, -1, 2, 1}; // 把 { 减 2, 1, 减 3, 4, 减 1, 2, 1}; 写入 int a0[7]
    int a1[3] = {-1, -2, -3};             // 把 { 减 1, 减 2, 减 3}; 写入 int a1[3]
    if (max_sub_array_ic(a0, 7) != 6) {
        printf("ms1 failed\n");
        return 1;
    }
    if (max_sub_array_ic(a1, 3) != -1) {
        printf("ms2 failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
