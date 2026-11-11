// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135154838
// LeetCode 242. 有效的字母异位词 — C++ 版（方案1）
#include <algorithm>                                  // 引入头文件
#include <cassert>                                    // 引入头文件
#include <iostream>                                   // 引入头文件
#include <string>                                     // 引入头文件
static bool isAnagram(std::string s, std::string t) { // 定义判定函数 isAnagram
    if (s.size() != t.size())
        return false; // 若 字符串.大小() 不等于 另一字符串.大小()，直接返回 false
    std::sort(s.begin(), s.end()); // std::sort(字符串 迭代位置 , 字符串.终点());
    std::sort(t.begin(), t.end()); // std::sort(另一字符串 迭代位置 , 另一字符串.终点());
    return s == t;                 // 返回 字符串 等于 另一字符串
}
int main() {                                 // 程序入口：跑内嵌自测用例
    assert(isAnagram("anagram", "nagaram")); // 断言校验
    assert(!isAnagram("rat", "car"));        // 断言校验
    std::cout << "PASS" << std::endl;        // 全部用例通过，输出 PASS
    return 0;                                // 返回 0
}
