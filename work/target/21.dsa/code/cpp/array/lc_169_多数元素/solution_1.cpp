// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133531071
// LeetCode 169. 多数元素 — C++ 版（方案1）
#include <cassert>                                         // 引入头文件
#include <iostream>                                        // 引入头文件
#include <unordered_map>                                   // 引入头文件
#include <vector>                                          // 引入头文件
static int majorityElement(const std::vector<int> &nums) { // 定义函数/方法 majorityElement
    std::unordered_map<int, int> counts; // std::unordered_map 小于 int, int 超过 counts;
    int best = nums[0], bn = 0;          // 把 数组[0], bn 赋值为 0 存入 当前最优
    for (int v : nums) {
        int c = ++counts[v];
        if (c > bn) {
            bn = c;
            best = v;
        }
    }
    return best; // 返回 当前最优
}
int main() {
    assert(majorityElement({3, 2, 3}) == 3);
    assert(majorityElement({2, 2, 1, 1, 1, 2, 2}) == 2);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS