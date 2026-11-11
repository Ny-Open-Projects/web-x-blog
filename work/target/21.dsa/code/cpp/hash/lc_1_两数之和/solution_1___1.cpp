// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130663853
// LeetCode 1. 两数之和 — C++ 版（方案1：暴力双循环）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> twoSum(const std::vector<int> &nums, int target) {
    int n = static_cast<int>(nums.size()); // 把 static_cast 小于 int 超过 (数组.大小()) 存入 元素个数
    for (int i = 0; i < n; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (int j = i + 1; j < n; ++j) { // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 元素个数 就继续
            if (nums[i] + nums[j] == target)
                return {i, j}; // 若 数组[下标 i] 加 数组[下标 j] 等于 目标值，直接返回 {下标 i, 下标 j}
        }
    }
    return {}; // 返回 {}
}
int main() {                                                       // 程序入口：跑内嵌自测用例
    assert((twoSum({2, 7, 11, 15}, 9) == std::vector<int>{0, 1})); // 断言校验
    assert((twoSum({3, 2, 4}, 6) == std::vector<int>{1, 2}));      // 断言校验
    assert((twoSum({3, 3}, 6) == std::vector<int>{0, 1}));         // 断言校验
    std::cout << "PASS" << std::endl;                              // 全部用例通过，输出 PASS
    return 0;                                                      // 返回 0
}
