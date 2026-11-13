/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588 */
/* 动态规划之Fibonacci — C 版（方案2） */
#include <stdio.h>      // 引入头文件
static long memo_g[64]; // static long memo_g[64];
static long go(int n) { // 定义函数/方法 go
    if (n <= 1)
        return n; // 若 元素个数 不超过 1，直接返回 元素个数
    if (memo_g[n])
        return memo_g[n];              // 若 memo_g[元素个数]，直接返回 memo_g[元素个数]
    memo_g[n] = go(n - 1) + go(n - 2); // 把 go(元素个数 减 1) 加 go(元素个数 减 2); 写入 memo_g[n]
    return memo_g[n];                  // 返回 memo_g[元素个数]
}
static long fib_memo(int n) { // 定义函数/方法 fib_memo
    for (int i = 0; i < 64; i++)
        memo_g[i] = 0; // 让 下标 i 从 0 开始计数，下标 i 小于 64 就继续
    return go(n);      // 返回 go(元素个数)
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (fib_memo(10) != 55 || fib_memo(20) != 6765 || fib_memo(0) != 0) {
        printf("FAIL\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS