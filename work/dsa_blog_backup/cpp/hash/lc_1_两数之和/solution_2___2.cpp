// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130663853
// LeetCode 1. 两数之和 — C++ 版（方案2：哈希表一次遍历）
#include <cassert>       // 引入头文件
#include <iostream>      // 引入头文件
#include <unordered_map> // 引入头文件
#include <vector>        // 引入头文件
static std::vector<int> twoSum(const std::vector<int> &nums, int target) {
    std::unordered_map<int, int> seen; // std::unordered_map 小于 int, int 超过 已见集合;
    for (int i = 0; i < static_cast<int>(nums.size());
         ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 static_cast 小于 int 超过 (数组.大小()) 就继续
        auto it = seen.find(target - nums[i]); // 把 已见集合 查找 目标值 减 数组[下标 i]) 存入 it
        if (it != seen.end())
            return {it->second, i}; // 若 it 不等于 已见集合.终点()，直接返回 {it 减 超过 second, 下标 i}
        seen[nums[i]] = i; // 把 下标 i; 写入 seen[nums[i]]
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
