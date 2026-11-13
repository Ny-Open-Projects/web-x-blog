// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133894317
// LeetCode 18. 四数之和 — C++ 版（方案2）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件
static std::vector<std::vector<int>> fourSum(std::vector<int> nums, int target) {
    std::sort(nums.begin(), nums.end()); // std::sort(数组 迭代位置 , 数组.终点());
    std::vector<std::vector<int>> res;   // std::vector 小于 std::vector 小于 int 超过 超过 结果;
    int n = static_cast<int>(nums.size()); // 把 static_cast 小于 int 超过 (数组.大小()) 存入 元素个数
    for (int i = 0; i < n; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        if (i > 0 && nums[i] == nums[i - 1])
            continue; // 若 下标 i 超过 0 且 数组[下标 i] 等于 数组[下标 i 减 1]) continue;
        for (int j = i + 1; j < n; ++j) { // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 元素个数 就继续
            if (j > i + 1 && nums[j] == nums[j - 1])
                continue; // 若 下标 j 超过 下标 i 加 1 且 数组[下标 j] 等于 数组[下标 j 减 1]) continue;
            int left = j + 1, right = n - 1; // 把 下标 j 加 1, 右边界 赋值为 元素个数 减 1 存入 左边界
            while (left < right) { // 循环，直到不满足「左边界 小于 右边界」
                long long s = static_cast<long long>(nums[i]) + nums[j] + nums[left] + nums[right];
                if (s == target) { // 若 字符串 等于 目标值
                    res.push_back(
                        {nums[i], nums[j], nums[left], nums[right]}); // 结果 追加 {数组[下标 i], 数组[下标
                                                                      // j], 数组[左边界], 数组[右边界]});
                    ++left;
                    --right; // 加一 左边界; 减一 右边界;
                    while (left < right && nums[left] == nums[left - 1])
                        ++left; // 循环，直到不满足「左边界 小于 右边界 且 数组[左边界] 等于 数组[左边界 减
                                // 1]) 加一 左边界;」
                    while (left < right && nums[right] == nums[right + 1])
                        --right; // 循环，直到不满足「左边界 小于 右边界 且 数组[右边界] 等于 数组[右边界 加
                                 // 1]) 减一 右边界;」
                } else if (s < target)
                    ++left; // 否则，若 字符串 小于 目标值) 加一 左边界;
                else
                    --right; // 否则
            }
        }
    }
    return res; // 返回 结果
}
int main() {                                     // 程序入口：跑内嵌自测用例
    auto got = fourSum({1, 0, -1, 0, -2, 2}, 0); // 把 fourSum({1, 0, 减 1, 0, 减 2, 2}, 0) 存入 got
    assert(got.size() == 3);                     // 断言校验
    std::cout << "PASS" << std::endl;            // 全部用例通过，输出 PASS
    return 0;                                    // 返回 0
}
