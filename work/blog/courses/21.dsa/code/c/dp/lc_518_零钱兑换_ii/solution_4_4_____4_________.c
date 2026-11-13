/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734179 */
/* LeetCode 518. 零钱兑换II — C 版（方案4） */
#include <stdio.h>                                         // 引入头文件
static long change(int amount, const int *coins, int nc) { // 定义函数/方法 change
    long dp[10001] = {0};                                  // 把 {0}; 写入 long dp[10001]
    dp[0] = 1;                                             // 把 1; 写入 dp[0]
    for (int i = 0; i < nc; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 nc 就继续
        for (int a = coins[i]; a <= amount; a++)
            dp[a] += dp[a - coins[i]]; // 让 数组 从 硬币面额[下标 i] 开始计数，数组 不超过 目标金额 就继续
    }
    return dp[amount]; // 返回 DP 表[目标金额]
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (change(5, (int[]){1, 2, 5}, 3) != 4) {
        printf("FAIL 1\n");
        return 1;
    }
    if (change(3, (int[]){2}, 1) != 0) {
        printf("FAIL 2\n");
        return 1;
    }
    if (change(10, (int[]){1, 2, 5}, 3) != 10) {
        printf("FAIL 3\n");
        return 1;
    }
    if (change(0, (int[]){1, 2}, 2) != 1) {
        printf("FAIL 4\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS