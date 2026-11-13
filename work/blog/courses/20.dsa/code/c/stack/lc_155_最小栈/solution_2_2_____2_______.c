/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245934 */
/* LeetCode 155. 最小栈 — C 版（方案2） */
#include <stdio.h> // 引入头文件
typedef struct {
    int vals[4096];
    int mins[4096];
    int top;
} MinStack;
static void ms_init(MinStack *s) { s->top = 0; } // 把 0; } 写入 static void ms_init(MinStack *s) { s->top
static void ms_push(MinStack *s, int v) {        // 定义函数/方法 ms_push
    s->vals[s->top] = v;                         // 把 值; 写入 s->vals[s->top]
    s->mins[s->top] = s->top > 0 && s->mins[s->top - 1] < v ? s->mins[s->top - 1] : v;
    s->top++; // 字符串 减 超过 top 加一 ;
}
static void ms_pop(MinStack *s) {
    s->top--;
} // static void ms_pop(MinStack 乘 字符串) { 字符串 减 超过 top 减一 ; }
static int ms_top(MinStack *s) { return s->vals[s->top - 1]; }
static int ms_get_min(MinStack *s) { return s->mins[s->top - 1]; }
int main(void) { // 程序入口：跑内嵌自测用例
    MinStack s;  // MinStack 字符串;
    ms_init(&s); // ms_init( 按位与 字符串);
    ms_push(&s, -2);
    ms_push(&s, 0);
    ms_push(&s, -3);
    if (ms_get_min(&s) != -3) {
        printf("FAIL 1\n");
        return 1;
    }           // 若 ms_get_min( 按位与 字符串) 不等于 减 3) { 输出「FAIL 1 」); return 1; }
    ms_pop(&s); // ms_pop( 按位与 字符串);
    if (ms_top(&s) != 0) {
        printf("FAIL 2\n");
        return 1;
    } // 若 ms_top( 按位与 字符串) 不等于 0) { 输出「FAIL 2 」); return 1; }
    if (ms_get_min(&s) != -2) {
        printf("FAIL 3\n");
        return 1;
    } // 若 ms_get_min( 按位与 字符串) 不等于 减 2) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS