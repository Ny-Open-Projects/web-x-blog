// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130644389
// LeetCode 198. 打家劫舍 — C++ 版（方案1）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件
static int rob(const std::vector<int> &nums) {
    int a = 0, b = 0;
    for (int v : nums) {
        int t = std::max(b, a + v);
        a = b;
        b = t;
    }
    return b;
}
int main() {
    assert(rob({1, 2, 3, 1}) == 4);
    assert(rob({2, 7, 9, 3, 1}) == 12);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS