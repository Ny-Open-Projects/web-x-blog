// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138671078
// LeetCode 1356. 根据数字二进制下1的数目排序 — C++ 版（方案2）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件
static int countBits(int n) {
    int c = 0;
    while (n) {
        c += n & 1;
        n >>= 1;
    }
    return c;
}
static std::vector<int> sortByBits(std::vector<int> nums) {
    std::sort(nums.begin(), nums.end(),
              [](int a, int b) { // std::sort(数组 迭代位置 , 数组.终点(), [](int 数组, int b) {
                  int ba = countBits(a),
                      bb = countBits(b); // 把 countBits(数组), bb 赋值为 countBits(b) 存入 ba
                  if (ba != bb)
                      return ba < bb; // 若 ba 不等于 bb，直接返回 ba 小于 bb
                  return a < b;       // 返回 数组 小于 b
              });                     // });
    return nums;                      // 返回 数组
}
int main() { // 程序入口：跑内嵌自测用例
    assert(
        (sortByBits({0, 1, 2, 3, 4, 5, 6, 7, 8}) == std::vector<int>{0, 1, 2, 4, 8, 3, 5, 6, 7})); // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
