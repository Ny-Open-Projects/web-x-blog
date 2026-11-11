// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
// LeetCode 69. x 的平方根 — C++ 版（1 ) 方案1：二分（精确区间判断））
#include <cassert>                 // 引入头文件
#include <cstdint>                 // 引入头文件
#include <iostream>                // 引入头文件
static int64_t mySqrt(int64_t x) { // 定义函数/方法 mySqrt
    if (x < 2)
        return x;                       // 若 x 小于 2，直接返回 x
    int64_t lo = 1, hi = x / 2;         // 把 1, 右边界 赋值为 x 除以 2; 写入 int64_t lo
    while (lo <= hi) {                  // 循环，直到不满足「左边界 不超过 右边界」
        int64_t m = lo + (hi - lo) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2; 写入 int64_t m
        if (m * m <= x && x < (m + 1) * (m + 1))
            return m; // 若 映射表 乘 映射表 不超过 x 且 x 小于 (映射表 加 1) 乘 (映射表 加 1)，直接返回
                      // 映射表
        else if (m * m > x)
            hi = m - 1;
        else
            lo = m + 1; // 否则，若 映射表 乘 映射表 超过 x) 右边界 赋值为 映射表 减 1; else 左边界 赋值为
                        // 映射表 加 1;
    }
    return lo; // 返回 左边界
}
int main() { // 程序入口：跑内嵌自测用例
    int64_t cs[4][2] = {{4, 2}, {8, 2}, {16, 4}, {2147395599LL, 46339}};
    for (auto &c : cs)
        assert(mySqrt(c[0]) == c[1]); // 逐个取出 cs 的元素（字符）
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
}
