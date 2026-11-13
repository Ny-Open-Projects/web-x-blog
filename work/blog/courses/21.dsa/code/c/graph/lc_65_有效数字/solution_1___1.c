/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
 * LeetCode 65. 有效数字 — C 版 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

static int is_space(char c) { // 定义判定函数 is_space
    return c == ' ' || c == '\t' || c == '\n' || c == '\r' || c == '\f' ||
           c == '\v'; // 把 赋值为 '\值'; 写入 字符
}

/* 方案1（线性扫描） */
static int is_number(const char *s) { // 定义判定函数 is_number
    /* trim 首尾空白，等价于 TS 的 String.trim() */
    while (is_space(*s))
        s++;                // 循环，直到不满足「is_space( 乘 字符串)) 字符串 加一 ;」
    size_t len = strlen(s); // 把 strlen(字符串); 写入 size_t len
    while (len > 0 && is_space(s[len - 1]))
        len--; // 循环，直到不满足「长度 超过 0 且 is_space(字符串[长度 减 1])) 长度 减一 ;」
    if (len == 0)
        return 0;                              // 若 长度 等于 0，直接返回 0
    int has_dot = 0, has_e = 0, has_digit = 0; // 把 0, has_e 赋值为 0, has_digit 赋值为 0 存入 has_dot
    for (size_t i = 0; i < len; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
        char c = s[i];                 // 把 字符串[下标 i]; 写入 char c
        if (c == '.') {                // 若 字符 等于 '.'
            if (has_dot || has_e)
                return 0;                  // 若 has_dot 或 has_e，直接返回 0
            has_dot = 1;                   // 把 1; 写入 has_dot
        } else if (c == 'e' || c == 'E') { // 否则，若 字符 等于 'e' 或 字符 等于 'E'
            if (has_e || !has_digit)
                return 0;                  // 若 has_e 或 取反 has_digit，直接返回 0
            has_e = 1;                     // 把 1; 写入 has_e
            has_digit = 0;                 // 把 0; 写入 has_digit
        } else if (c == '+' || c == '-') { // 否则，若 字符 等于 ' 加 ' 或 字符 等于 ' 减 '
            if (i > 0 && s[i - 1] != 'e' && s[i - 1] != 'E')
                return 0;
        } else if (c >= '0' && c <= '9') { // 否则，若 字符 不低于 '0' 且 字符 不超过 '9'
            has_digit = 1;                 // 把 1; 写入 has_digit
        } else {                           // 否则
            return 0;                      // 返回 0
        }
    }
    return has_digit; // 返回 has_digit
}

int main(void) {                                     // 程序入口：跑内嵌自测用例
    if (is_number("abc") != 0) {                     // 若 is_number(「abc」) 不等于 0
        printf("isNumber('abc') should be false\n"); // 打印输出
        return 1;                                    // 返回 1
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
