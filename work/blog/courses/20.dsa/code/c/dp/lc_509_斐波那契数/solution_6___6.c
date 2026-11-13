/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130510175 */
/* LeetCode 509. 斐波那契数 — C 版（方案6） */
#include <stdio.h> // 引入头文件
static int fib(int n) {
    if (n < 2)
        return n;
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int t = a + b;
        a = b;
        b = t;
    }
    return b;
}
int main(void) {
    if (fib(2) != 1 || fib(3) != 2 || fib(4) != 3 || fib(10) != 55) {
        printf("FAIL\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS