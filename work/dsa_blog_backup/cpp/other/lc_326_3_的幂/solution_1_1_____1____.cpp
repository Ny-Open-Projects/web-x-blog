// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135359346
// LeetCode 326. 3的幂 — C++ 版（方案1）
#include <cassert>                        // 引入头文件
#include <iostream>                       // 引入头文件
static bool isPowerOfThree(long long n) { // 定义判定函数 isPowerOfThree
    while (n != 0 && n % 3 == 0)
        n /= 3; // 循环，直到不满足「元素个数 不等于 0 且 元素个数 对…取模 3 等于 0) 元素个数 除以 3;」
    return n == 1; // 返回 元素个数 等于 1
}
int main() {                          // 程序入口：跑内嵌自测用例
    assert(isPowerOfThree(27));       // 断言校验
    assert(!isPowerOfThree(0));       // 断言校验
    assert(isPowerOfThree(9));        // 断言校验
    assert(!isPowerOfThree(-1));      // 断言校验
    assert(isPowerOfThree(1));        // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
