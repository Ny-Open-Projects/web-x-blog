// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107435426
// 字典序最大问题分析 — C++ 版（方案4）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件
static std::vector<int> lexicographicallyLargest(int n, std::vector<int> arr) {
    std::sort(arr.begin(), arr.end(),
              std::greater<int>()); // std::sort(数组 迭代位置 , 数组.终点(), std::greater 小于 int 超过 ());
    arr.resize(static_cast<size_t>(n)); // 数组.resize(static_cast 小于 size_t 超过 (元素个数));
    return arr;                         // 返回 数组
}
int main() { // 程序入口：跑内嵌自测用例
    assert((lexicographicallyLargest(3, {1, 2, 3}) == std::vector<int>{3, 2, 1}));       // 断言校验
    assert((lexicographicallyLargest(4, {4, 2, 9, 7}) == std::vector<int>{9, 7, 4, 2})); // 断言校验
    assert((lexicographicallyLargest(2, {5, 1}) == std::vector<int>{5, 1}));             // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS