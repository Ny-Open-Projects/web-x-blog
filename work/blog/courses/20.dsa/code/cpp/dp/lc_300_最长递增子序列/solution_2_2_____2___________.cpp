// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130727613
// LeetCode 300. 最长递增子序列 — C++ 版（方案2）
#include <algorithm>                                   // 引入头文件
#include <cassert>                                     // 引入头文件
#include <iostream>                                    // 引入头文件
#include <vector>                                      // 引入头文件
static int lengthOfLIS(const std::vector<int> &nums) { // 定义函数/方法 lengthOfLIS
    std::vector<int> dp(nums.size(), 1); // std::vector 小于 int 超过 DP 表(数组.大小(), 1);
    int best = 0;                        // 把 0 存入 当前最优
    for (size_t i = 0; i < nums.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
        for (size_t j = 0; j < i; ++j) // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
            if (nums[j] < nums[i])
                dp[i] = std::max(dp[i], dp[j] + 1);
        best = std::max(best, dp[i]); // 把 std::取较大值 当前最优, DP 表[下标 i]); 写入 当前最优
    }
    return best; // 返回 当前最优
}
int main() {
    assert(lengthOfLIS({10, 9, 2, 5, 3, 7, 101, 18}) == 4);
    assert(lengthOfLIS({0, 1, 0, 3, 2, 3}) == 4);
    assert(lengthOfLIS({7, 7, 7, 7}) == 1);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS