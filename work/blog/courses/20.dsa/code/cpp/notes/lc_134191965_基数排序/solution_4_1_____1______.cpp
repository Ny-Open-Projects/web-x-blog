// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134191965
// 数据结构与算法之排序: 基数排序 — C++ 版（方案4）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> radixSort(const std::vector<int> &nums) {
    if (nums.empty())
        return nums;                // 若 数组 是否为空，直接返回 数组
    int mn = nums[0], mx = nums[0]; // 把 数组[0], mx 赋值为 数组[0] 存入 mn
    for (int v : nums) {
        mn = std::min(mn, v);
        mx = std::max(mx, v);
    }
    int offset = mn < 0 ? -mn : 0; // 把 mn 小于 0 ? 减 mn : 0 存入 offset
    std::vector<long long> adj;    // std::vector 小于 long long 超过 邻接表;
    long long maxAdj = 0;          // 把 0 存入 maxAdj
    for (int v : nums) {
        adj.push_back(v + offset);
        maxAdj = std::max(maxAdj, static_cast<long long>(v) + offset);
    }
    long long radix = 1;                     // 把 1 存入 radix
    std::vector<long long> tmp(nums.size()); // std::vector 小于 long long 超过 临时变量(数组.大小());
    while (maxAdj >= radix) {                // 循环，直到不满足「maxAdj 不低于 radix」
        long long bucket[10] = {0};          // 把 {0}; 写入 long long bucket[10]
        for (auto x : adj)
            bucket[(x / radix) % 10]++; // 逐个取出 邻接表 的元素（x）
        for (int i = 1; i < 10; ++i)
            bucket[i] += bucket[i - 1]; // 让 下标 i 从 1 开始计数，下标 i 小于 10 就继续
        for (int i = static_cast<int>(adj.size()) - 1; i >= 0; --i) {
            tmp[--bucket[(adj[i] / radix) % 10]] =
                adj[i]; // 把 邻接表[下标 i]; 写入 tmp[--bucket[(adj[i] / radix) % 10]]
        }
        adj = tmp;   // 把 临时变量; 写入 邻接表
        radix *= 10; // 把 10; 写入 radix *
    }
    std::vector<int> out; // std::vector 小于 int 超过 out;
    for (auto x : adj)
        out.push_back(static_cast<int>(x - offset)); // 逐个取出 邻接表 的元素（x）
    return out;                                      // 返回 out
}
int main() { // 程序入口：跑内嵌自测用例
    assert((radixSort({5, 4, 3, 2, 1}) == std::vector<int>{1, 2, 3, 4, 5})); // 断言校验
    assert((radixSort({3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}) ==
            std::vector<int>{1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9})); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS