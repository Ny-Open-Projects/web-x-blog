// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130590161
// LeetCode 115. 不同的子序列 — C++ 版（方案4）
#include <cassert>                                                   // 引入头文件
#include <iostream>                                                  // 引入头文件
#include <string>                                                    // 引入头文件
#include <vector>                                                    // 引入头文件
static int numDistinct(const std::string &s, const std::string &t) { // 定义函数/方法 numDistinct
    int m = static_cast<int>(s.size()), n = static_cast<int>(t.size());
    std::vector<long long> dp(n + 1, 0); // std::vector 小于 long long 超过 DP 表(元素个数 加 1, 0);
    dp[0] = 1;                           // 把 1; 写入 dp[0]
    for (int i = 1; i <= m; ++i) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
        for (int j = n; j >= 1; --j) { // 让 下标 j 从 元素个数 开始计数，下标 j 不低于 1 就继续
            if (s[i - 1] == t[j - 1])
                dp[j] += dp[j - 1];
        }
    }
    return static_cast<int>(dp[n]); // 返回 static_cast 小于 int 超过 (DP 表[元素个数])
}
int main() {
    assert(numDistinct("rabbbit", "rabbit") == 3);
    assert(numDistinct("babgbag", "bag") == 5);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS