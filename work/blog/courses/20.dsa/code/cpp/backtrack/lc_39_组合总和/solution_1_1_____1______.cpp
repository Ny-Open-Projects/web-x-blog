// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133865307
// LeetCode 39. 组合总和 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<std::vector<int>> combinationSum(const std::vector<int> &candidates, int target) {
    std::vector<std::vector<int>> res; // std::vector 小于 std::vector 小于 int 超过 超过 结果;
    std::vector<int> path;             // std::vector 小于 int 超过 当前路径;
    std::function<void(size_t, int)> dfs = [&](size_t start, int remaining) {
        if (remaining == 0) {
            res.push_back(path);
            return;
        } // 若 remaining 等于 0) { 结果 追加 当前路径); return; }
        if (remaining < 0)
            return; // 若 remaining 小于 0) return;
        for (size_t i = start; i < candidates.size();
             ++i) { // 让 下标 i 从 起点 开始计数，下标 i 小于 候选数组.大小() 就继续
            path.push_back(candidates[i]);     // 当前路径 追加 候选数组[下标 i]);
            dfs(i, remaining - candidates[i]); // dfs(下标 i, remaining 减 候选数组[下标 i]);
            path.pop_back();                   // 弹出栈顶元素
        }
    };
    dfs(0, target); // dfs(0, 目标值);
    return res;     // 返回 结果
}
int main() { // 程序入口：跑内嵌自测用例
    assert((combinationSum({2, 3, 6, 7}, 7) == std::vector<std::vector<int>>{{2, 2, 3}, {7}})); // 断言校验
    assert((combinationSum({2, 3, 5}, 8) ==
            std::vector<std::vector<int>>{{2, 2, 2, 2}, {2, 3, 3}, {3, 5}})); // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
