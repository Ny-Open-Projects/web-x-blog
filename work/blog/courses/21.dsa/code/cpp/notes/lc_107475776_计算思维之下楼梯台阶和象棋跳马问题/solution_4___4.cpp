// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
// 计算思维之下楼梯台阶和象棋跳马问题 — C++ 版（方案4）
#include <cassert>                            // 引入头文件
#include <iostream>                           // 引入头文件
static long long climbStairsVariants(int n) { // static long long climbStairsVariants(int 元素个数) {
    if (n <= 1)
        return 1;           // 若 元素个数 不超过 1，直接返回 1
    long long a = 1, b = 1; // 把 1, b 赋值为 1 存入 数组
    for (int i = 2; i <= n; ++i) {
        long long t = a + b;
        a = b;
        b = t;
    }         // 让 下标 i 从 2 开始计数，下标 i 不超过 元素个数 就继续
    return b; // 返回 b
}
int main() {
    assert(climbStairsVariants(10) == 89);
    assert(climbStairsVariants(1) == 1);
    assert(climbStairsVariants(2) == 2);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS