/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145198996 */
/* LeetCode 225. 用队列实现栈 — C 版（方案2） */
#include <stdio.h> // 引入头文件
typedef struct {
    int q[4096];
    int head, tail;
} MyStack; // typedef struct { int 节点[4096]; int 头节点, 尾节点; } MyStack;
static void ms_init(MyStack *s) {
    s->head = 0;
    s->tail = 0;
}
static void ms_push(MyStack *s, int x) { s->q[s->head++] = x; }
static int ms_pop(MyStack *s) { return s->q[--s->head]; }
static int ms_top(MyStack *s) { return s->q[s->head - 1]; }
static int ms_empty(MyStack *s) { return s->head == s->tail; }
int main(void) { // 程序入口：跑内嵌自测用例
    MyStack s;   // MyStack 字符串;
    ms_init(&s); // ms_init( 按位与 字符串);
    ms_push(&s, 1);
    ms_push(&s, 2); // ms_push( 按位与 字符串, 1); ms_push( 按位与 字符串, 2);
    if (ms_top(&s) != 2) {
        printf("FAIL 1\n");
        return 1;
    } // 若 ms_top( 按位与 字符串) 不等于 2) { 输出「FAIL 1 」); return 1; }
    if (ms_pop(&s) != 2) {
        printf("FAIL 2\n");
        return 1;
    } // 若 ms_pop( 按位与 字符串) 不等于 2) { 输出「FAIL 2 」); return 1; }
    if (ms_empty(&s)) {
        printf("FAIL 3\n");
        return 1;
    } // 若 ms_empty( 按位与 字符串)) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS