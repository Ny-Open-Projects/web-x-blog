// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// LeetCode 215. 数组中的第K个最大元素 — C++ 版（方案10）
#include <cassert>                                               // 引入头文件
#include <iostream>                                              // 引入头文件
#include <vector>                                                // 引入头文件
static int findKthLargest(const std::vector<int> &nums, int k) { // 定义函数/方法 findKthLargest
    std::vector<int> a = nums;                                   // 把 数组; 写入 std::vector<int> a
    int n = static_cast<int>(a.size()); // 把 static_cast 小于 int 超过 (数组.大小()) 存入 元素个数
    for (int i = n - 1; i > n - 1 - k;
         --i) { // 让 下标 i 从 元素个数 减 1 开始计数，下标 i 超过 元素个数 减 1 减 下标 k 就继续
        for (int j = 0; j < i; ++j) { // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
            if (a[j] > a[j + 1])
                std::swap(a[j], a[j + 1]); // 若 数组[下标 j] 超过 数组[下标 j 加 1]) std::交换 数组[下标 j],
                                           // 数组[下标 j 加 1]);
        }
    }
    return a[n - k]; // 返回 数组[元素个数 减 下标 k]
}
int main() {                                                     // 程序入口：跑内嵌自测用例
    assert(findKthLargest({3, 2, 1, 5, 6, 4}, 2) == 5);          // 断言校验
    assert(findKthLargest({3, 2, 3, 1, 2, 4, 5, 5, 6}, 4) == 4); // 断言校验
    assert(findKthLargest({1}, 1) == 1);                         // 断言校验
    std::cout << "PASS" << std::endl;                            // 全部用例通过，输出 PASS
    return 0;                                                    // 返回 0
}
