/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130683917 */
/* LeetCode 322. 零钱兑换 — C 版（方案1） */
#include <stdio.h>                                             // 引入头文件
static int coin_change(const int *coins, int nc, int amount) { // 定义函数/方法 coin_change
    long dp[10001];                                            // long DP 表[10001];
    dp[0] = 0;                                                 // 把 0; 写入 dp[0]
    for (int a = 1; a <= amount; a++)
        dp[a] = 1L << 40; // 让 数组 从 1 开始计数，数组 不超过 目标金额 就继续
    for (int a = 1; a <= amount; a++) { // 让 数组 从 1 开始计数，数组 不超过 目标金额 就继续
        for (int i = 0; i < nc; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 nc 就继续
            if (coins[i] <= a &&
                dp[a - coins[i]] < (1L << 40)) { // 若 硬币面额[下标 i] 不超过 数组 且 DP 表[数组 减
                                                 // 硬币面额[下标 i]] 小于 (1L 小于 小于 40
                if (dp[a - coins[i]] + 1 < dp[a])
                    dp[a] = dp[a - coins[i]] + 1;
            }
        }
    }
    return dp[amount] >= (1L << 40) ? -1 : (int)dp[amount]; // 返回 DP 表[目标金额] 不低于 (1L 小于 小于 40) ?
                                                            // 减 1 : (int)DP 表[目标金额]
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (coin_change((int[]){1, 2, 5}, 3, 11) != 3) {
        printf("FAIL 1\n");
        return 1;
    }
    if (coin_change((int[]){2}, 1, 3) != -1) {
        printf("FAIL 2\n");
        return 1;
    }
    if (coin_change((int[]){1}, 1, 0) != 0) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS