// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130497821
// LeetCode 53. 最大子数组和 — C++ 版（方案3）
#include <algorithm>                                   // 引入头文件
#include <cassert>                                     // 引入头文件
#include <iostream>                                    // 引入头文件
#include <vector>                                      // 引入头文件
static int maxSubArray(const std::vector<int> &nums) { // 定义函数/方法 maxSubArray
    int best = nums[0], cur = nums[0]; // 把 数组[0], 当前值 赋值为 数组[0] 存入 当前最优
    for (size_t i = 1; i < nums.size(); ++i) { // 让 下标 i 从 1 开始计数，下标 i 小于 数组.大小() 就继续
        cur = std::max(cur + nums[i],
                       nums[i]); // 把 std::取较大值 当前值 加 数组[下标 i], 数组[下标 i]); 写入 当前值
        best = std::max(best, cur); // 把 std::取较大值 当前最优, 当前值); 写入 当前最优
    }
    return best; // 返回 当前最优
}
int main() {
    assert(maxSubArray({-2, 1, -3, 4, -1, 2, 1, -5, 4}) == 6);
    assert(maxSubArray({1}) == 1);
    assert(maxSubArray({5, 4, -1, 7, 8}) == 23);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS