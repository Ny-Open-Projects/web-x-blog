// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134135902
// LeetCode 344. 反转字符串 — C++ 版（方案1）
#include <algorithm>                              // 引入头文件
#include <cassert>                                // 引入头文件
#include <iostream>                               // 引入头文件
#include <string>                                 // 引入头文件
static std::string reverseString(std::string s) { // static std::string reverseString(std::string 字符串) {
    std::reverse(s.begin(), s.end()); // std::reverse(字符串 迭代位置 , 字符串.终点());
    return s;                         // 返回 字符串
}
int main() {
    assert(reverseString("hello") == "olleh");
    assert(reverseString("Hannah") == "hannaH");
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS