/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130778527 */
/* LeetCode 125. 验证回文串 — C 版（方案3） */
#include <ctype.h>                        // 引入头文件
#include <stdio.h>                        // 引入头文件
#include <string.h>                       // 引入头文件
static int is_palindrome(const char *s) { // 定义判定函数 is_palindrome
    char f[8192];                         // char f[8192];
    int n = 0;                            // 把 0 存入 元素个数
    for (const char *p = s; *p; p++) { // 把 字符串; 乘 节点; 节点 加一 ) { 写入 for (const char *p
        if (isalnum((unsigned char)*p))
            f[n++] = tolower((unsigned char)*p);
    }
    int i = 0, j = n - 1; // 把 0, 下标 j 赋值为 元素个数 减 1 存入 下标 i
    while (i < j) {       // 循环，直到不满足「下标 i 小于 下标 j」
        if (f[i] != f[j])
            return 0; // 若 f[下标 i] 不等于 f[下标 j]，直接返回 0
        i++;
        j--; // 下标 i 加一 ; 下标 j 减一 ;
    }
    return 1; // 返回 1
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (!is_palindrome("A man, a plan, a canal: Panama")) {
        printf("FAIL 1\n");
        return 1;
    }
    if (is_palindrome("race a car")) {
        printf("FAIL 2\n");
        return 1;
    }
    if (!is_palindrome(" ")) {
        printf("FAIL 3\n");
        return 1;
    }                 // 若 取反 is_palindrome(「 」)) { 输出「 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
