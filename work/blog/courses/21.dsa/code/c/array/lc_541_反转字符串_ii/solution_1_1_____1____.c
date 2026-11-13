/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134588341 */
/* LeetCode 541. 反转字符串II — C 版（方案1） */
#include <stdio.h>                                          // 引入头文件
#include <string.h>                                         // 引入头文件
static void reverse_str(const char *s, int k, char out[]) { // 定义函数/方法 reverse_str
    int n = (int)strlen(s);                                 // 把 (int)strlen(字符串) 存入 元素个数
    int pos = 0;                                            // 把 0 存入 pos
    for (int i = 0; i < n; i += 2 * k) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        int end = i + k < n ? i + k
                            : n; // 把 下标 i 加 下标 k 小于 元素个数 ? 下标 i 加 下标 k : 元素个数 存入 终点
        for (int j = end - 1; j >= i; j--)
            out[pos++] = s[j]; // 让 下标 j 从 终点 减 1 开始计数，下标 j 不低于 下标 i 就继续
        for (int j = end; j < i + 2 * k && j < n; j++)
            out[pos++] = s[j]; // 让 下标 j 从 终点 开始计数，下标 j 小于 下标 i 加 2 乘 下标 k 且 下标 j 小于
                               // 元素个数 就继续
    }
    out[pos] = '\0'; // 把 '\0'; 写入 out[pos]
}
int main(void) {                    // 程序入口：跑内嵌自测用例
    char out[8192];                 // char out[8192];
    reverse_str("abcdefg", 2, out); // reverse_str(「abcdefg」, 2, out);
    if (strcmp(out, "bacdfeg") != 0) {
        printf("FAIL 1 %s\n", out);
        return 1;
    }
    reverse_str("abcd", 2, out); // reverse_str(「abcd」, 2, out);
    if (strcmp(out, "bacd") != 0) {
        printf("FAIL 2\n");
        return 1;
    }                           // 若 strcmp(out, 「bacd」) 不等于 0) { 输出「bacd」); return 1; }
    reverse_str("abc", 1, out); // reverse_str(「abc」, 1, out);
    if (strcmp(out, "abc") != 0) {
        printf("FAIL 3\n");
        return 1;
    } // 若 strcmp(out, 「abc」) 不等于 0) { 输出「abc」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS