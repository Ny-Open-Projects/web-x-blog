// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145582435
// LeetCode 3105. 最长的严格递增或递减子数组 — C++ 版（方案2）
#include <algorithm>                                                // 引入头文件
#include <cassert>                                                  // 引入头文件
#include <iostream>                                                 // 引入头文件
#include <vector>                                                   // 引入头文件
static int longestMonotonicSubarray(const std::vector<int> &nums) { // 定义函数/方法 longestMonotonicSubarray
    if (nums.empty())
        return 0;                   // 若 数组 是否为空，直接返回 0
    int inc = 1, dec = 1, best = 1; // 把 1, dec 赋值为 1, 当前最优 赋值为 1 存入 inc
    for (size_t i = 1; i < nums.size(); ++i) { // 让 下标 i 从 1 开始计数，下标 i 小于 数组.大小() 就继续
        if (nums[i] > nums[i - 1]) {
            ++inc;
            dec = 1;
        } // 若 数组[下标 i] 超过 数组[下标 i 减 1]) { 加一 inc; dec 赋值为 1; }
        else if (nums[i] < nums[i - 1]) {
            ++dec;
            inc = 1;
        } // 否则，若 数组[下标 i] 小于 数组[下标 i 减 1]) { 加一 dec; inc 赋值为 1; }
        else {
            inc = 1;
            dec = 1;
        }                                  // 否则
        best = std::max({best, inc, dec}); // 把 std::取较大值 {当前最优, inc, dec}); 写入 当前最优
    }
    return best; // 返回 当前最优
}
int main() {
    assert(longestMonotonicSubarray({1, 2, 3, 4, 5}) == 5);
    assert(longestMonotonicSubarray({5, 4, 3, 2, 1}) == 5);
    assert(longestMonotonicSubarray({1, 4, 3, 2, 5}) == 3);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS