// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134773756
// LeetCode 75. 颜色分类 — C++ 版（方案1）
#include <cassert>                               // 引入头文件
#include <iostream>                              // 引入头文件
#include <vector>                                // 引入头文件
static void sortColors(std::vector<int> &nums) { // 定义函数/方法 sortColors
    int p0 = 0, cur = 0, p2 = static_cast<int>(nums.size()) - 1;
    while (cur <= p2) { // 循环，直到不满足「当前值 不超过 p2」
        if (nums[cur] == 0)
            std::swap(nums[p0++],
                      nums[cur++]); // 若 数组[当前值] 等于 0) std::交换 数组[p0 加一 ], 数组[当前值 加一 ]);
        else if (nums[cur] == 2)
            std::swap(nums[cur],
                      nums[p2--]); // 否则，若 数组[当前值] 等于 2) std::交换 数组[当前值], 数组[p2 减一 ]);
        else
            ++cur; // 否则
    }
}
int main() {                                           // 程序入口：跑内嵌自测用例
    std::vector<int> v = {2, 0, 2, 1, 1, 0};           // 把 {2, 0, 2, 1, 1, 0}; 写入 std::vector<int> v
    sortColors(v);                                     // sortColors(值);
    assert((v == std::vector<int>{0, 0, 1, 1, 2, 2})); // 断言校验
    std::vector<int> v2 = {2, 0, 1};                   // 把 {2, 0, 1}; 写入 std::vector<int> v2
    sortColors(v2);                                    // sortColors(v2);
    assert((v2 == std::vector<int>{0, 1, 2}));         // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS