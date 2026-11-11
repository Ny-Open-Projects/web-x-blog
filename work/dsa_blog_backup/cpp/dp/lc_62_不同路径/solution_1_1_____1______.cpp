// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130641517
// LeetCode 62. 不同路径 — C++ 版（方案1）
#include <cassert>                     // 引入头文件
#include <iostream>                    // 引入头文件
#include <vector>                      // 引入头文件
static int uniquePaths(int m, int n) { // 定义函数/方法 uniquePaths
    std::vector<int> dp(n, 1);         // std::vector 小于 int 超过 DP 表(元素个数, 1);
    for (int i = 1; i < m; ++i) // 让 下标 i 从 1 开始计数，下标 i 小于 映射表 就继续
        for (int j = 1; j < n; ++j)
            dp[j] += dp[j - 1]; // 让 下标 j 从 1 开始计数，下标 j 小于 元素个数 就继续
    return dp[n - 1];           // 返回 DP 表[元素个数 减 1]
}
int main() {
    assert(uniquePaths(3, 7) == 28);
    assert(uniquePaths(3, 2) == 3);
    assert(uniquePaths(1, 1) == 1);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS