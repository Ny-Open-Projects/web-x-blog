// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
// 数据结构与算法笔记: 复杂度 — C++ 版（方案8）
#include <cassert>                  // 引入头文件
#include <iostream>                 // 引入头文件
static long long funcCalls(int n) { // static long long funcCalls(int 元素个数) {
    if (n <= 1)
        return 1;                // 若 元素个数 不超过 1，直接返回 1
    return 2 * funcCalls(n - 1); // 返回 2 乘 funcCalls(元素个数 减 1)
}
int main() {
    assert(funcCalls(1) == 1);
    assert(funcCalls(2) == 2);
    assert(funcCalls(5) == 16);
    assert(funcCalls(10) == 512);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS