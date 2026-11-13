// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138771574
// LeetCode 93. 复原IP地址 — C++ 版（方案2）
#include <cassert>                           // 引入头文件
#include <iostream>                          // 引入头文件
#include <string>                            // 引入头文件
#include <vector>                            // 引入头文件
static bool validSeg(const std::string &s) { // 定义函数/方法 validSeg
    if (s.empty() || s.size() > 3)
        return false; // 若 字符串 是否为空 或 字符串.大小() 超过 3，直接返回 false
    if (s.size() > 1 && s[0] == '0')
        return false; // 若 字符串.大小() 超过 1 且 字符串[0] 等于 '0'，直接返回 false
    return std::stoi(s) <= 255; // 返回 std::stoi(字符串) 不超过 255
}
static std::vector<std::string> restoreIpAddresses(const std::string &s) {
    std::vector<std::string> res; // std::vector 小于 std::string 超过 结果;
    int n = static_cast<int>(s.size()); // 把 static_cast 小于 int 超过 (字符串.大小()) 存入 元素个数
    if (n < 4 || n > 12)
        return res;              // 若 元素个数 小于 4 或 元素个数 超过 12，直接返回 结果
    for (int a = 1; a <= 3; ++a) // 让 数组 从 1 开始计数，数组 不超过 3 就继续
        for (int b = 1; b <= 3; ++b)       // 让 b 从 1 开始计数，b 不超过 3 就继续
            for (int c = 1; c <= 3; ++c) { // 让 字符 从 1 开始计数，字符 不超过 3 就继续
                int d = n - a - b - c;     // 把 元素个数 减 数组 减 b 减 字符 存入 d
                if (d < 1 || d > 3)
                    continue; // 若 d 小于 1 或 d 超过 3) continue;
                auto s1 = s.substr(0, a), s2 = s.substr(a, b), s3 = s.substr(a + b, c),
                     s4 = s.substr(a + b + c);
                if (validSeg(s1) && validSeg(s2) && validSeg(s3) &&
                    validSeg(s4)) { // 若 validSeg(s1) 且 validSeg(s2) 且 validSeg(s3) 且 validSeg(s4
                    res.push_back(s1 + "." + s2 + "." + s3 + "." +
                                  s4); // 结果 追加 s1 加 「.」 加 s2 加 「.」 加 s3 加 「.」 加 s4);
                }
            }
    return res; // 返回 结果
}
int main() { // 程序入口：跑内嵌自测用例
    assert((restoreIpAddresses("25525511135") ==
            std::vector<std::string>{"255.255.11.135", "255.255.111.35"}));      // 断言校验
    assert((restoreIpAddresses("0000") == std::vector<std::string>{"0.0.0.0"})); // 断言校验
    assert(restoreIpAddresses("abc").empty());                                   // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
