// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133468105
// LeetCode 136. 只出现一次的数字 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <numeric>  // 引入头文件
#include <vector>   // 引入头文件
static int singleNumber(const std::vector<int> &nums) {
    return std::accumulate(nums.begin(), nums.end(), 0, std::bit_xor<int>());
}
int main() {
    assert(singleNumber({2, 2, 1}) == 1);
    assert(singleNumber({4, 1, 2, 1, 2}) == 4);
    assert(singleNumber({1}) == 1);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS