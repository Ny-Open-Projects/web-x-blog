/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134135902 */
/* LeetCode 344. 反转字符串 — C 版（方案2） */
#include <stdio.h>                     // 引入头文件
#include <string.h>                    // 引入头文件
static void reverse_string(char s[]) { // 定义函数/方法 reverse_string
    int n = (int)strlen(s);            // 把 (int)strlen(字符串) 存入 元素个数
    for (int i = 0, j = n - 1; i < j; i++, j--) {
        char t = s[i];
        s[i] = s[j];
        s[j] = t;
    } // 让 下标 i 从 0, 下标 j 赋值为 元素个数 减 1 开始计数，下标 i 小于 下标 j 就继续
}
int main(void) { // 程序入口：跑内嵌自测用例
    char b[64];  // char b[64];
    strcpy(b, "hello");
    reverse_string(b); // strcpy(b, 「hello」); reverse_string(b);
    if (strcmp(b, "olleh") != 0) {
        printf("FAIL 1\n");
        return 1;
    } // 若 strcmp(b, 「olleh」) 不等于 0) { 输出「olleh」); return 1; }
    strcpy(b, "Hannah");
    reverse_string(b); // strcpy(b, 「Hannah」); reverse_string(b);
    if (strcmp(b, "hannaH") != 0) {
        printf("FAIL 2\n");
        return 1;
    } // 若 strcmp(b, 「hannaH」) 不等于 0) { 输出「hannaH」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS