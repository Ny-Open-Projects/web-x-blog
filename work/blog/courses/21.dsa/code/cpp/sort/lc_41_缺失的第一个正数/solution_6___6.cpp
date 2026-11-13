// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066015
// LeetCode 41. 缺失的第一个正数 — C++ 版（方案6）
#include <algorithm>                                            // 引入头文件
#include <cassert>                                              // 引入头文件
#include <iostream>                                             // 引入头文件
#include <vector>                                               // 引入头文件
static int firstMissingPositive(const std::vector<int> &nums) { // 定义函数/方法 firstMissingPositive
    if (nums.empty())
        return 1;         // 若 数组 是否为空，直接返回 1
    std::vector<int> pos; // std::vector 小于 int 超过 pos;
    for (int v : nums)
        if (v > 0)
            pos.push_back(v); // for (int 值 : 数组) if (值 超过 0) pos 追加 值);
    if (pos.empty())
        return 1;                      // 若 pos 是否为空，直接返回 1
    std::sort(pos.begin(), pos.end()); // std::sort(pos 迭代位置 , pos.终点());
    if (pos[0] != 1)
        return 1; // 若 pos[0] 不等于 1，直接返回 1
    for (size_t i = 0; i + 1 < pos.size();
         ++i) { // 让 下标 i 从 0 开始计数，下标 i 加 1 小于 pos.大小() 就继续
        if (pos[i + 1] - pos[i] > 1)
            return pos[i] + 1; // 若 pos[下标 i 加 1] 减 pos[下标 i] 超过 1，直接返回 pos[下标 i] 加 1
    }
    return pos.back() + 1; // 返回 pos.back() 加 1
}
int main() {                                              // 程序入口：跑内嵌自测用例
    assert(firstMissingPositive({1, 2, 0}) == 3);         // 断言校验
    assert(firstMissingPositive({3, 4, -1, 1}) == 2);     // 断言校验
    assert(firstMissingPositive({7, 8, 9, 11, 12}) == 1); // 断言校验
    assert(firstMissingPositive({}) == 1);                // 断言校验
    std::cout << "PASS" << std::endl;                     // 全部用例通过，输出 PASS
    return 0;                                             // 返回 0
}
