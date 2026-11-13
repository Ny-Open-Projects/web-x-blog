/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130668538 */
/* LeetCode 58. 最后一个单词的长度 — C 版（方案1） */
#include <stdio.h>                              // 引入头文件
#include <string.h>                             // 引入头文件
static int length_of_last_word(const char *s) { // 定义函数/方法 length_of_last_word
    int n = (int)strlen(s);                     // 把 (int)strlen(字符串) 存入 元素个数
    int end = n - 1;                            // 把 元素个数 减 1 存入 终点
    while (end >= 0 && s[end] == ' ')
        end--; // 循环，直到不满足「终点 不低于 0 且 字符串[终点] 等于 ' ') 终点 减一 ;」
    if (end < 0)
        return 0;    // 若 终点 小于 0，直接返回 0
    int start = end; // 把 终点 存入 起点
    while (start >= 0 && s[start] != ' ')
        start--; // 循环，直到不满足「起点 不低于 0 且 字符串[起点] 不等于 ' ') 起点 减一 ;」
    return end - start; // 返回 终点 减 起点
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (length_of_last_word("Hello World") != 5) {
        printf("FAIL 1\n");
        return 1;
    }
    if (length_of_last_word(" ") != 0) {
        printf("FAIL 2\n");
        return 1;
    } // 若 length_of_last_word(「 」) 不等于 0) { 输出「 」); return 1; }
    if (length_of_last_word("a") != 1) {
        printf("FAIL 3\n");
        return 1;
    } // 若 length_of_last_word(「数组」) 不等于 1) { 输出「数组」); return 1; }
    if (length_of_last_word(" fly me to the moon ") != 4) {
        printf("FAIL 4\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
