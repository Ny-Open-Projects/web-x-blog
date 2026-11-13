// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133834060
// LeetCode 2407. 最长递增子序列II — C++ 版（方案1）
#include <algorithm>                                          // 引入头文件
#include <cassert>                                            // 引入头文件
#include <iostream>                                           // 引入头文件
#include <vector>                                             // 引入头文件
static int lengthOfLIS(const std::vector<int> &nums, int k) { // 定义函数/方法 lengthOfLIS
    int n = static_cast<int>(nums.size()); // 把 static_cast 小于 int 超过 (数组.大小()) 存入 元素个数
    std::vector<int> dp(n, 1);             // std::vector 小于 int 超过 DP 表(元素个数, 1);
    int best = 0;                          // 把 0 存入 当前最优
    for (int i = 0; i < n; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (int j = 0; j < i; ++j) { // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
            if (nums[j] < nums[i] && nums[i] - nums[j] <= k)
                dp[i] = std::max(dp[i], dp[j] + 1);
        }
        best = std::max(best, dp[i]); // 把 std::取较大值 当前最优, DP 表[下标 i]); 写入 当前最优
    }
    return best; // 返回 当前最优
}
int main() {
    assert(lengthOfLIS({4, 2, 1, 4, 3, 4, 5, 8, 15}, 3) == 5);
    assert(lengthOfLIS({1}, 1) == 1);
    assert(lengthOfLIS({}, 3) == 0);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS