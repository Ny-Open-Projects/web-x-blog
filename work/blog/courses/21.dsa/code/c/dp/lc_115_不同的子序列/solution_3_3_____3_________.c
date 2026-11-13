/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130590161 */
/* LeetCode 115. 不同的子序列 — C 版（方案3） */
#include <stdio.h>                                       // 引入头文件
#include <string.h>                                      // 引入头文件
static long num_distinct(const char *s, const char *t) { // 定义函数/方法 num_distinct
    int m = (int)strlen(s),
        n = (int)strlen(t); // 把 (int)strlen(字符串), 元素个数 赋值为 (int)strlen(另一字符串) 存入 映射表
    long dp[1001] = {0};           // 把 {0}; 写入 long dp[1001]
    dp[0] = 1;                     // 把 1; 写入 dp[0]
    for (int i = 1; i <= m; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
        for (int j = n; j >= 1; j--) { // 让 下标 j 从 元素个数 开始计数，下标 j 不低于 1 就继续
            if (s[i - 1] == t[j - 1])
                dp[j] += dp[j - 1];
        }
    }
    return dp[n]; // 返回 DP 表[元素个数]
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (num_distinct("rabbbit", "rabbit") != 3) {
        printf("FAIL 1\n");
        return 1;
    }
    if (num_distinct("babgbag", "bag") != 5) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS