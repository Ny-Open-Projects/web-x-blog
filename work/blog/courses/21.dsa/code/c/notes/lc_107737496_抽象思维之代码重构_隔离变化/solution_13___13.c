/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案13：微型正则匹配 match/matchhere/matchstar）
 */
#include <stdbool.h> // 引入头文件
#include <stdio.h>   // 引入头文件

static bool matchhere(const char *re,
                      const char *text); // static bool matchhere(const char 乘 re, const char 乘 text);

static bool matchstar(char c, const char *re, const char *text) { // 定义函数/方法 matchstar
    const char *t = text;                                         // 把 text; 写入 const char *t
    while (true) {                                                // 循环，直到不满足「true」
        if (matchhere(re, t))
            return true; // 若 matchhere(re, 另一字符串)，直接返回 true
        if (*t == 0)
            break; // 若 乘 另一字符串 等于 0) break;
        if (*t != c && c != '.')
            break; // 若 乘 另一字符串 不等于 字符 且 字符 不等于 '.') break;
        t++;       // 另一字符串 加一
    }
    return false; // 返回 false
}

static bool matchhere(const char *re, const char *text) { // 定义函数/方法 matchhere
    if (*re == 0)
        return true; // 若 乘 re 等于 0，直接返回 true
    if (re[1] == '*')
        return matchstar(re[0], re + 2,
                         text); // 若 re[1] 等于 ' 乘 '，直接返回 matchstar(re[0], re 加 2, text)
    if (re[0] == '$' && re[1] == 0)
        return *text == 0; // 若 re[0] 等于 '$' 且 re[1] 等于 0，直接返回 乘 text 等于 0
    if (*text != 0 && (re[0] == '.' || re[0] == *text))
        return matchhere(re + 1, text + 1);
    return false; // 返回 false
}

static bool match(const char *re, const char *text) { // 定义函数/方法 match
    if (*re == '^')
        return matchhere(re + 1, text); // 若 乘 re 等于 ' 按位异或 '，直接返回 matchhere(re 加 1, text)
    const char *t = text;               // 把 text; 写入 const char *t
    while (true) {                      // 循环，直到不满足「true」
        if (matchhere(re, t))
            return true; // 若 matchhere(re, 另一字符串)，直接返回 true
        if (*t == 0)
            break; // 若 乘 另一字符串 等于 0) break;
        t++;       // 另一字符串 加一
    }
    return false; // 返回 false
}

int main(void) { // 程序入口：跑内嵌自测用例
    if (!match("abc", "xxabcxx")) {
        printf("m1 failed\n");
        return 1;
    } // 若 取反 match(「abc」, 「abc」)) { 输出「abc」); return 1; }
    if (!match("a.c", "axc")) {
        printf("m2 failed\n");
        return 1;
    } // 若 取反 match(「数组.字符」, 「数组.字符」)) { 输出「数组.字符」); return 1; }
    if (!match("a*", "aaaa")) {
        printf("m3 failed\n");
        return 1;
    } // 若 取反 match(「数组 乘 」, 「数组 乘 」)) { 输出「数组 乘 」); return 1; }
    if (match("^a", "ba")) {
        printf("m4 failed\n");
        return 1;
    }
    if (!match("c$", "abc")) {
        printf("m5 failed\n");
        return 1;
    } // 若 取反 match(「字符$」, 「字符$」)) { 输出「字符$」); return 1; }
    if (!match("a.*c", "aXYZc")) {
        printf("m6 failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
