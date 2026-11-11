// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133657416
// LeetCode 92. 反转链表II — C++ 版（方案1）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件
static std::vector<int> reverseBetween(std::vector<int> vals, int left, int right) {
    std::reverse(vals.begin() + (left - 1),
                 vals.begin() +
                     right); // std::reverse(vals 迭代位置 加 (左边界 减 1), vals 迭代位置 加 右边界);
    return vals;             // 返回 vals
}
int main() { // 程序入口：跑内嵌自测用例
    assert((reverseBetween({1, 2, 3, 4, 5}, 2, 4) == std::vector<int>{1, 4, 3, 2, 5})); // 断言校验
    assert((reverseBetween({1, 2, 3, 4, 5}, 1, 4) == std::vector<int>{4, 3, 2, 1, 5})); // 断言校验
    assert((reverseBetween({5}, 1, 1) == std::vector<int>{5}));                         // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
