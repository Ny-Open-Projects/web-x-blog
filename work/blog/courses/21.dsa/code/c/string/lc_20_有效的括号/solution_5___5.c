/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133759617 */
/* LeetCode 20. 有效的括号 — C 版（方案5） */
#include <stdio.h>                     // 引入头文件
#include <string.h>                    // 引入头文件
static int is_valid(const char *s) {   // 定义判定函数 is_valid
    char stack[8192];                  // char 栈[8192];
    int top = 0;                       // 把 0 存入 top
    for (const char *p = s; *p; p++) { // 把 字符串; 乘 节点; 节点 加一 ) { 写入 for (const char *p
        if (*p == ')') {               // 若 乘 节点 等于 ')'
            if (top == 0 || stack[--top] != '(')
                return 0;       // 若 top 等于 0 或 栈[ 减一 top] 不等于 '('，直接返回 0
        } else if (*p == ']') { // 否则，若 乘 节点 等于 ']'
            if (top == 0 || stack[--top] != '[')
                return 0;       // 若 top 等于 0 或 栈[ 减一 top] 不等于 '['，直接返回 0
        } else if (*p == '}') { // 否则，若 乘 节点 等于 '}'
            if (top == 0 || stack[--top] != '{')
                return 0;      // 若 top 等于 0 或 栈[ 减一 top] 不等于 '{'，直接返回 0
        } else {               // 否则
            stack[top++] = *p; // 把 乘 节点; 写入 stack[top++]
        }
    }
    return top == 0; // 返回 top 等于 0
}
int main(void) { // 程序入口：跑内嵌自测用例
    const char *tests[] = {
        "(",  "()",   "()[]{}",
        "(]", "([)]", "abc"}; // 把 {「(」, 「(」, 「(」, 「(」, 「(」, 「(」}; 写入 const char *tests[]
    const int want[] = {0, 1, 1, 0, 0, 0}; // 把 {0, 1, 1, 0, 0, 0}; 写入 const int want[]
    for (int i = 0; i < 6; i++) {          // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
        if (is_valid(tests[i]) != want[i]) {
            printf("FAIL %d\n", i);
            return 1;
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
