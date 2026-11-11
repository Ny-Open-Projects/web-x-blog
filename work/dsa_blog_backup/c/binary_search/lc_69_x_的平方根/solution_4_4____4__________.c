/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
 * LeetCode 69. x 的平方根 — C 版（4 ) 方案4：二分（返回 hi）） */
#include <stdio.h>                   // 引入头文件
static long my_sqrt(long x) {        // 定义函数/方法 my_sqrt
    long lo = 1, hi = x;             // 把 1, 右边界 赋值为 x; 写入 long lo
    while (lo <= hi) {               // 循环，直到不满足「左边界 不超过 右边界」
        long m = lo + (hi - lo) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2; 写入 long m
        if (m * m == x)
            return m; // 若 映射表 乘 映射表 等于 x，直接返回 映射表
        else if (m * m < x)
            lo = m + 1;
        else
            hi = m - 1; // 否则，若 映射表 乘 映射表 小于 x) 左边界 赋值为 映射表 加 1; else 右边界 赋值为
                        // 映射表 减 1;
    }
    return hi; // 返回 右边界
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
