// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134588341
// LeetCode 541. 反转字符串II — C++ 版（方案1）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <string>    // 引入头文件
static std::string reverseStr(const std::string &s, int k) {
    std::string out = s; // 把 字符串; 写入 std::string out
    for (size_t i = 0; i < s.size();
         i += 2 * static_cast<size_t>(k)) { // 让 下标 i 从 0 开始计数，下标 i 小于 字符串.大小() 就继续
        size_t end = std::min(i + static_cast<size_t>(k), s.size());
        std::reverse(out.begin() + i,
                     out.begin() + end); // std::reverse(out 迭代位置 加 下标 i, out 迭代位置 加 终点);
    }
    return out; // 返回 out
}
int main() {
    assert(reverseStr("abcdefg", 2) == "bacdfeg");
    assert(reverseStr("abcd", 2) == "bacd");
    assert(reverseStr("abc", 1) == "abc");
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS