// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295
// 数据结构与算法之排序: 归并排序 — C++ 版（方案5）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> mergeSort(const std::vector<int> &nums) {
    if (nums.size() <= 1)
        return nums;              // 若 数组.大小() 不超过 1，直接返回 数组
    size_t mid = nums.size() / 2; // 把 数组.大小() 除以 2; 写入 size_t mid
    auto left = mergeSort(std::vector<int>(nums.begin(), nums.begin() + mid));
    auto right = mergeSort(std::vector<int>(nums.begin() + mid, nums.end()));
    std::vector<int> out; // std::vector 小于 int 超过 out;
    size_t i = 0, j = 0;  // 把 0, 下标 j 赋值为 0; 写入 size_t i
    while (i < left.size() &&
           j < right.size()) { // 循环，直到不满足「下标 i 小于 左边界.大小() 且 下标 j 小于 右边界.大小(」
        if (left[i] <= right[j])
            out.push_back(
                left[i++]); // 若 左边界[下标 i] 不超过 右边界[下标 j]) out 追加 左边界[下标 i 加一 ]);
        else
            out.push_back(right[j++]); // 否则
    }
    while (i < left.size())
        out.push_back(
            left[i++]); // 循环，直到不满足「下标 i 小于 左边界.大小()) out 追加 左边界[下标 i 加一 ]);」
    while (j < right.size())
        out.push_back(
            right[j++]); // 循环，直到不满足「下标 j 小于 右边界.大小()) out 追加 右边界[下标 j 加一 ]);」
    return out; // 返回 out
}
int main() { // 程序入口：跑内嵌自测用例
    assert((mergeSort({5, 4, 3, 2, 1}) == std::vector<int>{1, 2, 3, 4, 5})); // 断言校验
    assert((mergeSort({3, 1, 4, 1, 5}) == std::vector<int>{1, 1, 3, 4, 5})); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS