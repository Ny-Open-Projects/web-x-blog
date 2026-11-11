// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// LeetCode 215. 数组中的第K个最大元素 — C++ 版（方案8）
#include <cassert>                                                  // 引入头文件
#include <iostream>                                                 // 引入头文件
#include <vector>                                                   // 引入头文件
static void quickselect(std::vector<int> &a, int l, int r, int k) { // 定义函数/方法 quickselect
    if (l >= r)
        return;                     // 若 左指针 不低于 右指针) return;
    int i = l, j = r;               // 把 左指针, 下标 j 赋值为 右指针 存入 下标 i
    int pivot = a[l + (r - l) / 2]; // 把 数组[(左指针 加 右指针) 除以 2] 存入 pivot
    while (i <= j) {                // 循环，直到不满足「下标 i 不超过 下标 j」
        while (a[i] > pivot)
            ++i; // 循环，直到不满足「数组[下标 i] 超过 pivot) 加一 下标 i;」
        while (a[j] < pivot)
            --j; // 循环，直到不满足「数组[下标 j] 小于 pivot) 减一 下标 j;」
        if (i <= j) {
            std::swap(a[i], a[j]);
            ++i;
            --j;
        }
    }
    if (k <= j + 1) {
        if (l < j)
            quickselect(a, l, j, k);
        return;
    }
    if (k >= i + 1 && i < r)
        quickselect(a, i, r, k);
}
static int findKthLargest(std::vector<int> nums, int k) { // 定义函数/方法 findKthLargest
    quickselect(nums, 0, static_cast<int>(nums.size()) - 1, k);
    return nums[k - 1]; // 返回 数组[下标 k 减 1]
}
int main() {                                                     // 程序入口：跑内嵌自测用例
    assert(findKthLargest({3, 2, 1, 5, 6, 4}, 2) == 5);          // 断言校验
    assert(findKthLargest({3, 2, 3, 1, 2, 4, 5, 5, 6}, 4) == 4); // 断言校验
    assert(findKthLargest({1}, 1) == 1);                         // 断言校验
    std::cout << "PASS" << std::endl;                            // 全部用例通过，输出 PASS
    return 0;                                                    // 返回 0
}
