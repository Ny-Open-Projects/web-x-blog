// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130753613
// LeetCode 392. 判断子序列 — C++ 版（方案1）
#include <cassert>                                                      // 引入头文件
#include <iostream>                                                     // 引入头文件
#include <string>                                                       // 引入头文件
static bool isSubsequence(const std::string &s, const std::string &t) { // 定义判定函数 isSubsequence
    size_t i = 0;                                                       // 把 0; 写入 size_t i
    for (char c : t) { // for (char 字符 : 另一字符串) {
        if (i < s.size() && s[i] == c)
            ++i; // 若 下标 i 小于 字符串.大小() 且 字符串[下标 i] 等于 字符) 加一 下标 i;
    }
    return i == s.size(); // 返回 下标 i 等于 字符串.大小()
}
int main() {
    assert(isSubsequence("abc", "ahbgdc"));
    assert(!isSubsequence("axc", "ahbgdc"));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS