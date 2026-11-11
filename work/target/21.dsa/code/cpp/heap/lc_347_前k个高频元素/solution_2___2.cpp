// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400
// LeetCode 347. 前K个高频元素 — C++ 版（方案2）
#include <algorithm>     // 引入头文件
#include <cassert>       // 引入头文件
#include <iostream>      // 引入头文件
#include <unordered_map> // 引入头文件
#include <vector>        // 引入头文件
static std::vector<int> topKFrequent(const std::vector<int> &nums, int k) {
    std::unordered_map<int, long long> counts; // std::unordered_map 小于 int, long long 超过 counts;
    for (int v : nums)
        ++counts[v]; // for (int 值 : 数组) 加一 counts[值];
    std::vector<std::pair<int, long long>> items(counts.begin(), counts.end());
    std::sort(items.begin(), items.end(), [](auto &a, auto &b) {
        if (a.second != b.second)
            return a.second > b.second; // 若 数组.second 不等于 b.second，直接返回 数组.second 超过 b.second
        return a.first < b.first; // 返回 数组.first 小于 b.first
    });                           // });
    std::vector<int> res;         // std::vector 小于 int 超过 结果;
    for (int i = 0; i < k && i < static_cast<int>(items.size()); ++i)
        res.push_back(items[i].first);
    return res; // 返回 结果
}
int main() {                                        // 程序入口：跑内嵌自测用例
    auto got = topKFrequent({1, 1, 1, 2, 2, 3}, 2); // 把 topKFrequent({1, 1, 1, 2, 2, 3}, 2) 存入 got
    std::sort(got.begin(), got.end());              // std::sort(got 迭代位置 , got.终点());
    assert((got == std::vector<int>{1, 2}));        // 断言校验
    assert((topKFrequent({1}, 1) == std::vector<int>{1})); // 断言校验
    std::cout << "PASS" << std::endl;                      // 全部用例通过，输出 PASS
    return 0;                                              // 返回 0
}
