/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114011 */
/* LeetCode 232. 用栈实现队列 — C 版（方案1） */
#include <stdio.h> // 引入头文件
typedef struct {
    int in_[4096];
    int in_n;
    int out_[4096];
    int out_n;
} MyQueue;
static void mq_init(MyQueue *q) {
    q->in_n = 0;
    q->out_n = 0;
}
static void mq_in2out(MyQueue *q) { // 定义函数/方法 mq_in2out
    while (q->in_n > 0)
        q->out_[q->out_n++] = q->in_[--q->in_n];
}
static void mq_push(MyQueue *q, int x) { q->in_[q->in_n++] = x; }
static int mq_pop(MyQueue *q) { // 定义函数/方法 mq_pop
    if (q->out_n == 0)
        mq_in2out(q);           // 若 节点 减 超过 out_n 等于 0) mq_in2out(节点);
    return q->out_[--q->out_n]; // 返回 节点 减 超过 out_[ 减一 节点 减 超过 out_n]
}
static int mq_peek(MyQueue *q) { // 定义函数/方法 mq_peek
    if (q->out_n == 0)
        mq_in2out(q);             // 若 节点 减 超过 out_n 等于 0) mq_in2out(节点);
    return q->out_[q->out_n - 1]; // 返回 节点 减 超过 out_[节点 减 超过 out_n 减 1]
}
static int mq_empty(MyQueue *q) { return q->in_n == 0 && q->out_n == 0; }
int main(void) { // 程序入口：跑内嵌自测用例
    MyQueue q;   // MyQueue 节点;
    mq_init(&q); // mq_init( 按位与 节点);
    mq_push(&q, 1);
    mq_push(&q, 2); // mq_push( 按位与 节点, 1); mq_push( 按位与 节点, 2);
    if (mq_peek(&q) != 1) {
        printf("FAIL 1\n");
        return 1;
    } // 若 mq_peek( 按位与 节点) 不等于 1) { 输出「FAIL 1 」); return 1; }
    if (mq_pop(&q) != 1) {
        printf("FAIL 2\n");
        return 1;
    } // 若 mq_pop( 按位与 节点) 不等于 1) { 输出「FAIL 2 」); return 1; }
    if (mq_empty(&q)) {
        printf("FAIL 3\n");
        return 1;
    } // 若 mq_empty( 按位与 节点)) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS