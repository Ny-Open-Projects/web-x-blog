/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138290964 */
/* LeetCode 482. 密钥格式化 — C 版（方案2） */
#include <ctype.h>                                                     // 引入头文件
#include <stdio.h>                                                     // 引入头文件
#include <string.h>                                                    // 引入头文件
static void license_key_formatting(const char *s, int k, char out[]) { // 定义函数/方法 license_key_formatting
    char cleaned[8192];                                                // char cleaned[8192];
    int n = 0;                                                         // 把 0 存入 元素个数
    for (const char *p = s; *p; p++) { // 把 字符串; 乘 节点; 节点 加一 ) { 写入 for (const char *p
        if (*p != '-')
            cleaned[n++] = (char)toupper((unsigned char)*p);
    }
    int pos = 0; // 把 0 存入 pos
    if (n == 0) {
        out[0] = '\0';
        return;
    }                  // 若 元素个数 等于 0) { out[0] 赋值为 '\0'; return; }
    int first = n % k; // 把 元素个数 对…取模 下标 k 存入 first
    int idx = 0;       // 把 0 存入 idx
    if (first > 0) {   // 若 first 超过 0
        for (int i = 0; i < first; i++)
            out[pos++] = cleaned[idx++]; // 让 下标 i 从 0 开始计数，下标 i 小于 first 就继续
        if (idx < n)
            out[pos++] = '-'; // 若 idx 小于 元素个数) out[pos 加一 ] 赋值为 ' 减 ';
    }
    while (idx < n) { // 循环，直到不满足「idx 小于 元素个数」
        for (int i = 0; i < k; i++)
            out[pos++] = cleaned[idx++]; // 让 下标 i 从 0 开始计数，下标 i 小于 下标 k 就继续
        if (idx < n)
            out[pos++] = '-'; // 若 idx 小于 元素个数) out[pos 加一 ] 赋值为 ' 减 ';
    }
    out[pos] = '\0'; // 把 '\0'; 写入 out[pos]
}
int main(void) {    // 程序入口：跑内嵌自测用例
    char out[8192]; // char out[8192];
    license_key_formatting("5F3Z-2e-9-w", 4,
                           out); // license_key_formatting(「5F3Z 减 2e 减 9 减 权重」, 4, out);
    if (strcmp(out, "5F3Z-2E9W") != 0) {
        printf("FAIL 1 %s\n", out);
        return 1;
    }
    license_key_formatting("2-5g-3-J", 2, out); // license_key_formatting(「2 减 5g 减 3 减 J」, 2, out);
    if (strcmp(out, "2-5G-3J") != 0) {
        printf("FAIL 2 %s\n", out);
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
