// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134424807
// LeetCode 485. 最大连续1的个数 — C++ 版（方案1）
#include <cassert>                                                // 引入头文件
#include <iostream>                                               // 引入头文件
#include <vector>                                                 // 引入头文件
static int findMaxConsecutiveOnes(const std::vector<int> &nums) { // 定义函数/方法 findMaxConsecutiveOnes
    int best = 0, cur = 0; // 把 0, 当前值 赋值为 0 存入 当前最优
    for (int v : nums) {   // for (int 值 : 数组) {
        if (v == 1) {
            ++cur;
            best = std::max(best, cur);
        } // 若 值 等于 1) { 加一 当前值; 当前最优 赋值为 std::取较大值 当前最优, 当前值); }
        else
            cur = 0; // 否则
    }
    return best; // 返回 当前最优
}
int main() {
    assert(findMaxConsecutiveOnes({1, 1, 0, 1, 1, 1}) == 3);
    assert(findMaxConsecutiveOnes({1, 0, 1, 1, 0, 1}) == 2);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS