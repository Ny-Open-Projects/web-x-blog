// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135949307
// LeetCode 452. 用最少数量的箭引爆气球 — C++ 版（方案1）
#include <algorithm>                                                 // 引入头文件
#include <cassert>                                                   // 引入头文件
#include <iostream>                                                  // 引入头文件
#include <vector>                                                    // 引入头文件
static int findMinArrowShots(std::vector<std::vector<int>> points) { // 定义函数/方法 findMinArrowShots
    if (points.empty())
        return 0; // 若 points 是否为空，直接返回 0
    std::sort(points.begin(), points.end(), [](auto &a, auto &b) { return a[1] < b[1]; });
    int arrows = 1;                              // 把 1 存入 arrows
    int end = points[0][1];                      // 把 points[0][1] 存入 终点
    for (size_t k = 1; k < points.size(); ++k) { // 让 下标 k 从 1 开始计数，下标 k 小于 points.大小() 就继续
        if (points[k][0] > end) {
            ++arrows;
            end = points[k][1];
        }
    }
    return arrows; // 返回 arrows
}
int main() { // 程序入口：跑内嵌自测用例
    assert(findMinArrowShots({{10, 16}, {2, 8}, {1, 6}, {7, 12}}) == 2); // 断言校验
    assert(findMinArrowShots({}) == 0);                                  // 断言校验
    assert(findMinArrowShots({{1, 2}, {3, 4}, {5, 6}, {7, 8}}) == 4);    // 断言校验
    std::cout << "PASS" << std::endl;                                    // 全部用例通过，输出 PASS
    return 0;                                                            // 返回 0
}
