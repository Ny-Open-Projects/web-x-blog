/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130641517 */
/* LeetCode 62. 不同路径 — C 版（方案4） */
#include <stdio.h>                      // 引入头文件
static int unique_paths(int m, int n) { // 定义函数/方法 unique_paths
    int dp[101];                        // int DP 表[101];
    for (int j = 0; j < n; j++)
        dp[j] = 1;              // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
    for (int i = 1; i < m; i++) // 让 下标 i 从 1 开始计数，下标 i 小于 映射表 就继续
        for (int j = 1; j < n; j++)
            dp[j] += dp[j - 1]; // 让 下标 j 从 1 开始计数，下标 j 小于 元素个数 就继续
    return dp[n - 1];           // 返回 DP 表[元素个数 减 1]
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (unique_paths(3, 7) != 28) {
        printf("FAIL 1\n");
        return 1;
    } // 若 unique_paths(3, 7) 不等于 28) { 输出「FAIL 1 」); return 1; }
    if (unique_paths(3, 2) != 3) {
        printf("FAIL 2\n");
        return 1;
    } // 若 unique_paths(3, 2) 不等于 3) { 输出「FAIL 2 」); return 1; }
    if (unique_paths(1, 1) != 1) {
        printf("FAIL 3\n");
        return 1;
    } // 若 unique_paths(1, 1) 不等于 1) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS