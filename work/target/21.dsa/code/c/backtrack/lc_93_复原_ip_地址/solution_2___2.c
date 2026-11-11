/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138771574 */
/* LeetCode 93. 复原IP地址 — C 版（方案2） */
#include <stdio.h>                             // 引入头文件
#include <string.h>                            // 引入头文件
static int valid_seg(const char *s, int len) { // 定义函数/方法 valid_seg
    if (len == 0 || len > 3)
        return 0; // 若 长度 等于 0 或 长度 超过 3，直接返回 0
    if (len > 1 && s[0] == '0')
        return 0; // 若 长度 超过 1 且 字符串[0] 等于 '0'，直接返回 0
    int v = 0;    // 把 0 存入 值
    for (int i = 0; i < len; i++)
        v = v * 10 + (s[i] - '0'); // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
    return v <= 255;               // 返回 值 不超过 255
}
static int restore_ip_addresses(const char *s, char out[][16]) { // 定义函数/方法 restore_ip_addresses
    int res = 0;                                                 // 把 0 存入 结果
    int n = (int)strlen(s); // 把 (int)strlen(字符串) 存入 元素个数
    if (n < 4 || n > 12)
        return 0;                    // 若 元素个数 小于 4 或 元素个数 超过 12，直接返回 0
    for (int a = 1; a <= 3; a++)     // 让 数组 从 1 开始计数，数组 不超过 3 就继续
        for (int b = 1; b <= 3; b++) // 让 b 从 1 开始计数，b 不超过 3 就继续
            for (int c = 1; c <= 3; c++) { // 让 字符 从 1 开始计数，字符 不超过 3 就继续
                int d = n - a - b - c;     // 把 元素个数 减 数组 减 b 减 字符 存入 d
                if (d < 1 || d > 3)
                    continue; // 若 d 小于 1 或 d 超过 3) continue;
                if (valid_seg(s, a) && valid_seg(s + a, b) && valid_seg(s + a + b, c) &&
                    valid_seg(s + a + b + c, d)) {
                    snprintf(out[res], 16, "%.*s.%.*s.%.*s.%.*s", a, s, b, s + a, c, s + a + b, d,
                             s + a + b + c); // 打印输出
                    res++;                   // 结果 加一
                }
            }
    return res; // 返回 结果
}
int main(void) {      // 程序入口：跑内嵌自测用例
    char out[64][16]; // char out[64][16];
    int n = restore_ip_addresses("25525511135",
                                 out); // 把 restore_ip_addresses(「25525511135」, out) 存入 元素个数
    if (n != 2) {
        printf("FAIL cnt=%d\n", n);
        return 1;
    } // 若 元素个数 不等于 2) { 输出「FAIL 计数 赋值为 对…取模 d 」, 元素个数); return 1; }
    if (strcmp(out[0], "255.255.11.135") != 0 || strcmp(out[1], "255.255.111.35") != 0) {
        printf("FAIL ips\n");
        return 1;
    }
    n = restore_ip_addresses("0000", out); // 把 restore_ip_addresses(「0000」, out); 写入 元素个数
    if (n != 1 || strcmp(out[0], "0.0.0.0") != 0) {
        printf("FAIL 2\n");
        return 1;
    }
    if (restore_ip_addresses("abc", out) != 0) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
