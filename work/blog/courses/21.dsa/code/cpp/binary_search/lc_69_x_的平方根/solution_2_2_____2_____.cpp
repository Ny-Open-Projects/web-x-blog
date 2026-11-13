// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
// LeetCode 69. x 的平方根 — C++ 版（2 ) 方案2：二分（保留 ans））
#include <cassert>                      // 引入头文件
#include <cstdint>                      // 引入头文件
#include <iostream>                     // 引入头文件
static int64_t mySqrt(int64_t x) {      // 定义函数/方法 mySqrt
    int64_t lo = 0, hi = x, ans = 0;    // 把 0, 右边界 赋值为 x, 答案 赋值为 0; 写入 int64_t lo
    while (lo <= hi) {                  // 循环，直到不满足「左边界 不超过 右边界」
        int64_t m = lo + (hi - lo) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2; 写入 int64_t m
        if (m * m <= x) {
            ans = m;
            lo = m + 1;
        } else
            hi = m - 1;
    }
    return ans; // 返回 答案
}
int main() { // 程序入口：跑内嵌自测用例
    int64_t cs[4][2] = {{4, 2}, {8, 2}, {16, 4}, {2147395599LL, 46339}};
    for (auto &c : cs)
        assert(mySqrt(c[0]) == c[1]); // 逐个取出 cs 的元素（字符）
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
}
