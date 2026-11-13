// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/99759428
// 数据结构与算法之数组操作 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> twoSum(const std::vector<int> &nums, int target) {
    for (size_t i = 0; i < nums.size(); ++i) // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
        for (size_t j = i + 1; j < nums.size();
             ++j) // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 数组.大小() 就继续
            if (nums[i] + nums[j] == target)
                return {static_cast<int>(i), static_cast<int>(j)};
    return {}; // 返回 {}
}
static int maxSubArray(const std::vector<int> &nums) { // 定义函数/方法 maxSubArray
    int best = nums[0], cur = nums[0]; // 把 数组[0], 当前值 赋值为 数组[0] 存入 当前最优
    for (size_t i = 1; i < nums.size(); ++i) { // 让 下标 i 从 1 开始计数，下标 i 小于 数组.大小() 就继续
        cur = std::max(cur + nums[i],
                       nums[i]); // 把 std::取较大值 当前值 加 数组[下标 i], 数组[下标 i]); 写入 当前值
        best = std::max(best, cur); // 把 std::取较大值 当前最优, 当前值); 写入 当前最优
    }
    return best; // 返回 当前最优
}
static std::vector<int> rotateArray(const std::vector<int> &nums, int k) {
    auto v = nums;            // 把 数组 存入 值
    size_t n = v.size();      // 把 值.大小(); 写入 size_t n
    k %= static_cast<int>(n); // 把 static_cast 小于 int 超过 (元素个数); 写入 k %
    std::rotate(v.begin(), v.begin() + n - k,
                v.end()); // std::rotate(值 迭代位置 , 值 迭代位置 加 元素个数 减 下标 k, 值.终点());
    return v;             // 返回 值
}
int main() {                                                       // 程序入口：跑内嵌自测用例
    assert((twoSum({2, 7, 11, 15}, 9) == std::vector<int>{0, 1})); // 断言校验
    assert(maxSubArray({-2, 1, -3, 4, -1, 2, 1, -5, 4}) == 6);     // 断言校验
    assert((rotateArray({1, 2, 3, 4, 5, 6, 7}, 3) == std::vector<int>{5, 6, 7, 1, 2, 3, 4})); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS