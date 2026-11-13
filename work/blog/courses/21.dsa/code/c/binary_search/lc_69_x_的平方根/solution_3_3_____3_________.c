/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
 * LeetCode 69. x 的平方根 — C 版（3 ) 方案3：牛顿迭代） */
#include <stdio.h>            // 引入头文件
static long my_sqrt(long x) { // 定义函数/方法 my_sqrt
    if (x < 2)
        return x; // 若 x 小于 2，直接返回 x
    long r = x;   // 把 x; 写入 long r
    while (r * r > x)
        r = (r + x / r) /
            2; // 循环，直到不满足「右指针 乘 右指针 超过 x) 右指针 赋值为 (右指针 加 x 除以 右指针) 除以 2;」
    return r;  // 返回 右指针
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
