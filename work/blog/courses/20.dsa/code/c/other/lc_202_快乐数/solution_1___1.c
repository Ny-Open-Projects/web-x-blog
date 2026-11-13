/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135124945 */
/* LeetCode 202. 快乐数 — C 版（方案1） */
#include <stdio.h>                   // 引入头文件
static long bit_square_sum(long n) { // 定义函数/方法 bit_square_sum
    long s = 0;                      // 把 0; 写入 long s
    while (n > 0) {
        long d = n % 10;
        s += d * d;
        n /= 10;
    }
    return s; // 返回 字符串
}
static int is_happy(long n) { // 定义判定函数 is_happy
    long seen[1024];          // long 已见集合[1024];
    int cnt = 0;              // 把 0 存入 计数
    while (n != 1) {          // 循环，直到不满足「元素个数 不等于 1」
        for (int i = 0; i < cnt; i++)
            if (seen[i] == n)
                return 0; // 让 下标 i 从 0 开始计数，下标 i 小于 计数 就继续
        if (cnt < 1024)
            seen[cnt++] = n;   // 若 计数 小于 1024) 已见集合[计数 加一 ] 赋值为 元素个数;
        n = bit_square_sum(n); // 把 bit_square_sum(元素个数); 写入 元素个数
    }
    return 1; // 返回 1
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (bit_square_sum(1) != 1) {
        printf("FAIL a1\n");
        return 1;
    } // 若 bit_square_sum(1) 不等于 1) { 输出「FAIL a1 」); return 1; }
    if (bit_square_sum(19) != 82) {
        printf("FAIL a2\n");
        return 1;
    } // 若 bit_square_sum(19) 不等于 82) { 输出「FAIL a2 」); return 1; }
    if (bit_square_sum(82) != 68) {
        printf("FAIL a3\n");
        return 1;
    } // 若 bit_square_sum(82) 不等于 68) { 输出「FAIL a3 」); return 1; }
    if (!is_happy(19) || !is_happy(1) || is_happy(2)) {
        printf("FAIL b\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
