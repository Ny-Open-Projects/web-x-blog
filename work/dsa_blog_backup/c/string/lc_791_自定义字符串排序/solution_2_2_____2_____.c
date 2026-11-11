/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136838836 */
/* LeetCode 791. 自定义字符串排序 — C 版（方案2） */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件
static void custom_sort_string(const char *order, const char *s,
                               char out[]) { // 定义函数/方法 custom_sort_string
    int count[26] = {0};                     // 把 {0}; 写入 int count[26]
    for (const char *p = s; *p; p++)
        count[*p - 'a']++;
    int pos = 0;                           // 把 0 存入 pos
    for (const char *p = order; *p; p++) { // 把 order; 乘 节点; 节点 加一 ) { 写入 for (const char *p
        int idx = *p - 'a';                // 把 乘 节点 减 '数组' 存入 idx
        for (int i = 0; i < count[idx]; i++)
            out[pos++] = *p; // 让 下标 i 从 0 开始计数，下标 i 小于 计数[idx] 就继续
        count[idx] = 0;      // 把 0; 写入 count[idx]
    }
    for (int i = 0; i < 26; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 26 就继续
        for (int j = 0; j < count[i]; j++)
            out[pos++] = 'a' + i; // 让 下标 j 从 0 开始计数，下标 j 小于 计数[下标 i] 就继续
    }
    out[pos] = '\0'; // 把 '\0'; 写入 out[pos]
}
int main(void) {                            // 程序入口：跑内嵌自测用例
    char out[8192];                         // char out[8192];
    custom_sort_string("cba", "abcd", out); // custom_sort_string(「cba」, 「cba」, out);
    if (strcmp(out, "cbad") != 0) {
        printf("FAIL 1 %s\n", out);
        return 1;
    } // 若 strcmp(out, 「cbad」) 不等于 0) { 输出「cbad」, out); return 1; }
    custom_sort_string("bcafg", "abcd", out); // custom_sort_string(「bcafg」, 「bcafg」, out);
    if (strcmp(out, "bcad") != 0) {
        printf("FAIL 2 %s\n", out);
        return 1;
    }                 // 若 strcmp(out, 「bcad」) 不等于 0) { 输出「bcad」, out); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
