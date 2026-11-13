/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
 * LeetCode 65. 有效数字 — C 版 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

/* 方案7（确定有限状态自动机 DFA，其余字符 lowercase）
 * 字符类：0=blank 1=sign 2='.' 3=digit 4='e' 5=other（转移表中 -1 表示无转移）
 * 与 TS 的 graph 一致；非数字/空白/符号字符统一 lowercase，'E' 归并为 'e' */
enum { CLS_BLANK, CLS_SIGN, CLS_DOT, CLS_DIGIT, CLS_E, CLS_OTHER, CLS_N };

static const int TRANS[8][CLS_N] = {
    // 把 { 写入 static const int TRANS[8][CLS_N]
    /*        blank sign  dot  digit  e  other */
    /* 0 */ {0, 1, 2, 6, -1, -1},
    /* 1 */ {-1, -1, 2, 6, -1, -1},
    /* 2 */ {-1, -1, -1, 3, -1, -1},
    /* 3 */ {-1, -1, -1, 3, 4, -1},
    /* 4 */ {-1, 7, -1, 5, -1, -1},
    /* 5 */ {-1, -1, -1, 5, -1, -1},
    /* 6 */ {-1, -1, 3, 6, 4, -1},
    /* 7 */ {-1, -1, -1, 5, -1, -1},
};

static int is_space(char c) { // 定义判定函数 is_space
    return c == ' ' || c == '\t' || c == '\n' || c == '\r' || c == '\f' ||
           c == '\v'; // 把 赋值为 '\值'; 写入 字符
}

static int is_number(const char *s) { // 定义判定函数 is_number
    /* trim 首尾空白，等价于 TS 的 String.trim() */
    while (is_space(*s))
        s++;                // 循环，直到不满足「is_space( 乘 字符串)) 字符串 加一 ;」
    size_t len = strlen(s); // 把 strlen(字符串); 写入 size_t len
    while (len > 0 && is_space(s[len - 1]))
        len--; // 循环，直到不满足「长度 超过 0 且 is_space(字符串[长度 减 1])) 长度 减一 ;」
    int state = 0;                     // 把 0 存入 state
    for (size_t i = 0; i < len; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
        char ch = s[i];                // 把 字符串[下标 i]; 写入 char ch
        if (ch >= 'A' && ch <= 'Z')
            ch = ch - 'A' + 'a';         /* lowercase */
        int cls;                         // int cls;
        if (ch >= '0' && ch <= '9')      // 若 字符 不低于 '0' 且 字符 不超过 '9'
            cls = CLS_DIGIT;             // 把 CLS_DIGIT; 写入 cls
        else if (ch == ' ')              // 定义函数/方法 if
            cls = CLS_BLANK;             // 把 CLS_BLANK; 写入 cls
        else if (ch == '+' || ch == '-') // 定义函数/方法 if
            cls = CLS_SIGN;              // 把 CLS_SIGN; 写入 cls
        else if (ch == '.')              // 定义函数/方法 if
            cls = CLS_DOT;               // 把 CLS_DOT; 写入 cls
        else if (ch == 'e')              // 定义函数/方法 if
            cls = CLS_E;                 // 把 CLS_E; 写入 cls
        else                             // 否则
            cls = CLS_OTHER;             // 把 CLS_OTHER; 写入 cls
        int ns = TRANS[state][cls];      // 把 TRANS[state][cls] 存入 ns
        if (ns < 0)
            return 0; // 若 ns 小于 0，直接返回 0
        state = ns;   // 把 ns; 写入 state
    }
    return state == 3 || state == 5 || state == 6; // 返回 state 等于 3 或 state 等于 5 或 state 等于 6
}

int main(void) {                                  // 程序入口：跑内嵌自测用例
    if (is_number("0") != 1) {                    // 若 is_number(「0」) 不等于 1
        printf("isNumber('0') should be true\n"); // 打印输出
        return 1;                                 // 返回 1
    }
    if (is_number("abc") != 0) {                     // 若 is_number(「abc」) 不等于 0
        printf("isNumber('abc') should be false\n"); // 打印输出
        return 1;                                    // 返回 1
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
