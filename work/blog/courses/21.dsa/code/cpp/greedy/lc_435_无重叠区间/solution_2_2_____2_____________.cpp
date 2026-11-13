// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135941089
// LeetCode 435. 无重叠区间 — C++ 版（方案2）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件
static int
eraseOverlapIntervals(std::vector<std::vector<int>> intervals) { // 定义函数/方法 eraseOverlapIntervals
    if (intervals.empty())
        return 0; // 若 intervals 是否为空，直接返回 0
    std::sort(intervals.begin(), intervals.end(), [](auto &a, auto &b) { return a[1] < b[1]; });
    int count = 1;             // 把 1 存入 计数
    int end = intervals[0][1]; // 把 intervals[0][1] 存入 终点
    for (size_t i = 1; i < intervals.size();
         ++i) { // 让 下标 i 从 1 开始计数，下标 i 小于 intervals.大小() 就继续
        if (intervals[i][0] >= end) {
            ++count;
            end = intervals[i][1];
        }
    }
    return static_cast<int>(intervals.size()) -
           count; // 返回 static_cast 小于 int 超过 (intervals.大小()) 减 计数
}
int main() { // 程序入口：跑内嵌自测用例
    assert(eraseOverlapIntervals({{1, 2}, {2, 3}, {3, 4}, {1, 3}}) == 1); // 断言校验
    assert(eraseOverlapIntervals({}) == 0);                               // 断言校验
    assert(eraseOverlapIntervals({{1, 2}, {1, 2}, {1, 2}}) == 2);         // 断言校验
    std::cout << "PASS" << std::endl;                                     // 全部用例通过，输出 PASS
    return 0;                                                             // 返回 0
}
