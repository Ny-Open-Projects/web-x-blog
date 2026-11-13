// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130521152
// LeetCode 746. 使用最小花费爬楼梯 — C++ 版（方案5）
#include <algorithm>                                             // 引入头文件
#include <cassert>                                               // 引入头文件
#include <iostream>                                              // 引入头文件
#include <vector>                                                // 引入头文件
static int minCostClimbingStairs(const std::vector<int> &cost) { // 定义函数/方法 minCostClimbingStairs
    int a = 0, b = 0;                                            // 把 0, b 赋值为 0 存入 数组
    for (size_t i = 2; i <= cost.size(); ++i) { // 让 下标 i 从 2 开始计数，下标 i 不超过 cost.大小() 就继续
        int t = std::min(a + cost[i - 2], b + cost[i - 1]);
        a = b;
        b = t; // 把 b; b 赋值为 另一字符串; 写入 数组
    }
    return b; // 返回 b
}
int main() {
    assert(minCostClimbingStairs({10, 15, 20}) == 15);
    assert(minCostClimbingStairs({1, 100, 1, 1, 1, 100, 1, 1, 100, 1}) == 6);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS