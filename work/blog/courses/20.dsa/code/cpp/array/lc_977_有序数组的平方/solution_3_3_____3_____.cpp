// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134982348
// LeetCode 977. 有序数组的平方 — C++ 版（方案3）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> sortedSquares(const std::vector<int> &nums) {
    int n = static_cast<int>(nums.size()); // 把 static_cast 小于 int 超过 (数组.大小()) 存入 元素个数
    std::vector<int> out(n);               // std::vector 小于 int 超过 out(元素个数);
    int l = 0, r = n - 1,
        idx = n - 1; // 把 0, 右指针 赋值为 元素个数 减 1, idx 赋值为 元素个数 减 1 存入 左指针
    while (l <= r) { // 循环，直到不满足「左指针 不超过 右指针」
        long long a = std::abs(nums[l]), b = std::abs(nums[r]); // 把 std::取绝对值 数组[左指针]), b 赋值为
                                                                // std::取绝对值 数组[右指针]) 存入 数组
        if (a > b) {
            out[idx--] = static_cast<int>(a * a);
            ++l;
        } else {
            out[idx--] = static_cast<int>(b * b);
            --r;
        } // 否则
    }
    return out; // 返回 out
}
int main() {
    assert((sortedSquares({-4, -1, 0, 3, 10}) == std::vector<int>{0, 1, 9, 16, 100}));
    assert((sortedSquares({-7, -3, 2, 3, 11}) == std::vector<int>{4, 9, 9, 49, 121}));
    assert((sortedSquares({1, 2, 3}) == std::vector<int>{1, 4, 9}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS