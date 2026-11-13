/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135256754 */
/* LeetCode 76. 最小覆盖子串 — C 版（方案3） */
#include <stdio.h>                                                 // 引入头文件
#include <string.h>                                                // 引入头文件
static void min_window(const char *s, const char *t, char out[]) { // 定义函数/方法 min_window
    out[0] = '\0';                                                 // 把 '\0'; 写入 out[0]
    int sl = (int)strlen(s),
        tl = (int)strlen(t); // 把 (int)strlen(字符串), tl 赋值为 (int)strlen(另一字符串) 存入 sl
    if (sl == 0 || tl == 0)
        return;                               // 若 sl 等于 0 或 tl 等于 0) return;
    int target[256] = {0}, window[256] = {0}; // 把 {0}, window[256] 赋值为 {0}; 写入 int target[256]
    for (int i = 0; i < tl; i++)
        target[(unsigned char)t[i]]++; // 让 下标 i 从 0 开始计数，下标 i 小于 tl 就继续
    int required = 0;                  // 把 0 存入 required
    for (int i = 0; i < 256; i++)
        if (target[i] > 0)
            required++; // 让 下标 i 从 0 开始计数，下标 i 小于 256 就继续
    int left = 0, formed = 0, min_len = 1 << 30, min_left = 0;
    for (int right = 0; right < sl; right++) { // 让 右边界 从 0 开始计数，右边界 小于 sl 就继续
        unsigned char c = (unsigned char)s[right]; // 把 (unsigned char)字符串[右边界]; 写入 unsigned char c
        window[c]++;                               // window[字符] 加一 ;
        if (target[c] > 0 && window[c] == target[c])
            formed++; // 若 目标值[字符] 超过 0 且 window[字符] 等于 目标值[字符]) formed 加一 ;
        while (formed == required) { // 循环，直到不满足「formed 等于 required」
            if (right - left + 1 < min_len) {
                min_len = right - left + 1;
                min_left = left;
            }
            unsigned char lc =
                (unsigned char)s[left]; // 把 (unsigned char)字符串[左边界]; 写入 unsigned char lc
            window[lc]--;               // window[lc] 减一 ;
            if (target[lc] > 0 && window[lc] < target[lc])
                formed--; // 若 目标值[lc] 超过 0 且 window[lc] 小于 目标值[lc]) formed 减一 ;
            left++;       // 左边界 加一
        }
    }
    if (min_len < (1 << 30)) {              // 若 min_len 小于 (1 小于 小于 30
        memcpy(out, s + min_left, min_len); // memcpy(out, 字符串 加 min_left, min_len);
        out[min_len] = '\0';                // 把 '\0'; 写入 out[min_len]
    }
}
int main(void) {                             // 程序入口：跑内嵌自测用例
    char out[4096];                          // char out[4096];
    min_window("ADOBECODEBANC", "ABC", out); // min_window(「ADOBECODEBANC」, 「ADOBECODEBANC」, out);
    if (strcmp(out, "BANC") != 0) {
        printf("FAIL 1 got %s\n", out);
        return 1;
    } // 若 strcmp(out, 「BANC」) 不等于 0) { 输出「BANC」, out); return 1; }
    min_window("a", "a", out); // min_window(「数组」, 「数组」, out);
    if (strcmp(out, "a") != 0) {
        printf("FAIL 2\n");
        return 1;
    } // 若 strcmp(out, 「数组」) 不等于 0) { 输出「数组」); return 1; }
    min_window("a", "aa", out); // min_window(「数组」, 「数组」, out);
    if (strcmp(out, "") != 0) {
        printf("FAIL 3\n");
        return 1;
    }                 // 若 strcmp(out, 「」) 不等于 0) { 输出「」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
