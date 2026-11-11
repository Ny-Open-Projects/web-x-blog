/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案11：Rule 循环游标）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

typedef struct {   // typedef struct {
    char data[16]; // char data[16];
    int idx;       // int idx;
    int length;    // int 长度;
} Rule;            // } Rule;

static void rule_init(Rule *r, const char *s) { // 定义函数/方法 rule_init
    strcpy(r->data, s);                         // strcpy(右指针 减 超过 data, 字符串);
    r->idx = 0;                                 // 把 0; 写入 r->idx
    r->length = (int)strlen(s);                 // 把 (int)strlen(字符串); 写入 r->length
}

static char rule_next(Rule *r) { // 定义函数/方法 rule_next
    char ch = r->data[r->idx];   // 把 右指针 减 超过 data[右指针 减 超过 idx]; 写入 char ch
    r->idx =
        (r->idx + 1) % r->length; // 把 (右指针 减 超过 idx 加 1) 对…取模 右指针 减 超过 长度; 写入 r->idx
    return ch;                    // 返回 字符
}

static char rule_peek(const Rule *r) { // 定义函数/方法 rule_peek
    return r->data[r->idx];            // 返回 右指针 减 超过 data[右指针 减 超过 idx]
}

int main(void) {                          // 程序入口：跑内嵌自测用例
    Rule r;                               // Rule 右指针;
    rule_init(&r, "ESVM");                // rule_init( 按位与 右指针, 「ESVM」);
    char s1[16] = "";                     // 把 「」; 写入 char s1[16]
    for (int i = 0; i < 10; i++) {        // 让 下标 i 从 0 开始计数，下标 i 小于 10 就继续
        char buf[2] = {rule_next(&r), 0}; // 把 { rule_next( 按位与 右指针), 0 }; 写入 char buf[2]
        strcat(s1, buf);                  // 打印输出
    }
    Rule r2;                               // Rule r2;
    rule_init(&r2, "semv");                // rule_init( 按位与 r2, 「semv」);
    char s2[16] = "";                      // 把 「」; 写入 char s2[16]
    for (int i = 0; i < 6; i++) {          // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
        char buf[2] = {rule_next(&r2), 0}; // 把 { rule_next( 按位与 r2), 0 }; 写入 char buf[2]
        strcat(s2, buf);                   // 打印输出
    }
    if (strcmp(s1, "ESVMESVMES") != 0) {
        printf("rule1 failed\n");
        return 1;
    }
    if (strcmp(s2, "semvse") != 0) {
        printf("rule2 failed\n");
        return 1;
    }                 // 若 strcmp(s2, 「semvse」) 不等于 0) { 输出「semvse」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
