// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133524779
// LeetCode 167. 两数之和II — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> twoSum(const std::vector<int> &numbers, int target) {
    int l = 0, r = static_cast<int>(numbers.size()) -
                   1; // 把 0, 右指针 赋值为 static_cast 小于 int 超过 (numbers.大小()) 减 1 存入 左指针
    while (l < r) {                      // 循环，直到不满足「左指针 小于 右指针」
        int s = numbers[l] + numbers[r]; // 把 numbers[左指针] 加 numbers[右指针] 存入 字符串
        if (s == target)
            return {l + 1, r + 1}; // 若 字符串 等于 目标值，直接返回 {左指针 加 1, 右指针 加 1}
        if (s < target)
            ++l;
        else
            --r; // 若 字符串 小于 目标值) 加一 左指针; else 减一 右指针;
    }
    return {}; // 返回 {}
}
int main() {
    assert((twoSum({2, 7, 11, 15}, 9) == std::vector<int>{1, 2}));
    assert((twoSum({2, 3, 4}, 6) == std::vector<int>{1, 3}));
    assert((twoSum({-1, 0}, -1) == std::vector<int>{1, 2}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS