// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135038527
// LeetCode 217. 存在重复元素 — C++ 版（方案2）
#include <cassert>                                            // 引入头文件
#include <iostream>                                           // 引入头文件
#include <unordered_set>                                      // 引入头文件
#include <vector>                                             // 引入头文件
static bool containsDuplicate(const std::vector<int> &nums) { // 定义函数/方法 containsDuplicate
    return std::unordered_set<int>(nums.begin(), nums.end()).size() != nums.size();
}
int main() {                                  // 程序入口：跑内嵌自测用例
    assert(containsDuplicate({1, 2, 3, 1}));  // 断言校验
    assert(!containsDuplicate({1, 2, 3, 4})); // 断言校验
    std::cout << "PASS" << std::endl;         // 全部用例通过，输出 PASS
    return 0;                                 // 返回 0
}
