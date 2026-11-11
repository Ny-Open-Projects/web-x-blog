// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134178290
// LeetCode 77. 组合 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<std::vector<int>> combine(int n, int k) {
    std::vector<std::vector<int>> res; // std::vector 小于 std::vector 小于 int 超过 超过 结果;
    std::vector<int> path;             // std::vector 小于 int 超过 当前路径;
    std::function<void(int)> dfs =
        [&](int start) { // 把 [ 按位与 ](int 起点) { 写入 std::function<void(int)> dfs
            if (static_cast<int>(path.size()) == k) {
                res.push_back(path);
                return;
            }
            for (int i = start; i <= n - (k - static_cast<int>(path.size())) + 1; ++i) {
                path.push_back(i); // 当前路径 追加 下标 i);
                dfs(i + 1);        // dfs(下标 i 加 1);
                path.pop_back();   // 弹出栈顶元素
            }
        };
    dfs(1);     // dfs(1);
    return res; // 返回 结果
}
int main() { // 程序入口：跑内嵌自测用例
    assert((combine(4, 2) ==
            std::vector<std::vector<int>>{{1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4}})); // 断言校验
    assert((combine(1, 1) == std::vector<std::vector<int>>{{1}}));                           // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
