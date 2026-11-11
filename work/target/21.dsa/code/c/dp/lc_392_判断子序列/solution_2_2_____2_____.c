/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130753613 */
/* LeetCode 392. 判断子序列 — C 版（方案2） */
#include <stdio.h>                                        // 引入头文件
#include <string.h>                                       // 引入头文件
static int is_subsequence(const char *s, const char *t) { // 定义判定函数 is_subsequence
    int i = 0;                                            // 把 0 存入 下标 i
    for (const char *p = t; *p; p++) { // 把 另一字符串; 乘 节点; 节点 加一 ) { 写入 for (const char *p
        if (s[i] && s[i] == *p)
            i++; // 若 字符串[下标 i] 且 字符串[下标 i] 等于 乘 节点) 下标 i 加一 ;
    }
    return s[i] == '\0'; // 返回 字符串[下标 i] 等于 '\0'
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (!is_subsequence("abc", "ahbgdc")) {
        printf("FAIL 1\n");
        return 1;
    } // 若 取反 is_subsequence(「abc」, 「abc」)) { 输出「abc」); return 1; }
    if (is_subsequence("axc", "ahbgdc")) {
        printf("FAIL 2\n");
        return 1;
    } // 若 is_subsequence(「axc」, 「axc」)) { 输出「axc」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS