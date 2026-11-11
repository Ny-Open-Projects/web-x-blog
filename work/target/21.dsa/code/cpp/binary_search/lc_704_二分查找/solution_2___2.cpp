// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134221939
// LeetCode 704. 二分查找 — C++ 版

#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

int search(const std::vector<int> &nums, int target) { // 定义函数/方法 search
    int left = 0, right = static_cast<int>(nums.size()) -
                          1; // 把 0, 右边界 赋值为 static_cast 小于 int 超过 (数组.大小()) 减 1 存入 左边界
    while (left <= right) {                  // 循环，直到不满足「左边界 不超过 右边界」
        int mid = left + (right - left) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2 存入 中点
        if (nums[mid] == target) {           // 若 数组[中点] 等于 目标值
            return mid;                      // 返回 中点
        } else if (nums[mid] < target) {     // 否则，若 数组[中点] 小于 目标值
            left = mid + 1;                  // 把 中点 加 1; 写入 左边界
        } else {                             // 否则
            right = mid - 1;                 // 把 中点 减 1; 写入 右边界
        }
    }
    return -1; // 返回 减 1
}

int main() {                                       // 程序入口：跑内嵌自测用例
    assert(search({1, 2, 3}, 1) == 0);             // 断言校验
    assert(search({-1, 0, 3, 5, 9, 12}, 9) == 4);  // 断言校验
    assert(search({-1, 0, 3, 5, 9, 12}, 2) == -1); // 断言校验
    std::cout << "PASS" << std::endl;              // 全部用例通过，输出 PASS
    return 0;                                      // 返回 0
}
