/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130727613 */
/* LeetCode 300. 最长递增子序列 — C 版（方案2） */
#include <stdio.h>                                // 引入头文件
static int length_of_lis(const int *n, int len) { // 定义函数/方法 length_of_lis
    int dp[4096], best = 0;                       // 把 0; 写入 int dp[4096], best
    for (int i = 0; i < len; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
        dp[i] = 1;                  // 把 1; 写入 dp[i]
        for (int j = 0; j < i; j++) // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
            if (n[j] < n[i] && dp[j] + 1 > dp[i])
                dp[i] = dp[j] + 1;
        if (dp[i] > best)
            best = dp[i]; // 若 DP 表[下标 i] 超过 当前最优) 当前最优 赋值为 DP 表[下标 i];
    }
    return best; // 返回 当前最优
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (length_of_lis((int[]){10, 9, 2, 5, 3, 7, 101, 18}, 8) != 4) {
        printf("FAIL 1\n");
        return 1;
    }
    if (length_of_lis((int[]){0, 1, 0, 3, 2, 3}, 6) != 4) {
        printf("FAIL 2\n");
        return 1;
    }
    if (length_of_lis((int[]){7, 7, 7, 7}, 4) != 1) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS