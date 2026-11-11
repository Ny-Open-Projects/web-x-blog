// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689
// LeetCode 113951689. 动态规划之 LCS — C++ 版（最长公共子序列：DP 填表 + 回溯构造）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <string>    // 引入头文件
#include <vector>    // 引入头文件

static std::vector<std::vector<int>> lcs_table(const std::string &a, const std::string &b) {
    int m = static_cast<int>(a.size()), n = static_cast<int>(b.size());
    std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
    for (int i = 1; i <= m; ++i) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
        for (int j = 1; j <= n; ++j) { // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
            if (a[i - 1] == b[j - 1]) {          // 若 数组[下标 i 减 1] 等于 b[下标 j 减 1]
                dp[i][j] = dp[i - 1][j - 1] + 1; // 把 DP 表[下标 i 减 1][下标 j 减 1] 加 1; 写入 dp[i][j]
            } else {                             // 否则
                dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp; // 返回 DP 表
}

static int lcs_length(const std::string &a, const std::string &b) { // 定义函数/方法 lcs_length
    return lcs_table(a, b)[a.size()][b.size()]; // 返回 lcs_table(数组, b)[数组.大小()][b.大小()]
}

static std::string lcs_string(const std::string &a, const std::string &b) {
    auto dp = lcs_table(a, b); // 把 lcs_table(数组, b) 存入 DP 表
    int i = static_cast<int>(a.size()), j = static_cast<int>(b.size());
    std::string out;                 // std::string out;
    while (i > 0 && j > 0) {         // 循环，直到不满足「下标 i 超过 0 且 下标 j 超过 0」
        if (a[i - 1] == b[j - 1]) {  // 若 数组[下标 i 减 1] 等于 b[下标 j 减 1]
            out.push_back(a[i - 1]); // out 追加 数组[下标 i 减 1]);
            --i;
            --j; // 减一 下标 i; 减一 下标 j;
        } else if (dp[i - 1][j] >=
                   dp[i][j - 1]) { // 否则，若 DP 表[下标 i 减 1][下标 j] 不低于 DP 表[下标 i][下标 j 减 1]
            --i;                   // 减一 下标 i;
        } else {                   // 否则
            --j;                   // 减一 下标 j;
        }
    }
    std::reverse(out.begin(), out.end()); // std::reverse(out 迭代位置 , out.终点());
    return out;                           // 返回 out
}

static bool is_common_sub(const std::string &a, const std::string &b,
                          const std::string &s) { // 定义判定函数 is_common_sub
    size_t ia = 0, ib = 0;                        // 把 0, ib 赋值为 0; 写入 size_t ia
    for (char ch : s) {                           // for (char 字符 : 字符串) {
        while (ia < a.size() && a[ia] != ch)
            ++ia; // 循环，直到不满足「ia 小于 数组.大小() 且 数组[ia] 不等于 字符) 加一 ia;」
        while (ib < b.size() && b[ib] != ch)
            ++ib; // 循环，直到不满足「ib 小于 b.大小() 且 b[ib] 不等于 字符) 加一 ib;」
        if (ia >= a.size() || ib >= b.size())
            return false; // 若 ia 不低于 数组.大小() 或 ib 不低于 b.大小()，直接返回 false
        ++ia;
        ++ib; // 加一 ia; 加一 ib;
    }
    return true; // 返回 true
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::tuple<std::string, std::string, int>> cases = {
        {"ABCBDAB", "BDCABA", 4}, {"AGGTAB", "GXTXAYB", 4}, {"abc", "abc", 3},
        {"", "abc", 0},           {"abc", "xyz", 0},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) { // 让 idx 从 0 开始计数，idx 小于 cases.大小() 就继续
        int got = lcs_length(std::get<0>(cases[idx]), std::get<1>(cases[idx]));
        if (got != std::get<2>(cases[idx])) { // 若 got 不等于 std::get 小于 2 超过 (cases[idx]
            std::cout << "case " << idx << " failed: got " << got << " want " << std::get<2>(cases[idx])
                      << std::endl; // 打印输出
            return 1;               // 返回 1
        }
    }
    for (auto &p : {std::pair<std::string, std::string>{"ABCBDAB", "BDCABA"}, {"AGGTAB", "GXTXAYB"}}) {
        std::string s =
            lcs_string(p.first, p.second); // 把 lcs_string(节点.first, 节点.second); 写入 std::string s
        if (static_cast<int>(s.size()) != lcs_length(p.first, p.second) ||
            !is_common_sub(p.first, p.second, s)) { // 取反 is_common_sub(节点.first, 节点.second, 字符串)) {
            std::cout << "lcs_string failed: " << s << std::endl; // 打印输出
            return 1;                                             // 返回 1
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
