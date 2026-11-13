// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138481618
// LeetCode 2042. 检查句子中的数字是否递增 — C++ 版（方案2）
#include <cassert>                                      // 引入头文件
#include <cctype>                                       // 引入头文件
#include <iostream>                                     // 引入头文件
#include <sstream>                                      // 引入头文件
#include <string>                                       // 引入头文件
static bool areNumbersAscending(const std::string &s) { // 定义函数/方法 areNumbersAscending
    long long prev = -1;                                // 把 减 1 存入 前一个
    std::istringstream iss(s);                          // std::istringstream iss(字符串);
    std::string tok;                                    // std::string tok;
    while (iss >> tok) {                                // 循环，直到不满足「iss 超过 超过 tok」
        if (std::isdigit(static_cast<unsigned char>(
                tok[0]))) { // 若 std::isdigit(static_cast 小于 unsigned char 超过 (tok[0]
            long long num = std::stoll(tok); // 把 std::stoll(tok) 存入 num
            if (num <= prev)
                return false; // 若 num 不超过 前一个，直接返回 false
            prev = num;       // 把 num; 写入 前一个
        }
    }
    return true; // 返回 true
}
int main() { // 程序入口：跑内嵌自测用例
    assert(areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles")); // 断言校验
    assert(!areNumbersAscending("hello world 5 x 5"));                                   // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
