/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130540333 */
/* LeetCode 72. 编辑距离 — C 版（方案2） */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件
static int min2(int a, int b) {
    return a < b ? a : b;
} // static int min2(int 数组, int b) { return 数组 小于 b ? 数组 : b; }
static int min3(int a, int b, int c) { return min2(min2(a, b), c); }
static int min_distance(const char *w1, const char *w2) { // 定义函数/方法 min_distance
    int m = (int)strlen(w1),
        n = (int)strlen(w2); // 把 (int)strlen(w1), 元素个数 赋值为 (int)strlen(w2) 存入 映射表
    int dp[1001];            // int DP 表[1001];
    for (int j = 0; j <= n; j++)
        dp[j] = j; // 让 下标 j 从 0 开始计数，下标 j 不超过 元素个数 就继续
    for (int i = 1; i <= m; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
        int prev_diag = dp[0];     // 把 DP 表[0] 存入 prev_diag
        dp[0] = i;                 // 把 下标 i; 写入 dp[0]
        for (int j = 1; j <= n; j++) { // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
            int tmp = dp[j];           // 把 DP 表[下标 j] 存入 临时变量
            dp[j] = w1[i - 1] == w2[j - 1] ? prev_diag : 1 + min3(prev_diag, dp[j], dp[j - 1]);
            prev_diag = tmp; // 把 临时变量; 写入 prev_diag
        }
    }
    return dp[n]; // 返回 DP 表[元素个数]
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (min_distance("horse", "ros") != 3) {
        printf("FAIL 1\n");
        return 1;
    }
    if (min_distance("intention", "execution") != 5) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS