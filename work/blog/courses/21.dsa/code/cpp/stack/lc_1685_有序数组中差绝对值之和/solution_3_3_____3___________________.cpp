// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136236962
// LeetCode 1685. 有序数组中差绝对值之和 — C++ 版（方案3）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> getSumAbsoluteDifferences(const std::vector<int> &nums) {
    size_t n = nums.size(); // 把 数组.大小(); 写入 size_t n
    long long total = 0;    // 把 0 存入 总和
    for (int v : nums)
        total += v;                  // 把 值; 写入 for (int v : nums) total +
    long long prefix = 0;            // 把 0 存入 prefix
    std::vector<int> out;            // std::vector 小于 int 超过 out;
    for (size_t i = 0; i < n; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        long long v = nums[i];       // 把 数组[下标 i] 存入 值
        long long left = v * static_cast<long long>(i) -
                         prefix; // 把 值 乘 static_cast 小于 long long 超过 (下标 i) 减 prefix 存入 左边界
        long long right = (total - prefix - v) - v * static_cast<long long>(n - 1 - i);
        out.push_back(
            static_cast<int>(left + right)); // out 追加 static_cast 小于 int 超过 (左边界 加 右边界));
        prefix += v;                         // prefix累加 值
    }
    return out; // 返回 out
}
int main() {
    assert((getSumAbsoluteDifferences({2, 3, 5}) == std::vector<int>{4, 3, 5}));
    assert((getSumAbsoluteDifferences({1, 4, 6, 8, 10}) == std::vector<int>{24, 15, 13, 15, 21}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS