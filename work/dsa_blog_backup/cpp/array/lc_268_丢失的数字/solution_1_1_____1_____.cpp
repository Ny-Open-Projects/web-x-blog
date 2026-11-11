// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133968437
// LeetCode 268. 丢失的数字 — C++ 版（方案1）
#include <cassert>                                       // 引入头文件
#include <iostream>                                      // 引入头文件
#include <numeric>                                       // 引入头文件
#include <vector>                                        // 引入头文件
static int missingNumber(const std::vector<int> &nums) { // 定义函数/方法 missingNumber
    long long n =
        static_cast<long long>(nums.size()); // 把 static_cast 小于 long long 超过 (数组.大小()) 存入 元素个数
    long long sum = std::accumulate(nums.begin(), nums.end(),
                                    0LL); // 把 std::accumulate(数组 迭代位置 , 数组.终点(), 0LL) 存入 累计和
    return static_cast<int>(
        n * (n + 1) / 2 -
        sum); // 返回 static_cast 小于 int 超过 (元素个数 乘 (元素个数 加 1) 除以 2 减 累计和)
}
int main() {
    assert(missingNumber({3, 0, 1}) == 2);
    assert(missingNumber({0, 1}) == 2);
    assert(missingNumber({9, 6, 4, 2, 3, 5, 7, 0, 1}) == 8);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS