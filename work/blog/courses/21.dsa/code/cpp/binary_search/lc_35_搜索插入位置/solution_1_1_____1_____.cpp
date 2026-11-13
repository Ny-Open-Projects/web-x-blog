// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233077
// LeetCode 35. 搜索插入位置 — C++ 版（方案1：二分查找）
#include <cassert>                                           // 引入头文件
#include <iostream>                                          // 引入头文件
#include <vector>                                            // 引入头文件
int searchInsert(const std::vector<int> &nums, int target) { // 定义函数/方法 searchInsert
    int left = 0, right = static_cast<int>(
                      nums.size()); // 把 0, 右边界 赋值为 static_cast 小于 int 超过 (数组.大小()) 存入 左边界
    while (left < right) {                   // 循环，直到不满足「左边界 小于 右边界」
        int mid = left + (right - left) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2 存入 中点
        if (nums[mid] < target)
            left = mid + 1;
        else
            right = mid; // 若 数组[中点] 小于 目标值) 左边界 赋值为 中点 加 1; else 右边界 赋值为 中点;
    }
    return left; // 返回 左边界
}
int main() {                                    // 程序入口：跑内嵌自测用例
    assert(searchInsert({1, 2, 3}, 1) == 0);    // 断言校验
    assert(searchInsert({1, 3, 5, 6}, 5) == 2); // 断言校验
    assert(searchInsert({1, 3, 5, 6}, 2) == 1); // 断言校验
    assert(searchInsert({1, 3, 5, 6}, 7) == 4); // 断言校验
    assert(searchInsert({1, 3, 5, 6}, 0) == 0); // 断言校验
    std::cout << "PASS" << std::endl;           // 全部用例通过，输出 PASS
}
