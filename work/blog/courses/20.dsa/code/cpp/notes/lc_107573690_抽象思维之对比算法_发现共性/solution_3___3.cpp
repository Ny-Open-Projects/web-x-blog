// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107573690
// 抽象思维之对比算法 发现共性 — C++ 版（方案3）
#include <cassert>                              // 引入头文件
#include <iostream>                             // 引入头文件
#include <vector>                               // 引入头文件
static long long climbStairsRefactored(int n) { // static long long climbStairsRefactored(int 元素个数) {
    if (n == 0)
        return 1; // 若 元素个数 等于 0，直接返回 1
    if (n < 0)
        return 0;                        // 若 元素个数 小于 0，直接返回 0
    std::vector<long long> dp(n + 1, 0); // std::vector 小于 long long 超过 DP 表(元素个数 加 1, 0);
    dp[0] = 1;                           // 把 1; 写入 dp[0]
    for (int i = 1; i <= n; ++i) { // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
        dp[i] = dp[i - 1];         // 把 DP 表[下标 i 减 1]; 写入 dp[i]
        if (i >= 2)
            dp[i] += dp[i - 2]; // 若 下标 i 不低于 2) DP 表[下标 i] 累加 DP 表[下标 i 减 2];
        if (i >= 3)
            dp[i] += dp[i - 3]; // 若 下标 i 不低于 3) DP 表[下标 i] 累加 DP 表[下标 i 减 3];
    }
    return dp[n]; // 返回 DP 表[元素个数]
}
int main() {
    assert(climbStairsRefactored(10) == 274);
    assert(climbStairsRefactored(3) == 4);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS