// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135424151
// LeetCode 292. Nim游戏 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
static bool canWinNim(long long n) { return n % 4 != 0; }
int main() {                          // 程序入口：跑内嵌自测用例
    assert(!canWinNim(4));            // 断言校验
    assert(canWinNim(1));             // 断言校验
    assert(canWinNim(2));             // 断言校验
    assert(!canWinNim(8));            // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
