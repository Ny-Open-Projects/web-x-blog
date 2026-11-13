// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130704336
// LeetCode 63. 不同路径II — C++ 版（方案4）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static int uniquePathsWithObstacles(
    const std::vector<std::vector<int>> &grid) { // 定义函数/方法 uniquePathsWithObstacles
    size_t m = grid.size(),
           n = grid[0].size(); // 把 网格.大小(), 元素个数 赋值为 网格[0].大小(); 写入 size_t m
    std::vector<int> dp(n, 0);       // std::vector 小于 int 超过 DP 表(元素个数, 0);
    dp[0] = grid[0][0] == 1 ? 0 : 1; // 把 网格[0][0] 等于 1 ? 0 : 1; 写入 dp[0]
    for (size_t i = 0; i < m; ++i)   // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
        for (size_t j = 0; j < n; ++j) { // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
            if (grid[i][j] == 1)
                dp[j] = 0; // 若 网格[下标 i][下标 j] 等于 1) DP 表[下标 j] 赋值为 0;
            else if (j > 0)
                dp[j] += dp[j - 1]; // 否则，若 下标 j 超过 0) DP 表[下标 j] 累加 DP 表[下标 j 减 1];
        }
    return dp[n - 1]; // 返回 DP 表[元素个数 减 1]
}
int main() { // 程序入口：跑内嵌自测用例
    assert(uniquePathsWithObstacles({{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}) == 2); // 断言校验
    assert(uniquePathsWithObstacles({{0, 1}, {0, 0}}) == 1);                  // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS