// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130613988
// LeetCode 583. 两个字符串的删除操作 — C++ 版（方案1）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <string>    // 引入头文件
#include <vector>    // 引入头文件
static int minDeleteDistance(const std::string &w1,
                             const std::string &w2) { // 定义函数/方法 minDeleteDistance
    int m = static_cast<int>(w1.size()), n = static_cast<int>(w2.size());
    std::vector<int> dp(n + 1); // std::vector 小于 int 超过 DP 表(元素个数 加 1);
    for (int j = 0; j <= n; ++j)
        dp[j] = j; // 让 下标 j 从 0 开始计数，下标 j 不超过 元素个数 就继续
    for (int i = 1; i <= m; ++i) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
        int prevDiag = dp[0];      // 把 DP 表[0] 存入 prevDiag
        dp[0] = i;                 // 把 下标 i; 写入 dp[0]
        for (int j = 1; j <= n; ++j) { // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
            int tmp = dp[j];           // 把 DP 表[下标 j] 存入 临时变量
            dp[j] = (w1[i - 1] == w2[j - 1]) ? prevDiag : 1 + std::min({prevDiag, dp[j], dp[j - 1]});
            prevDiag = tmp; // 把 临时变量; 写入 prevDiag
        }
    }
    return dp[n]; // 返回 DP 表[元素个数]
}
int main() {
    assert(minDeleteDistance("sea", "eat") == 2);
    assert(minDeleteDistance("leetcode", "etco") == 4);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS