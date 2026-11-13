// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138290964
// LeetCode 482. 密钥格式化 — C++ 版（方案1）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <cctype>    // 引入头文件
#include <iostream>  // 引入头文件
#include <string>    // 引入头文件
static std::string licenseKeyFormatting(const std::string &s, int k) {
    std::string cleaned; // std::string cleaned;
    for (char c : s) {   // for (char 字符 : 字符串) {
        if (c != '-')
            cleaned.push_back(static_cast<char>(std::toupper(static_cast<unsigned char>(c))));
    }
    int n = static_cast<int>(cleaned.size()); // 把 static_cast 小于 int 超过 (cleaned.大小()) 存入 元素个数
    if (n == 0)
        return "";     // 若 元素个数 等于 0，直接返回 「」
    std::string out;   // std::string out;
    int first = n % k; // 把 元素个数 对…取模 下标 k 存入 first
    int idx = 0;       // 把 0 存入 idx
    if (first > 0) {   // 若 first 超过 0
        for (int i = 0; i < first; ++i)
            out.push_back(cleaned[idx++]); // 让 下标 i 从 0 开始计数，下标 i 小于 first 就继续
        if (idx < n)
            out.push_back('-'); // 若 idx 小于 元素个数) out 追加 ' 减 ');
    }
    while (idx < n) { // 循环，直到不满足「idx 小于 元素个数」
        for (int i = 0; i < k; ++i)
            out.push_back(cleaned[idx++]); // 让 下标 i 从 0 开始计数，下标 i 小于 下标 k 就继续
        if (idx < n)
            out.push_back('-'); // 若 idx 小于 元素个数) out 追加 ' 减 ');
    }
    return out; // 返回 out
}
int main() {                                                       // 程序入口：跑内嵌自测用例
    assert(licenseKeyFormatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W"); // 断言校验
    assert(licenseKeyFormatting("2-5g-3-J", 2) == "2-5G-3J");      // 断言校验
    std::cout << "PASS" << std::endl;                              // 全部用例通过，输出 PASS
    return 0;                                                      // 返回 0
}
