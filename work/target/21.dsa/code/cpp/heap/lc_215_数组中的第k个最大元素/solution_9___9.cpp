// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// LeetCode 215. 数组中的第K个最大元素 — C++ 版（方案9）
#include <algorithm>                                      // 引入头文件
#include <cassert>                                        // 引入头文件
#include <iostream>                                       // 引入头文件
#include <vector>                                         // 引入头文件
static int findKthLargest(std::vector<int> nums, int k) { // 定义函数/方法 findKthLargest
    std::sort(nums.begin(), nums.end(),
              std::greater<int>()); // std::sort(数组 迭代位置 , 数组.终点(), std::greater 小于 int 超过 ());
    return nums[k - 1]; // 返回 数组[下标 k 减 1]
}
int main() {                                                     // 程序入口：跑内嵌自测用例
    assert(findKthLargest({3, 2, 1, 5, 6, 4}, 2) == 5);          // 断言校验
    assert(findKthLargest({3, 2, 3, 1, 2, 4, 5, 5, 6}, 4) == 4); // 断言校验
    assert(findKthLargest({1}, 1) == 1);                         // 断言校验
    std::cout << "PASS" << std::endl;                            // 全部用例通过，输出 PASS
    return 0;                                                    // 返回 0
}
