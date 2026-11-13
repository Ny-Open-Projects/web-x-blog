// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135917076
// LeetCode 567. 字符串的排列 — C++ 版（方案2）
#include <cassert>                                                         // 引入头文件
#include <iostream>                                                        // 引入头文件
#include <string>                                                          // 引入头文件
#include <vector>                                                          // 引入头文件
static bool checkInclusion(const std::string &s1, const std::string &s2) { // 定义判定函数 checkInclusion
    int m = static_cast<int>(s1.size()), n = static_cast<int>(s2.size());
    if (m > n)
        return false;                        // 若 映射表 超过 元素个数，直接返回 false
    std::vector<int> s1c(26, 0), s2c(26, 0); // std::vector 小于 int 超过 s1c(26, 0), s2c(26, 0);
    for (int i = 0; i < m; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
        ++s1c[s1[i] - 'a'];       // 加一 s1c[s1[下标 i] 减 '数组'];
        ++s2c[s2[i] - 'a'];       // 加一 s2c[s2[下标 i] 减 '数组'];
    }
    if (s1c == s2c)
        return true;              // 若 s1c 等于 s2c，直接返回 true
    for (int i = m; i < n; ++i) { // 让 下标 i 从 映射表 开始计数，下标 i 小于 元素个数 就继续
        ++s2c[s2[i] - 'a'];     // 加一 s2c[s2[下标 i] 减 '数组'];
        --s2c[s2[i - m] - 'a']; // 减一 s2c[s2[下标 i 减 映射表] 减 '数组'];
        if (s1c == s2c)
            return true; // 若 s1c 等于 s2c，直接返回 true
    }
    return false; // 返回 false
}
int main() {                                   // 程序入口：跑内嵌自测用例
    assert(checkInclusion("ab", "eidbaooo"));  // 断言校验
    assert(!checkInclusion("ab", "eidboaoo")); // 断言校验
    std::cout << "PASS" << std::endl;          // 全部用例通过，输出 PASS
    return 0;                                  // 返回 0
}
