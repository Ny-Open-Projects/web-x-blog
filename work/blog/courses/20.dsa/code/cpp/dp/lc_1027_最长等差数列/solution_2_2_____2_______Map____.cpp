// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130687299
// LeetCode 1027. 最长等差数列 — C++ 版（方案2）
#include <cassert>                                               // 引入头文件
#include <iostream>                                              // 引入头文件
#include <unordered_map>                                         // 引入头文件
#include <vector>                                                // 引入头文件
static int longestArithSeqLength(const std::vector<int> &nums) { // 定义函数/方法 longestArithSeqLength
    size_t n = nums.size();                                      // 把 数组.大小(); 写入 size_t n
    std::vector<std::unordered_map<int, int>> dp(n);
    int best = 1;                    // 把 1 存入 当前最优
    for (size_t i = 0; i < n; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (size_t j = 0; j < i; ++j) { // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
            int d = nums[i] - nums[j];   // 把 数组[下标 i] 减 数组[下标 j] 存入 d
            int cur = dp[j].count(d) ? dp[j][d] + 1
                                     : 2; // 把 DP 表[下标 j].计数(d) ? DP 表[下标 j][d] 加 1 : 2 存入 当前值
            dp[i][d] = cur;               // 把 当前值; 写入 dp[i][d]
            best = std::max(best, cur); // 把 std::取较大值 当前最优, 当前值); 写入 当前最优
        }
    }
    return best; // 返回 当前最优
}
int main() {
    assert(longestArithSeqLength({9, 4, 7, 2, 10}) == 3);
    assert(longestArithSeqLength({3, 6, 9, 12}) == 4);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS