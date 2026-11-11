// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
// 数据结构与算法之排序: 计数排序 — C++ 版（方案4）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> countSort(const std::vector<int> &nums) {
    if (nums.empty())
        return nums;                // 若 数组 是否为空，直接返回 数组
    int mx = nums[0], mn = nums[0]; // 把 数组[0], mn 赋值为 数组[0] 存入 mx
    for (int v : nums) {
        mx = std::max(mx, v);
        mn = std::min(mn, v);
    }
    int range = mx - mn + 1; // 把 mx 减 mn 加 1 存入 range
    std::vector<int> count(range, 0),
        output(nums.size()); // std::vector 小于 int 超过 计数(range, 0), 输出(数组.大小());
    for (int v : nums)
        count[v - mn]++; // for (int 值 : 数组) 计数[值 减 mn] 加一 ;
    for (int i = 1; i < range; ++i)
        count[i] += count[i - 1]; // 让 下标 i 从 1 开始计数，下标 i 小于 range 就继续
    for (int i = static_cast<int>(nums.size()) - 1; i >= 0; --i) {
        output[--count[nums[i] - mn]] = nums[i]; // 把 数组[下标 i]; 写入 output[--count[nums[i] - mn]]
    }
    return output; // 返回 输出
}
int main() { // 程序入口：跑内嵌自测用例
    assert((countSort({5, 3, 8, 3, 1}) == std::vector<int>{1, 3, 3, 5, 8})); // 断言校验
    auto big = countSort(
        {102, 103, 108, 107, 101, 102, 102, 102, 107, 103, 109, 108, 102, 101, 104, 102, 104, 106, 109, 102});
    assert(big.size() == 20 && big.front() == 101 && big.back() == 109); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS