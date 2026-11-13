// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130506068
// LeetCode 70. 爬楼梯 — C++ 版（方案6）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
static int climbStairs(int n) {
    if (n <= 2)
        return n;
    int a = 1, b = 2;
    for (int i = 3; i <= n; ++i) {
        int t = a + b;
        a = b;
        b = t;
    }
    return b;
}
int main() {
    assert(climbStairs(2) == 2);
    assert(climbStairs(3) == 3);
    assert(climbStairs(10) == 89);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS