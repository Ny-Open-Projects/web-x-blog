// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// LeetCode 215. 数组中的第K个最大元素 — C++ 版（方案11）
#include <cassert>                                               // 引入头文件
#include <iostream>                                              // 引入头文件
#include <queue>                                                 // 引入头文件
#include <vector>                                                // 引入头文件
static int findKthLargest(const std::vector<int> &nums, int k) { // 定义函数/方法 findKthLargest
    std::priority_queue<int> heap(
        nums.begin(), nums.end()); // std::priority_queue 小于 int 超过 堆(数组 迭代位置 , 数组.终点());
    for (int i = 0; i < k - 1; ++i)
        heap.pop();    // 让 下标 i 从 0 开始计数，下标 i 小于 下标 k 减 1 就继续
    return heap.top(); // 返回 堆.top()
}
int main() {                                                     // 程序入口：跑内嵌自测用例
    assert(findKthLargest({3, 2, 1, 5, 6, 4}, 2) == 5);          // 断言校验
    assert(findKthLargest({3, 2, 3, 1, 2, 4, 5, 5, 6}, 4) == 4); // 断言校验
    assert(findKthLargest({1}, 1) == 1);                         // 断言校验
    std::cout << "PASS" << std::endl;                            // 全部用例通过，输出 PASS
    return 0;                                                    // 返回 0
}
