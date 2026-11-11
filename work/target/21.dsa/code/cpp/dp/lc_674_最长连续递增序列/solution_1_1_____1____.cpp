// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130771608
// LeetCode 674. 最长连续递增序列 — C++ 版（方案1）
#include <algorithm>                                        // 引入头文件
#include <cassert>                                          // 引入头文件
#include <iostream>                                         // 引入头文件
#include <vector>                                           // 引入头文件
static int findLengthOfLCIS(const std::vector<int> &nums) { // 定义函数/方法 findLengthOfLCIS
    if (nums.empty())
        return 0;                              // 若 数组 是否为空，直接返回 0
    int best = 1, cur = 1;                     // 把 1, 当前值 赋值为 1 存入 当前最优
    for (size_t i = 1; i < nums.size(); ++i) { // 让 下标 i 从 1 开始计数，下标 i 小于 数组.大小() 就继续
        if (nums[i] > nums[i - 1]) {
            ++cur;
            best = std::max(best, cur);
        } else
            cur = 1; // 否则
    }
    return best; // 返回 当前最优
}
int main() {
    assert(findLengthOfLCIS({1, 3, 5, 4, 7}) == 3);
    assert(findLengthOfLCIS({2, 2, 2, 2, 2}) == 1);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS