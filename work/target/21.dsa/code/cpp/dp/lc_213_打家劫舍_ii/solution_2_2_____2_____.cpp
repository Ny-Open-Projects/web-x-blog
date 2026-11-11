// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130716392
// LeetCode 213. 打家劫舍II — C++ 版（方案2）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件
static int robLine(const std::vector<int> &nums) {
    int a = 0, b = 0;
    for (int v : nums) {
        int t = std::max(b, a + v);
        a = b;
        b = t;
    }
    return b;
}
static int robII(const std::vector<int> &nums) { // 定义函数/方法 robII
    if (nums.size() == 1)
        return nums[0]; // 若 数组.大小() 等于 1，直接返回 数组[0]
    std::vector<int> skipFirst(
        nums.begin() + 1,
        nums.end()); // std::vector 小于 int 超过 skipFirst(数组 迭代位置 加 1, 数组.终点());
    std::vector<int> skipLast(nums.begin(),
                              nums.end() -
                                  1); // std::vector 小于 int 超过 skipLast(数组 迭代位置 , 数组.终点() 减 1);
    return std::max(robLine(skipFirst),
                    robLine(skipLast)); // 返回 std::取较大值 robLine(skipFirst), robLine(skipLast))
}
int main() {
    assert(robII({2, 3, 2}) == 3);
    assert(robII({1, 2, 3, 1}) == 4);
    assert(robII({1}) == 1);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS