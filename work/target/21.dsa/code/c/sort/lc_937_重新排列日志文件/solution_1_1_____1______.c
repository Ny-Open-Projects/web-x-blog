/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/139965098 */
/* LeetCode 937. 重新排列日志文件 — C 版（方案1） */
#include <stdio.h>                               // 引入头文件
#include <stdlib.h>                              // 引入头文件
#include <string.h>                              // 引入头文件
static const char *content_of(const char *log) { // static const char 乘 content_of(const char 乘 log) {
    const char *sp = strchr(log, ' ');           // 把 strchr(log, ' '); 写入 const char *sp
    return sp ? sp + 1 : "";                     // 返回 sp ? sp 加 1 : 「」
}
static int is_digit_log(const char *log) { // 定义判定函数 is_digit_log
    const char *c = content_of(log);       // 把 content_of(log); 写入 const char *c
    return c[0] >= '0' && c[0] <= '9';     // 返回 字符[0] 不低于 '0' 且 字符[0] 不超过 '9'
}
static int cmp_letter(const void *a, const void *b) { // 定义函数/方法 cmp_letter
    const char *la = *(const char **)a; // 把 乘 (const char 乘 乘 )数组; 写入 const char *la
    const char *lb = *(const char **)b; // 把 乘 (const char 乘 乘 )b; 写入 const char *lb
    int cr = strcmp(content_of(la), content_of(lb)); // 把 strcmp(content_of(la), content_of(lb)) 存入 cr
    if (cr != 0)
        return cr;         // 若 cr 不等于 0，直接返回 cr
    return strcmp(la, lb); // 返回 strcmp(la, lb)
}
static int reorder_log_files(const char *logs[], int n,
                             const char *out[]) { // 定义函数/方法 reorder_log_files
    const char *letter[64], *digit[64];           // const char 乘 letter[64], 乘 digit[64];
    int ln = 0, dn = 0;                           // 把 0, dn 赋值为 0 存入 ln
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        if (is_digit_log(logs[i]))
            digit[dn++] = logs[i]; // 若 is_digit_log(logs[下标 i])) digit[dn 加一 ] 赋值为 logs[下标 i];
        else
            letter[ln++] = logs[i]; // 否则
    }
    qsort(letter, ln, sizeof(char *), cmp_letter); // qsort(letter, ln, sizeof(char 乘 ), cmp_letter);
    for (int i = 0; i < ln; i++)
        out[i] = letter[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 ln 就继续
    for (int i = 0; i < dn; i++)
        out[ln + i] = digit[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 dn 就继续
    return ln + dn;             // 返回 ln 加 dn
}
int main(void) { // 程序入口：跑内嵌自测用例
    const char *logs[] = {"a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"};
    const char *wants[] = {"g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"};
    const char *out[64];                     // const char 乘 out[64];
    int n = reorder_log_files(logs, 5, out); // 把 reorder_log_files(logs, 5, out) 存入 元素个数
    if (n != 5) {
        printf("FAIL n\n");
        return 1;
    } // 若 元素个数 不等于 5) { 输出「FAIL 元素个数 」); return 1; }
    for (int i = 0; i < 5; i++)
        if (strcmp(out[i], wants[i]) != 0) {
            printf("FAIL %d: %s\n", i, out[i]);
            return 1;
        }             // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
