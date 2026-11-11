// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134934324
// LeetCode 914. 卡牌分组 — C++ 版（方案5）
#include <cassert>                                         // 引入头文件
#include <iostream>                                        // 引入头文件
#include <numeric>                                         // 引入头文件
#include <unordered_map>                                   // 引入头文件
#include <vector>                                          // 引入头文件
static bool hasGroupsSizeX(const std::vector<int> &deck) { // 定义函数/方法 hasGroupsSizeX
    std::unordered_map<int, int> counts; // std::unordered_map 小于 int, int 超过 counts;
    for (int c : deck)
        ++counts[c]; // for (int 字符 : deck) 加一 counts[字符];
    int g = 0;       // 把 0 存入 g
    for (auto &[_, v] : counts)
        g = std::gcd(g, v); // 把 std::gcd(g, 值); 写入 for (auto &[_, v] : counts) g
    return g >= 2;          // 返回 g 不低于 2
}
int main() {
    assert(hasGroupsSizeX({1, 2, 3, 4, 4, 3, 2, 1}));
    assert(!hasGroupsSizeX({1, 1, 1, 2, 2, 2, 3, 3}));
    assert(!hasGroupsSizeX({1}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS