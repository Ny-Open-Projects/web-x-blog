// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130771847
// LeetCode 673. 最长递增子序列的个数 — C++ 版（方案2）
#include <algorithm>                                       // 引入头文件
#include <cassert>                                         // 引入头文件
#include <iostream>                                        // 引入头文件
#include <vector>                                          // 引入头文件
static int findNumberOfLIS(const std::vector<int> &nums) { // 定义函数/方法 findNumberOfLIS
    size_t n = nums.size();                                // 把 数组.大小(); 写入 size_t n
    std::vector<int> dp(n, 1), cnt(n, 1); // std::vector 小于 int 超过 DP 表(元素个数, 1), 计数(元素个数, 1);
    int best = 0, res = 0;                // 把 0, 结果 赋值为 0 存入 当前最优
    for (size_t i = 0; i < n; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (size_t j = 0; j < i; ++j) { // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
            if (nums[j] < nums[i]) {     // 若 数组[下标 j] 小于 数组[下标 i]
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
int main() {
    assert(findNumberOfLIS({1, 3, 5, 4, 7}) == 2);
    assert(findNumberOfLIS({2, 2, 2, 2, 2}) == 5);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS