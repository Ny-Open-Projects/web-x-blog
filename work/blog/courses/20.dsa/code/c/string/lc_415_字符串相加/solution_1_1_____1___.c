/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130736023 */
/* LeetCode 415. 字符串相加 — C 版（方案1） */
#include <stdio.h>                                                  // 引入头文件
#include <string.h>                                                 // 引入头文件
static void add_strings(const char *a, const char *b, char out[]) { // 定义函数/方法 add_strings
    int i = (int)strlen(a) - 1, j = (int)strlen(b) - 1, carry = 0, n = 0;
    while (i >= 0 || j >= 0 || carry) { // 循环，直到不满足「下标 i 不低于 0 或 下标 j 不低于 0 或 carry」
        int total = carry; // 把 carry 存入 总和
        if (i >= 0) {
            total += a[i] - '0';
            i--;
        } // 若 下标 i 不低于 0) { 总和 累加 数组[下标 i] 减 '0'; 下标 i 减一 ; }
        if (j >= 0) {
            total += b[j] - '0';
            j--;
        } // 若 下标 j 不低于 0) { 总和 累加 b[下标 j] 减 '0'; 下标 j 减一 ; }
        out[n++] = '0' + total % 10; // 把 '0' 加 总和 对…取模 10; 写入 out[n++]
        carry = total / 10;          // 把 总和 除以 10; 写入 carry
    }
    if (n == 0)
        out[n++] = '0'; // 若 元素个数 等于 0) out[元素个数 加一 ] 赋值为 '0';
    out[n] = '\0';      // 把 '\0'; 写入 out[n]
    for (int l = 0, r = n - 1; l < r; l++, r--) {
        char t = out[l];
        out[l] = out[r];
        out[r] = t;
    } // 让 左指针 从 0, 右指针 赋值为 元素个数 减 1 开始计数，左指针 小于 右指针 就继续
}
int main(void) {                   // 程序入口：跑内嵌自测用例
    char out[9000];                // char out[9000];
    add_strings("11", "123", out); // add_strings(「11」, 「11」, out);
    if (strcmp(out, "134") != 0) {
        printf("FAIL 1\n");
        return 1;
    }                              // 若 strcmp(out, 「134」) 不等于 0) { 输出「134」); return 1; }
    add_strings("456", "77", out); // add_strings(「456」, 「456」, out);
    if (strcmp(out, "533") != 0) {
        printf("FAIL 2\n");
        return 1;
    }                           // 若 strcmp(out, 「533」) 不等于 0) { 输出「533」); return 1; }
    add_strings("0", "0", out); // add_strings(「0」, 「0」, out);
    if (strcmp(out, "0") != 0) {
        printf("FAIL 3\n");
        return 1;
    }                 // 若 strcmp(out, 「0」) 不等于 0) { 输出「0」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
