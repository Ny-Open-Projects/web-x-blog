// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145568435
// LeetCode 350. 两个数组的交集 II — C++ 版（方案2）
#include <cassert>       // 引入头文件
#include <iostream>      // 引入头文件
#include <unordered_map> // 引入头文件
#include <vector>        // 引入头文件
static std::vector<int> intersect(const std::vector<int> &nums1, const std::vector<int> &nums2) {
    const auto &a = nums1.size() <= nums2.size()
                        ? nums1
                        : nums2; // 把 数组1.大小() 不超过 数组2.大小() ? 数组1 : 数组2; 写入 const auto &a
    const auto &b = nums1.size() <= nums2.size()
                        ? nums2
                        : nums1; // 把 数组1.大小() 不超过 数组2.大小() ? 数组2 : 数组1; 写入 const auto &b
    std::unordered_map<int, int> mp; // std::unordered_map 小于 int, int 超过 mp;
    for (int v : a)
        ++mp[v];          // for (int 值 : 数组) 加一 mp[值];
    std::vector<int> res; // std::vector 小于 int 超过 结果;
    for (int v : b) {     // for (int 值 : b) {
        if (mp[v] > 0) {
            res.push_back(v);
            --mp[v];
        } // 若 mp[值] 超过 0) { 结果 追加 值); 减一 mp[值]; }
    }
    return res; // 返回 结果
}
int main() { // 程序入口：跑内嵌自测用例
    assert((intersect({1, 2, 2, 1}, {2, 2}) == std::vector<int>{2, 2}));       // 断言校验
    assert((intersect({4, 9, 5}, {9, 4, 9, 8, 4}) == std::vector<int>{9, 4})); // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
