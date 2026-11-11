/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631 */
/* LeetCode 1143. 最长公共子序列 — C 版（方案1） */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件
static int longest_common_subsequence(const char *t1,
                                      const char *t2) { // 定义函数/方法 longest_common_subsequence
    int m = (int)strlen(t1),
        n = (int)strlen(t2); // 把 (int)strlen(t1), 元素个数 赋值为 (int)strlen(t2) 存入 映射表
    int dp[1001] = {0};      // 把 {0}; 写入 int dp[1001]
    for (int i = 1; i <= m; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
        int prev_diag = 0;         // 把 0 存入 prev_diag
        for (int j = 1; j <= n; j++) { // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
            int tmp = dp[j];           // 把 DP 表[下标 j] 存入 临时变量
            dp[j] = t1[i - 1] == t2[j - 1] ? prev_diag + 1 : (dp[j] > dp[j - 1] ? dp[j] : dp[j - 1]);
            prev_diag = tmp; // 把 临时变量; 写入 prev_diag
        }
    }
    return dp[n]; // 返回 DP 表[元素个数]
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (longest_common_subsequence("abcde", "ace") != 3) {
        printf("FAIL 1\n");
        return 1;
    }
    if (longest_common_subsequence("abc", "abc") != 3) {
        printf("FAIL 2\n");
        return 1;
    }
    if (longest_common_subsequence("abc", "def") != 0) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS