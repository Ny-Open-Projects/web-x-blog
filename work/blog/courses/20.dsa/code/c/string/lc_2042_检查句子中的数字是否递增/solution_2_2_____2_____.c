/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138481618 */
/* LeetCode 2042. 检查句子中的数字是否递增 — C 版（方案2） */
#include <ctype.h>                                    // 引入头文件
#include <stdio.h>                                    // 引入头文件
#include <stdlib.h>                                   // 引入头文件
#include <string.h>                                   // 引入头文件
static int are_numbers_ascending(const char *s) {     // 定义函数/方法 are_numbers_ascending
    long prev = -1;                                   // 把 减 1; 写入 long prev
    char tok[256];                                    // char tok[256];
    int ti = 0;                                       // 把 0 存入 ti
    const char *p = s;                                // 把 字符串; 写入 const char *p
    while (1) {                                       // 循环，直到不满足「1」
        if (*p == ' ' || *p == '\0') {                // 若 乘 节点 等于 ' ' 或 乘 节点 等于 '\0'
            if (ti > 0) {                             // 若 ti 超过 0
                tok[ti] = '\0';                       // 把 '\0'; 写入 tok[ti]
                if (isdigit((unsigned char)tok[0])) { // 若 isdigit((unsigned char)tok[0]
                    long num = atol(tok);             // 把 atol(tok); 写入 long num
                    if (num <= prev)
                        return 0; // 若 num 不超过 前一个，直接返回 0
                    prev = num;   // 把 num; 写入 前一个
                }
                ti = 0; // 把 0; 写入 ti
            }
            if (*p == '\0')
                break;         // 若 乘 节点 等于 '\0') break;
        } else if (ti < 255) { // 否则，若 ti 小于 255
            tok[ti++] = *p;    // 把 乘 节点; 写入 tok[ti++]
        }
        p++; // 节点 加一
    }
    return 1; // 返回 1
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (!are_numbers_ascending("1 box has 3 blue 4 red 6 green and 12 yellow marbles")) {
        printf("FAIL 1\n");
        return 1;
    }
    if (are_numbers_ascending("hello world 5 x 5")) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
