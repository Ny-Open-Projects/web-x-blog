// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135756434
// LeetCode 696. 计数二进制子串 — C++ 版（方案8）
#include <algorithm>                                     // 引入头文件
#include <cassert>                                       // 引入头文件
#include <iostream>                                      // 引入头文件
#include <string>                                        // 引入头文件
#include <vector>                                        // 引入头文件
static int countBinarySubstrings(const std::string &s) { // 定义函数/方法 countBinarySubstrings
    std::vector<int> groups;                             // std::vector 小于 int 超过 groups;
    int n = static_cast<int>(s.size()); // 把 static_cast 小于 int 超过 (字符串.大小()) 存入 元素个数
    int i = 0;                          // 把 0 存入 下标 i
    while (i < n) {                     // 循环，直到不满足「下标 i 小于 元素个数」
        char ch = s[i];                 // 把 字符串[下标 i]; 写入 char ch
        int cnt = 0;                    // 把 0 存入 计数
        while (i < n && s[i] == ch) {
            ++cnt;
            ++i;
        }
        groups.push_back(cnt); // groups 追加 计数);
    }
    int ans = 0;                                 // 把 0 存入 答案
    for (size_t k = 1; k < groups.size(); ++k) { // 让 下标 k 从 1 开始计数，下标 k 小于 groups.大小() 就继续
        ans +=
            std::min(groups[k - 1], groups[k]); // 答案累加 std::取较小值 groups[下标 k 减 1], groups[下标 k])
    }
    return ans; // 返回 答案
}
int main() {                                        // 程序入口：跑内嵌自测用例
    assert(countBinarySubstrings("00110011") == 6); // 断言校验
    assert(countBinarySubstrings("10101") == 4);    // 断言校验
    std::cout << "PASS" << std::endl;               // 全部用例通过，输出 PASS
    return 0;                                       // 返回 0
}
