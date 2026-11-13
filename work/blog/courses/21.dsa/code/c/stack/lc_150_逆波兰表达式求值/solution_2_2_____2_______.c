/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130726302 */
/* LeetCode 150. 逆波兰表达式求值 — C 版（方案2） */
#include <stdio.h>                                 // 引入头文件
#include <stdlib.h>                                // 引入头文件
#include <string.h>                                // 引入头文件
static long eval_rpn(const char **tokens, int n) { // 定义函数/方法 eval_rpn
    long st[4096];                                 // long st[4096];
    int top = 0;                                   // 把 0 存入 top
    for (int i = 0; i < n; i++) {  // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        const char *t = tokens[i]; // 把 tokens[下标 i]; 写入 const char *t
        if (strcmp(t, "+") == 0 || strcmp(t, "-") == 0 || strcmp(t, "*") == 0 || strcmp(t, "/") == 0) {
            long b = st[--top]; // 把 st[ 减一 top]; 写入 long b
            long a = st[--top]; // 把 st[ 减一 top]; 写入 long a
            long r = 0;         // 把 0; 写入 long r
            if (t[0] == '+')
                r = a + b; // 若 另一字符串[0] 等于 ' 加 ') 右指针 赋值为 数组 加 b;
            else if (t[0] == '-')
                r = a - b; // 否则，若 另一字符串[0] 等于 ' 减 ') 右指针 赋值为 数组 减 b;
            else if (t[0] == '*')
                r = a * b; // 否则，若 另一字符串[0] 等于 ' 乘 ') 右指针 赋值为 数组 乘 b;
            else
                r = a / b;       // 否则
            st[top++] = r;       // 把 右指针; 写入 st[top++]
        } else {                 // 否则
            st[top++] = atol(t); // 把 atol(另一字符串); 写入 st[top++]
        }
    }
    return st[0]; // 返回 st[0]
}
int main(void) {                                  // 程序入口：跑内嵌自测用例
    const char *t1[] = {"2", "1", "+", "3", "*"}; // 把 {「2」,「2」,「2」,「2」,「2」}; 写入 const char *t1[]
    const char *t2[] = {"4", "13", "5", "/",
                        "+"}; // 把 {「4」,「4」,「4」,「4」,「4」}; 写入 const char *t2[]
    const char *t3[] = {"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"};
    if (eval_rpn(t1, 5) != 9) {
        printf("FAIL 1\n");
        return 1;
    } // 若 eval_rpn(t1, 5) 不等于 9) { 输出「FAIL 1 」); return 1; }
    if (eval_rpn(t2, 5) != 6) {
        printf("FAIL 2\n");
        return 1;
    } // 若 eval_rpn(t2, 5) 不等于 6) { 输出「FAIL 2 」); return 1; }
    if (eval_rpn(t3, 13) != 22) {
        printf("FAIL 3\n");
        return 1;
    } // 若 eval_rpn(t3, 13) 不等于 22) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS