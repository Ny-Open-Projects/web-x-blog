// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133907522
// LeetCode 238. 除自身以外数组的乘积 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> productExceptSelf(const std::vector<int> &nums) {
    size_t n = nums.size();           // 把 数组.大小(); 写入 size_t n
    std::vector<long long> out(n, 1); // std::vector 小于 long long 超过 out(元素个数, 1);
    long long left = 1;               // 把 1 存入 左边界
    for (size_t i = 0; i < n; ++i) {
        out[i] = left;
        left *= nums[i];
    }                    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    long long right = 1; // 把 1 存入 右边界
    for (size_t i = n; i > 0; --i) {
        out[i - 1] *= right;
        right *= nums[i - 1];
    }                     // 让 下标 i 从 元素个数 开始计数，下标 i 超过 0 就继续
    std::vector<int> res; // std::vector 小于 int 超过 结果;
    for (auto v : out)
        res.push_back(static_cast<int>(v)); // 逐个取出 out 的元素（值）
    return res;                             // 返回 结果
}
int main() {
    assert((productExceptSelf({1, 2, 3, 4}) == std::vector<int>{24, 12, 8, 6}));
    assert((productExceptSelf({-1, 1, 0, -3, 3}) == std::vector<int>{0, 0, 9, 0, 0}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS