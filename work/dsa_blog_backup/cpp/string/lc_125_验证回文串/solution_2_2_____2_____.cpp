// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130778527
// LeetCode 125. 验证回文串 — C++ 版（方案2）
#include <cassert>                               // 引入头文件
#include <cctype>                                // 引入头文件
#include <iostream>                              // 引入头文件
#include <string>                                // 引入头文件
static bool isPalindrome(const std::string &s) { // 定义判定函数 isPalindrome
    std::string f;                               // std::string f;
    for (char c : s) {                           // for (char 字符 : 字符串) {
        if (std::isalnum(static_cast<unsigned char>(c)))
            f.push_back(static_cast<char>(std::tolower(static_cast<unsigned char>(c))));
    }
    size_t i = 0, j = f.size(); // 把 0, 下标 j 赋值为 f.大小(); 写入 size_t i
    if (j == 0)
        return true; // 若 下标 j 等于 0，直接返回 true
    --j;             // 减一 下标 j;
    while (i < j) {  // 循环，直到不满足「下标 i 小于 下标 j」
        if (f[i] != f[j])
            return false; // 若 f[下标 i] 不等于 f[下标 j]，直接返回 false
        ++i;
        --j; // 加一 下标 i; 减一 下标 j;
    }
    return true; // 返回 true
}
int main() {                                                // 程序入口：跑内嵌自测用例
    assert(isPalindrome("A man, a plan, a canal: Panama")); // 断言校验
    assert(!isPalindrome("race a car"));                    // 断言校验
    assert(isPalindrome(" "));                              // 断言校验
    std::cout << "PASS" << std::endl;                       // 全部用例通过，输出 PASS
    return 0;                                               // 返回 0
}
