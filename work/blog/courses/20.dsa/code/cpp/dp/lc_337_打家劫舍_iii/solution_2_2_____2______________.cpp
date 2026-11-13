// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130671359
// LeetCode 337. 打家劫舍III — C++ 版（方案2）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件
static std::pair<long long, long long> dfs(const std::vector<int> &vals, size_t i) {
    if (i >= vals.size() || vals[i] == INT32_MIN)
        return {0, 0}; // 若 下标 i 不低于 vals.大小() 或 vals[下标 i] 等于 INT32_MIN，直接返回 {0, 0}
    auto l = dfs(vals, 2 * i + 1); // 把 dfs(vals, 2 乘 下标 i 加 1) 存入 左指针
    auto r = dfs(vals, 2 * i + 2); // 把 dfs(vals, 2 乘 下标 i 加 2) 存入 右指针
    long long include =
        vals[i] + l.second + r.second; // 把 vals[下标 i] 加 左指针.second 加 右指针.second 存入 include
    long long exclude = std::max(l.first, l.second) + std::max(r.first, r.second);
    return {include, exclude}; // 返回 {include, exclude}
}
static int robTree(const std::vector<int> &vals) { // 定义函数/方法 robTree
    auto r = dfs(vals, 0);                         // 把 dfs(vals, 0) 存入 右指针
    return static_cast<int>(std::max(
        r.first, r.second)); // 返回 static_cast 小于 int 超过 (std::取较大值 右指针.first, 右指针.second))
}
int main() {                                     // 程序入口：跑内嵌自测用例
    const int N = INT32_MIN;                     // 把 INT32_MIN; 写入 const int N
    assert(robTree({3, 2, 3, N, 3, N, 1}) == 7); // 断言校验
    assert(robTree({3, 4, 5, 1, 3, N, 1}) == 9); // 断言校验
    assert(robTree({}) == 0);                    // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS