// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130683917
// LeetCode 322. 零钱兑换 — C++ 版（方案2）
#include <algorithm>                                               // 引入头文件
#include <cassert>                                                 // 引入头文件
#include <iostream>                                                // 引入头文件
#include <vector>                                                  // 引入头文件
static int coinChange(const std::vector<int> &coins, int amount) { // 定义函数/方法 coinChange
    std::vector<int> dp(amount + 1, -1); // std::vector 小于 int 超过 DP 表(目标金额 加 1, 减 1);
    dp[0] = 0;                           // 把 0; 写入 dp[0]
    for (int a = 1; a <= amount; ++a) { // 让 数组 从 1 开始计数，数组 不超过 目标金额 就继续
        for (int c : coins) {           // for (int 字符 : 硬币面额) {
            if (c <= a && dp[a - c] != -1) { // 若 字符 不超过 数组 且 DP 表[数组 减 字符] 不等于 减 1
                if (dp[a] == -1 || dp[a - c] + 1 < dp[a])
                    dp[a] = dp[a - c] + 1;
            }
        }
    }
    return dp[amount]; // 返回 DP 表[目标金额]
}
int main() {
    assert(coinChange({1, 2, 5}, 11) == 3);
    assert(coinChange({2}, 3) == -1);
    assert(coinChange({1}, 0) == 0);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS