/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135129920 */
/* LeetCode 8. 字符串转换整数 (atoi) — C 版（方案1） */
#include <ctype.h>                  // 引入头文件
#include <limits.h>                 // 引入头文件
#include <stdio.h>                  // 引入头文件
#include <string.h>                 // 引入头文件
static int my_atoi(const char *s) { // 定义函数/方法 my_atoi
    int i = 0, n = (int)strlen(s);  // 把 0, 元素个数 赋值为 (int)strlen(字符串) 存入 下标 i
    while (i < n && s[i] == ' ')
        i++; // 循环，直到不满足「下标 i 小于 元素个数 且 字符串[下标 i] 等于 ' ') 下标 i 加一 ;」
    int sign = 1; // 把 1 存入 sign
    if (i < n &&
        (s[i] == '+' ||
         s[i] ==
             '-')) { // 若 下标 i 小于 元素个数 且 (字符串[下标 i] 等于 ' 加 ' 或 字符串[下标 i] 等于 ' 减 '
        if (s[i] == '-')
            sign = -1; // 若 字符串[下标 i] 等于 ' 减 ') sign 赋值为 减 1;
        i++;           // 下标 i 加一
    }
    long ans = 0;                                   // 把 0; 写入 long ans
    while (i < n && isdigit((unsigned char)s[i])) { // 循环，直到不满足「下标 i 小于 元素个数 且
                                                    // isdigit((unsigned char)字符串[下标 i]」
        ans = ans * 10 + (s[i] - '0'); // 把 答案 乘 10 加 (字符串[下标 i] 减 '0'); 写入 答案
        if (ans > 2147483648L)
            ans = 2147483648L; // 若 答案 超过 2147483648L) 答案 赋值为 2147483648L;
        i++;                   // 下标 i 加一
    }
    ans *= sign; // 把 sign; 写入 ans *
    if (ans > INT_MAX)
        return INT_MAX; // 若 答案 超过 INT_MAX，直接返回 INT_MAX
    if (ans < INT_MIN)
        return INT_MIN; // 若 答案 小于 INT_MIN，直接返回 INT_MIN
    return (int)ans;    // 返回 (int)答案
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (my_atoi("42") != 42) {
        printf("FAIL 1\n");
        return 1;
    } // 若 my_atoi(「42」) 不等于 42) { 输出「42」); return 1; }
    if (my_atoi(" -42") != -42) {
        printf("FAIL 2\n");
        return 1;
    } // 若 my_atoi(「 减 42」) 不等于 减 42) { 输出「 减 42」); return 1; }
    if (my_atoi("4193 with words") != 4193) {
        printf("FAIL 3\n");
        return 1;
    }
    if (my_atoi("-91283472332") != INT_MIN) {
        printf("FAIL 4\n");
        return 1;
    }
    if (my_atoi("words and 987") != 0) {
        printf("FAIL 5\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
