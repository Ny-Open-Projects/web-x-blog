// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134134491
// LeetCode 47. 全排列II — C++ 版（方案2）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件
static std::vector<std::vector<int>> permuteUnique(std::vector<int> nums) {
    std::sort(nums.begin(), nums.end()); // std::sort(数组 迭代位置 , 数组.终点());
    std::vector<std::vector<int>> res;   // std::vector 小于 std::vector 小于 int 超过 超过 结果;
    std::vector<int> path;               // std::vector 小于 int 超过 当前路径;
    std::vector<bool> used(nums.size(), false); // std::vector 小于 bool 超过 已用标记(数组.大小(), false);
    std::function<void()> dfs = [&]() { // 把 [ 按位与 ]() { 写入 std::function<void()> dfs
        if (path.size() == nums.size()) {
            res.push_back(path);
            return;
        } // 若 当前路径.大小() 等于 数组.大小()) { 结果 追加 当前路径); return; }
        for (size_t i = 0; i < nums.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
            if (used[i])
                continue; // 若 已用标记[下标 i]) continue;
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1])
                continue;
            used[i] = true;          // 把 true; 写入 used[i]
            path.push_back(nums[i]); // 当前路径 追加 数组[下标 i]);
            dfs();                   // dfs();
            path.pop_back();         // 弹出栈顶元素
            used[i] = false;         // 把 false; 写入 used[i]
        }
    };
    dfs();      // dfs();
    return res; // 返回 结果
}
int main() { // 程序入口：跑内嵌自测用例
    assert((permuteUnique({1, 1, 2}) ==
            std::vector<std::vector<int>>{{1, 1, 2}, {1, 2, 1}, {2, 1, 1}})); // 断言校验
    assert(permuteUnique({1, 2, 3}).size() == 6);                             // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
