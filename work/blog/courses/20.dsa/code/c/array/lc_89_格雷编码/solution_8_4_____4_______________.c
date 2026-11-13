/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134866839 */
/* LeetCode 89. 格雷编码 — C 版（方案8） */
#include <stdio.h>                       // 引入头文件
static int gray_code(int n, int out[]) { // 定义函数/方法 gray_code
    int m = 1 << n;                      // 把 1 小于 小于 元素个数 存入 映射表
    for (int i = 0; i < m; i++)
        out[i] = i ^ (i >> 1); // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
    return m;                  // 返回 映射表
}
int main(void) {           // 程序入口：跑内嵌自测用例
    int out[4096], n;      // int out[4096], 元素个数;
    n = gray_code(2, out); // 把 gray_code(2, out); 写入 元素个数
    if (n != 4 || out[0] != 0 || out[1] != 1 || out[2] != 3 || out[3] != 2) {
        printf("FAIL 1\n");
        return 1;
    }
    n = gray_code(1, out); // 把 gray_code(1, out); 写入 元素个数
    if (n != 2 || out[0] != 0 || out[1] != 1) {
        printf("FAIL 2\n");
        return 1;
    }
    n = gray_code(3, out); // 把 gray_code(3, out); 写入 元素个数
    if (n != 8) {
        printf("FAIL 3\n");
        return 1;
    }                             // 若 元素个数 不等于 8) { 输出「FAIL 3 」); return 1; }
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        int nxt = out[(i + 1) % n]; // 把 out[(下标 i 加 1) 对…取模 元素个数] 存入 nxt
        int diff = out[i] ^ nxt;    // 把 out[下标 i] 按位异或 nxt 存入 差值
        int bits = 0;               // 把 0 存入 bits
        while (diff) {
            bits += diff & 1;
            diff >>= 1;
        } // 循环，直到不满足「差值) { bits 累加 差值 按位与 1; 差值 超过 不低于 1; }」
        if (bits != 1) {
            printf("FAIL gray\n");
            return 1;
        } // 若 bits 不等于 1) { 输出「FAIL gray 」); return 1; }
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS