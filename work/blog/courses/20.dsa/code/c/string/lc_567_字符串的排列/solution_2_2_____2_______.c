/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135917076 */
/* LeetCode 567. 字符串的排列 — C 版（方案2） */
#include <stdio.h>                                    // 引入头文件
#include <string.h>                                   // 引入头文件
static int cnt_eq(const int a[26], const int b[26]) { // 定义函数/方法 cnt_eq
    for (int i = 0; i < 26; i++)
        if (a[i] != b[i])
            return 0; // 让 下标 i 从 0 开始计数，下标 i 小于 26 就继续
    return 1;         // 返回 1
}
static int check_inclusion(const char *s1, const char *s2) { // 定义判定函数 check_inclusion
    int m = (int)strlen(s1),
        n = (int)strlen(s2); // 把 (int)strlen(s1), 元素个数 赋值为 (int)strlen(s2) 存入 映射表
    if (m > n)
        return 0;                     // 若 映射表 超过 元素个数，直接返回 0
    int s1c[26] = {0}, s2c[26] = {0}; // 把 {0}, s2c[26] 赋值为 {0}; 写入 int s1c[26]
    for (int i = 0; i < m; i++) {     // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
        s1c[s1[i] - 'a']++;           // s1c[s1[下标 i] 减 '数组'] 加一 ;
        s2c[s2[i] - 'a']++;           // s2c[s2[下标 i] 减 '数组'] 加一 ;
    }
    if (cnt_eq(s1c, s2c))
        return 1;                 // 若 cnt_eq(s1c, s2c)，直接返回 1
    for (int i = m; i < n; i++) { // 让 下标 i 从 映射表 开始计数，下标 i 小于 元素个数 就继续
        s2c[s2[i] - 'a']++;     // s2c[s2[下标 i] 减 '数组'] 加一 ;
        s2c[s2[i - m] - 'a']--; // s2c[s2[下标 i 减 映射表] 减 '数组'] 减一 ;
        if (cnt_eq(s1c, s2c))
            return 1; // 若 cnt_eq(s1c, s2c)，直接返回 1
    }
    return 0; // 返回 0
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (!check_inclusion("ab", "eidbaooo")) {
        printf("FAIL 1\n");
        return 1;
    } // 若 取反 check_inclusion(「ab」, 「ab」)) { 输出「ab」); return 1; }
    if (check_inclusion("ab", "eidboaoo")) {
        printf("FAIL 2\n");
        return 1;
    }                 // 若 check_inclusion(「ab」, 「ab」)) { 输出「ab」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
