// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133904873
// LeetCode 148. 排序链表 — C++ 版（方案6）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件
static std::vector<int> sortList(std::vector<int> vals) {
    std::sort(vals.begin(), vals.end()); // std::sort(vals 迭代位置 , vals.终点());
    return vals;                         // 返回 vals
}
int main() {                                                          // 程序入口：跑内嵌自测用例
    assert((sortList({4, 2, 1, 3}) == std::vector<int>{1, 2, 3, 4})); // 断言校验
    assert((sortList({-1, 5, 3, 4, 0}) == std::vector<int>{-1, 0, 3, 4, 5})); // 断言校验
    assert(sortList({}).empty());                                             // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
