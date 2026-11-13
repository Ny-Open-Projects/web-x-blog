/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
 * LeetCode 69. x 的平方根 — C 版（2 ) 方案2：二分（保留 ans）） */
#include <stdio.h>                   // 引入头文件
static long my_sqrt(long x) {        // 定义函数/方法 my_sqrt
    long lo = 0, hi = x, ans = 0;    // 把 0, 右边界 赋值为 x, 答案 赋值为 0; 写入 long lo
    while (lo <= hi) {               // 循环，直到不满足「左边界 不超过 右边界」
        long m = lo + (hi - lo) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2; 写入 long m
        if (m * m <= x) {
            ans = m;
            lo = m + 1;
        } else
            hi = m - 1;
    }
    return ans; // 返回 答案
}
int main(void) { // 程序入口：跑内嵌自测用例
    long cs[4][2] = {{4, 2}, {8, 2}, {16, 4}, {2147395599, 46339}};
    for (int i = 0; i < 4; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
        if (my_sqrt(cs[i][0]) != cs[i][1]) {
            printf("FAIL %d\\n", i);
            return 1;
        }
    printf("PASS\\n"); // 全部用例通过，输出 PASS
    return 0;          // 返回 0
}
