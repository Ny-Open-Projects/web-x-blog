/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135154838 */
/* LeetCode 242. 有效的字母异位词 — C 版（方案2） */
#include <stdio.h>                                    // 引入头文件
#include <string.h>                                   // 引入头文件
static int is_anagram(const char *s, const char *t) { // 定义判定函数 is_anagram
    size_t ls = strlen(s), lt = strlen(t); // 把 strlen(字符串), lt 赋值为 strlen(另一字符串); 写入 size_t ls
    if (ls != lt)
        return 0;       // 若 ls 不等于 lt，直接返回 0
    int cnt[256] = {0}; // 把 {0}; 写入 int cnt[256]
    for (size_t i = 0; i < ls; i++)
        cnt[(unsigned char)s[i]]++; // 让 下标 i 从 0 开始计数，下标 i 小于 ls 就继续
    for (size_t i = 0; i < lt; i++)
        cnt[(unsigned char)t[i]]--; // 让 下标 i 从 0 开始计数，下标 i 小于 lt 就继续
    for (int i = 0; i < 256; i++)
        if (cnt[i] != 0)
            return 0; // 让 下标 i 从 0 开始计数，下标 i 小于 256 就继续
    return 1;         // 返回 1
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (!is_anagram("anagram", "nagaram")) {
        printf("FAIL 1\n");
        return 1;
    }
    if (is_anagram("rat", "car")) {
        printf("FAIL 2\n");
        return 1;
    }                 // 若 is_anagram(「rat」, 「rat」)) { 输出「rat」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
