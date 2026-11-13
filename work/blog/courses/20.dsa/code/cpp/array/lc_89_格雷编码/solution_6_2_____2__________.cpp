// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134866839
// LeetCode 89. 格雷编码 — C++ 版（方案6）
#include <cassert>                        // 引入头文件
#include <iostream>                       // 引入头文件
#include <vector>                         // 引入头文件
static std::vector<int> grayCode(int n) { // static std::vector 小于 int 超过 grayCode(int 元素个数) {
    int m = 1 << n;                       // 把 1 小于 小于 元素个数 存入 映射表
    std::vector<int> out;                 // std::vector 小于 int 超过 out;
    out.reserve(m);                       // out.reserve(映射表);
    for (int i = 0; i < m; ++i)
        out.push_back(i ^ (i >> 1)); // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
    return out;                      // 返回 out
}
int main() {                                               // 程序入口：跑内嵌自测用例
    assert((grayCode(2) == std::vector<int>{0, 1, 3, 2})); // 断言校验
    assert((grayCode(1) == std::vector<int>{0, 1}));       // 断言校验
    auto g3 = grayCode(3);                                 // 把 grayCode(3) 存入 g3
    assert(g3.size() == 8);                                // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS