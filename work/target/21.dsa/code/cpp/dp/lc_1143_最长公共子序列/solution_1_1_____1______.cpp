// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
// LeetCode 1143. 最长公共子序列 — C++ 版（方案1）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <string>    // 引入头文件
#include <vector>    // 引入头文件
static int longestCommonSubsequence(const std::string &t1,
                                    const std::string &t2) { // 定义函数/方法 longestCommonSubsequence
    int m = static_cast<int>(t1.size()), n = static_cast<int>(t2.size());
    std::vector<int> dp(n + 1, 0); // std::vector 小于 int 超过 DP 表(元素个数 加 1, 0);
    for (int i = 1; i <= m; ++i) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
        int prevDiag = 0;          // 把 0 存入 prevDiag
        for (int j = 1; j <= n; ++j) { // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
            int tmp = dp[j];           // 把 DP 表[下标 j] 存入 临时变量
            dp[j] = (t1[i - 1] == t2[j - 1]) ? prevDiag + 1 : std::max(dp[j], dp[j - 1]);
            prevDiag = tmp; // 把 临时变量; 写入 prevDiag
        }
    }
    return dp[n]; // 返回 DP 表[元素个数]
}
int main() {
    assert(longestCommonSubsequence("abcde", "ace") == 3);
    assert(longestCommonSubsequence("abc", "abc") == 3);
    assert(longestCommonSubsequence("abc", "def") == 0);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS