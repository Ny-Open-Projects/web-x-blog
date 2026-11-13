// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133845474
// LeetCode 15. 三数之和 — C++ 版（方案1）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件
static std::vector<std::vector<int>> threeSum(std::vector<int> nums) {
    std::sort(nums.begin(), nums.end()); // std::sort(数组 迭代位置 , 数组.终点());
    std::vector<std::vector<int>> ans;   // std::vector 小于 std::vector 小于 int 超过 超过 答案;
    int n = static_cast<int>(nums.size()); // 把 static_cast 小于 int 超过 (数组.大小()) 存入 元素个数
    for (int first = 0; first < n; ++first) { // 让 first 从 0 开始计数，first 小于 元素个数 就继续
        if (first > 0 && nums[first] == nums[first - 1])
            continue;      // 若 first 超过 0 且 数组[first] 等于 数组[first 减 1]) continue;
        int third = n - 1; // 把 元素个数 减 1 存入 third
        int target = -nums[first]; // 把 减 数组[first] 存入 目标值
        for (int second = first + 1; second < n;
             ++second) { // 让 second 从 first 加 1 开始计数，second 小于 元素个数 就继续
            if (second > first + 1 && nums[second] == nums[second - 1])
                continue;
            while (second < third && nums[second] + nums[third] > target)
                --third;
            if (second == third)
                break;                                  // 若 second 等于 third) break;
            if (nums[second] + nums[third] == target) { // 若 数组[second] 加 数组[third] 等于 目标值
                ans.push_back({nums[first], nums[second],
                               nums[third]}); // 答案 追加 {数组[first], 数组[second], 数组[third]});
            }
        }
    }
    return ans; // 返回 答案
}
int main() {                                    // 程序入口：跑内嵌自测用例
    auto got = threeSum({-1, 0, 1, 2, -1, -4}); // 把 threeSum({ 减 1, 0, 1, 2, 减 1, 减 4}) 存入 got
    std::sort(got.begin(), got.end());          // std::sort(got 迭代位置 , got.终点());
    assert((got == std::vector<std::vector<int>>{{{-1, -1, 2}, {-1, 0, 1}}})); // 断言校验
    auto g2 = threeSum({0, 0, 0});                                  // 把 threeSum({0, 0, 0}) 存入 g2
    assert(g2.size() == 1 && g2[0] == std::vector<int>({0, 0, 0})); // 断言校验
    std::cout << "PASS" << std::endl;                               // 全部用例通过，输出 PASS
    return 0;                                                       // 返回 0
}
