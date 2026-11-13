// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
// LeetCode 69. x 的平方根 — C++ 版（3 ) 方案3：牛顿迭代）
#include <cassert>                 // 引入头文件
#include <cstdint>                 // 引入头文件
#include <iostream>                // 引入头文件
static int64_t mySqrt(int64_t x) { // 定义函数/方法 mySqrt
    if (x < 2)
        return x;  // 若 x 小于 2，直接返回 x
    int64_t r = x; // 把 x; 写入 int64_t r
    while (r * r > x)
        r = (r + x / r) /
            2; // 循环，直到不满足「右指针 乘 右指针 超过 x) 右指针 赋值为 (右指针 加 x 除以 右指针) 除以 2;」
    return r;  // 返回 右指针
}
int main() { // 程序入口：跑内嵌自测用例
    int64_t cs[4][2] = {{4, 2}, {8, 2}, {16, 4}, {2147395599LL, 46339}};
    for (auto &c : cs)
        assert(mySqrt(c[0]) == c[1]); // 逐个取出 cs 的元素（字符）
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
}
