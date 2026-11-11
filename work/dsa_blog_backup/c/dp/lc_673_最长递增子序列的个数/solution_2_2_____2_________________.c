/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130771847 */
/* LeetCode 673. 最长递增子序列的个数 — C 版（方案2） */
#include <stdio.h>                                      // 引入头文件
static int find_number_of_lis(const int *nums, int n) { // 定义函数/方法 find_number_of_lis
    int dp[4096], cnt[4096];                            // int DP 表[4096], 计数[4096];
    int best = 0, res = 0;                              // 把 0, 结果 赋值为 0 存入 当前最优
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        dp[i] = 1;
        cnt[i] = 1;                   // 把 1; 计数[下标 i] 赋值为 1; 写入 dp[i]
        for (int j = 0; j < i; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
            if (nums[j] < nums[i]) {  // 若 数组[下标 j] 小于 数组[下标 i]
                if (dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    cnt[i] = cnt[j];
                } else if (dp[j] + 1 == dp[i])
                    cnt[i] += cnt[j]; // 否则，若 DP 表[下标 j] 加 1 等于 DP 表[下标 i]) 计数[下标 i] 累加
                                      // 计数[下标 j];
            }
        }
        if (dp[i] > best) {
            best = dp[i];
            res = cnt[i];
        } else if (dp[i] == best)
            res += cnt[i]; // 否则，若 DP 表[下标 i] 等于 当前最优) 结果 累加 计数[下标 i];
    }
    return res; // 返回 结果
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (find_number_of_lis((int[]){1, 3, 5, 4, 7}, 5) != 2) {
        printf("FAIL 1\n");
        return 1;
    }
    if (find_number_of_lis((int[]){2, 2, 2, 2, 2}, 5) != 5) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS