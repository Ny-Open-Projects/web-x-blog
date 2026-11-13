// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233483
// LeetCode 153. 寻找旋转排序数组中的最小值 — C++ 版（方案1：二分查找）

#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

int findMin(const std::vector<int> &nums) { // 定义函数/方法 findMin
    int low = 0, high = static_cast<int>(nums.size()) -
                        1; // 把 0, high 赋值为 static_cast 小于 int 超过 (数组.大小()) 减 1 存入 low
    while (low < high) {                    // 循环，直到不满足「low 小于 high」
        int pivot = low + (high - low) / 2; // 防溢出写法
        if (nums[pivot] < nums[high]) {     // 若 数组[pivot] 小于 数组[high]
            high = pivot;                   // 把 pivot; 写入 high
        } else {                            // 否则
            low = pivot + 1;                // 把 pivot 加 1; 写入 low
        }
    }
    return nums[low]; // 返回 数组[low]
}

int main() {                                     // 程序入口：跑内嵌自测用例
    assert(findMin({1, 2, 3}) == 1);             // 断言校验
    assert(findMin({3, 4, 5, 1, 2}) == 1);       // 断言校验
    assert(findMin({4, 5, 6, 7, 0, 1, 2}) == 0); // 断言校验
    assert(findMin({11, 13, 15, 17}) == 11);     // 断言校验
    std::cout << "PASS" << std::endl;            // 全部用例通过，输出 PASS
    return 0;                                    // 返回 0
}
