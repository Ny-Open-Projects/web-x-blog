// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134109616
// LeetCode 78. 子集 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<std::vector<int>> subsets(const std::vector<int> &nums) {
    std::vector<std::vector<int>> res; // std::vector 小于 std::vector 小于 int 超过 超过 结果;
    std::vector<int> path;             // std::vector 小于 int 超过 当前路径;
    std::function<void(size_t)> dfs =
        [&](size_t start) {      // 把 [ 按位与 ](size_t 起点) { 写入 std::function<void(size_t)> dfs
            res.push_back(path); // 结果 追加 当前路径);
            for (size_t i = start; i < nums.size();
                 ++i) { // 让 下标 i 从 起点 开始计数，下标 i 小于 数组.大小() 就继续
                path.push_back(nums[i]); // 当前路径 追加 数组[下标 i]);
                dfs(i + 1);              // dfs(下标 i 加 1);
                path.pop_back();         // 弹出栈顶元素
            }
        };
    dfs(0);     // dfs(0);
    return res; // 返回 结果
}
int main() {                          // 程序入口：跑内嵌自测用例
    auto got = subsets({1, 2, 3});    // 把 subsets({1, 2, 3}) 存入 got
    assert(got.size() == 8);          // 断言校验
    assert(subsets({0}).size() == 2); // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
