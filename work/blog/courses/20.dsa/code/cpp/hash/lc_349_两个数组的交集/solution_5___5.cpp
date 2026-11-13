// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135064368
// LeetCode 349. 两个数组的交集 — C++ 版（方案5）
#include <cassert>       // 引入头文件
#include <iostream>      // 引入头文件
#include <unordered_set> // 引入头文件
#include <vector>        // 引入头文件
static std::vector<int> intersection(const std::vector<int> &nums1, const std::vector<int> &nums2) {
    std::unordered_set<int> s1(
        nums1.begin(), nums1.end()); // std::unordered_set 小于 int 超过 s1(数组1 迭代位置 , 数组1.终点());
    std::unordered_set<int> seen; // std::unordered_set 小于 int 超过 已见集合;
    std::vector<int> res;         // std::vector 小于 int 超过 结果;
    for (int v : nums2) {         // for (int 值 : 数组2) {
        if (s1.count(v) && !seen.count(v)) {
            res.push_back(v);
            seen.insert(v);
        } // 若 s1.计数(值) 且 取反 已见集合.计数(值)) { 结果 追加 值); 已见集合 插入 值); }
    }
    return res; // 返回 结果
}
int main() { // 程序入口：跑内嵌自测用例
    assert((intersection({1, 2, 2, 1}, {2, 2}) == std::vector<int>{2}));          // 断言校验
    assert((intersection({4, 9, 5}, {9, 4, 9, 8, 4}) == std::vector<int>{9, 4})); // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
