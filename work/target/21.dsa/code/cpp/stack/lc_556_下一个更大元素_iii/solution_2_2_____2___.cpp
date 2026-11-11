// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397820
// LeetCode 556. 下一个更大元素 III — C++ 版（方案2）
#include <algorithm>                   // 引入头文件
#include <cassert>                     // 引入头文件
#include <iostream>                    // 引入头文件
#include <vector>                      // 引入头文件
static int nextGreaterElement(int n) { // 定义函数/方法 nextGreaterElement
    std::vector<int> d;                // std::vector 小于 int 超过 d;
    long long x = n;                   // 把 元素个数 存入 x
    while (x > 0) {
        d.push_back(static_cast<int>(x % 10));
        x /= 10;
    }
    std::reverse(d.begin(), d.end());   // std::reverse(d 迭代位置 , d.终点());
    int m = static_cast<int>(d.size()); // 把 static_cast 小于 int 超过 (d.大小()) 存入 映射表
    int i = m - 2;                      // 把 映射表 减 2 存入 下标 i
    while (i >= 0 && d[i] >= d[i + 1])
        --i; // 循环，直到不满足「下标 i 不低于 0 且 d[下标 i] 不低于 d[下标 i 加 1]) 减一 下标 i;」
    if (i < 0)
        return -1; // 若 下标 i 小于 0，直接返回 减 1
    int j = m - 1; // 把 映射表 减 1 存入 下标 j
    while (d[j] <= d[i])
        --j; // 循环，直到不满足「d[下标 j] 不超过 d[下标 i]) 减一 下标 j;」
    std::swap(d[i], d[j]);                    // 交换 d[下标 i] 与 d[下标 j]
    std::reverse(d.begin() + i + 1, d.end()); // std::reverse(d 迭代位置 加 下标 i 加 1, d.终点());
    long long res = 0;                        // 把 0 存入 结果
    for (int v : d)
        res = res * 10 + v; // 把 结果 乘 10 加 值; 写入 for (int v : d) res
    return res > 2147483647LL
               ? -1
               : static_cast<int>(
                     res); // 返回 结果 超过 2147483647LL ? 减 1 : static_cast 小于 int 超过 (结果)
}
int main() {
    assert(nextGreaterElement(12) == 21);
    assert(nextGreaterElement(21) == -1);
    assert(nextGreaterElement(1) == -1);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS