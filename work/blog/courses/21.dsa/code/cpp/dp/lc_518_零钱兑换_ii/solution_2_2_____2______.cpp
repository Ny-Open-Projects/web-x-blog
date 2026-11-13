// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734179
// LeetCode 518. 零钱兑换II — C++ 版（方案2）
#include <cassert>                                             // 引入头文件
#include <iostream>                                            // 引入头文件
#include <vector>                                              // 引入头文件
static int change(int amount, const std::vector<int> &coins) { // 定义函数/方法 change
    std::vector<long long> dp(amount + 1, 0); // std::vector 小于 long long 超过 DP 表(目标金额 加 1, 0);
    dp[0] = 1;                                // 把 1; 写入 dp[0]
    for (int c : coins) {                     // for (int 字符 : 硬币面额) {
        for (int a = c; a <= amount; ++a)
            dp[a] += dp[a - c]; // 让 数组 从 字符 开始计数，数组 不超过 目标金额 就继续
    }
    return static_cast<int>(dp[amount]); // 返回 static_cast 小于 int 超过 (DP 表[目标金额])
}
int main() {
    assert(change(5, {1, 2, 5}) == 4);
    assert(change(3, {2}) == 0);
    assert(change(10, {1, 2, 5}) == 10);
    assert(change(0, {1, 2}) == 1);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS