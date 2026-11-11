/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130704336 */
/* LeetCode 63. 不同路径II — C 版（方案1） */
#include <stdio.h> // 引入头文件
static int unique_paths_with_obstacles(int grid[][3], int m,
                                       int n) { // 定义函数/方法 unique_paths_with_obstacles
    int dp[3] = {0};                            // 把 {0}; 写入 int dp[3]
    dp[0] = grid[0][0] == 1 ? 0 : 1;            // 把 网格[0][0] 等于 1 ? 0 : 1; 写入 dp[0]
    for (int i = 0; i < m; i++)       // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
        for (int j = 0; j < n; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
            if (grid[i][j] == 1)
                dp[j] = 0; // 若 网格[下标 i][下标 j] 等于 1) DP 表[下标 j] 赋值为 0;
            else if (j > 0)
                dp[j] += dp[j - 1]; // 否则，若 下标 j 超过 0) DP 表[下标 j] 累加 DP 表[下标 j 减 1];
        }
    return dp[n - 1]; // 返回 DP 表[元素个数 减 1]
}
int main(void) {                                      // 程序入口：跑内嵌自测用例
    int g1[3][3] = {{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}; // 把 {{0,0,0},{0,1,0},{0,0,0}}; 写入 int g1[3][3]
    if (unique_paths_with_obstacles(g1, 3, 3) != 2) {
        printf("FAIL 1\n");
        return 1;
    }
    int g2[2][3] = {{0, 1, 0}, {0, 0, 0}}; // 把 {{0,1,0},{0,0,0}}; 写入 int g2[2][3]
    if (unique_paths_with_obstacles(g2, 2, 3) != 1) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS