/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145361774 */
/* LeetCode 641. 设计循环双端队列 — C 版（方案1） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
typedef struct {
    int *data;
    int head, tail, cap, size;
} MyCircularDeque;
static MyCircularDeque *cdq_new(int k) { // static MyCircularDeque 乘 cdq_new(int 下标 k) {
    MyCircularDeque *d =
        malloc(sizeof(MyCircularDeque)); // 把 malloc(sizeof(MyCircularDeque)); 写入 MyCircularDeque *d
    d->cap = k;                          // 把 下标 k; 写入 d->cap
    d->data = malloc(sizeof(int) * k);   // 把 malloc(sizeof(int) 乘 下标 k); 写入 d->data
    d->head = 0;
    d->tail = 0;
    d->size = 0; // 把 0; d 减 超过 尾节点 赋值为 0; d 减 超过 大小 赋值为 0; 写入 d->head
    return d;    // 返回 d
}
static int cdq_insert_front(MyCircularDeque *d, int v) { // 定义函数/方法 cdq_insert_front
    if (d->size == d->cap)
        return 0; // 若 d 减 超过 大小 等于 d 减 超过 cap，直接返回 0
    d->head = (d->head + d->cap - 1) %
              d->cap; // 把 (d 减 超过 头节点 加 d 减 超过 cap 减 1) 对…取模 d 减 超过 cap; 写入 d->head
    d->data[d->head] = v; // 把 值; 写入 d->data[d->head]
    d->size++;            // d 减 超过 大小 加一 ;
    return 1;             // 返回 1
}
static int cdq_insert_last(MyCircularDeque *d, int v) { // 定义函数/方法 cdq_insert_last
    if (d->size == d->cap)
        return 0;                     // 若 d 减 超过 大小 等于 d 减 超过 cap，直接返回 0
    d->data[d->tail] = v;             // 把 值; 写入 d->data[d->tail]
    d->tail = (d->tail + 1) % d->cap; // 把 (d 减 超过 尾节点 加 1) 对…取模 d 减 超过 cap; 写入 d->tail
    d->size++;                        // d 减 超过 大小 加一 ;
    return 1;                         // 返回 1
}
static int cdq_delete_front(MyCircularDeque *d) { // 定义函数/方法 cdq_delete_front
    if (d->size == 0)
        return 0;                     // 若 d 减 超过 大小 等于 0，直接返回 0
    d->head = (d->head + 1) % d->cap; // 把 (d 减 超过 头节点 加 1) 对…取模 d 减 超过 cap; 写入 d->head
    d->size--;                        // d 减 超过 大小 减一 ;
    return 1;                         // 返回 1
}
static int cdq_delete_last(MyCircularDeque *d) { // 定义函数/方法 cdq_delete_last
    if (d->size == 0)
        return 0; // 若 d 减 超过 大小 等于 0，直接返回 0
    d->tail = (d->tail + d->cap - 1) %
              d->cap; // 把 (d 减 超过 尾节点 加 d 减 超过 cap 减 1) 对…取模 d 减 超过 cap; 写入 d->tail
    d->size--; // d 减 超过 大小 减一 ;
    return 1;  // 返回 1
}
static int cdq_get_front(MyCircularDeque *d) { return d->size == 0 ? -1 : d->data[d->head]; }
static int cdq_get_rear(MyCircularDeque *d) {
    return d->size == 0 ? -1 : d->data[(d->tail + d->cap - 1) % d->cap];
}
static int cdq_is_empty(MyCircularDeque *d) { return d->size == 0; }
static int cdq_is_full(MyCircularDeque *d) { return d->size == d->cap; }
int main(void) {                     // 程序入口：跑内嵌自测用例
    MyCircularDeque *d = cdq_new(3); // 把 cdq_new(3); 写入 MyCircularDeque *d
    if (!cdq_insert_last(d, 1)) {
        printf("FAIL 1\n");
        return 1;
    } // 若 取反 cdq_insert_last(d, 1)) { 输出「FAIL 1 」); return 1; }
    if (!cdq_insert_last(d, 2)) {
        printf("FAIL 2\n");
        return 1;
    } // 若 取反 cdq_insert_last(d, 2)) { 输出「FAIL 2 」); return 1; }
    if (!cdq_insert_front(d, 3)) {
        printf("FAIL 3\n");
        return 1;
    } // 若 取反 cdq_insert_front(d, 3)) { 输出「FAIL 3 」); return 1; }
    if (cdq_insert_front(d, 4)) {
        printf("FAIL 4\n");
        return 1;
    } // 若 cdq_insert_front(d, 4)) { 输出「FAIL 4 」); return 1; }
    if (cdq_get_rear(d) != 2) {
        printf("FAIL 5\n");
        return 1;
    } // 若 cdq_get_rear(d) 不等于 2) { 输出「FAIL 5 」); return 1; }
    if (!cdq_is_full(d)) {
        printf("FAIL 6\n");
        return 1;
    } // 若 取反 cdq_is_full(d)) { 输出「FAIL 6 」); return 1; }
    if (!cdq_delete_last(d)) {
        printf("FAIL 7\n");
        return 1;
    } // 若 取反 cdq_delete_last(d)) { 输出「FAIL 7 」); return 1; }
    if (!cdq_insert_front(d, 4)) {
        printf("FAIL 8\n");
        return 1;
    } // 若 取反 cdq_insert_front(d, 4)) { 输出「FAIL 8 」); return 1; }
    if (cdq_get_front(d) != 4) {
        printf("FAIL 9\n");
        return 1;
    } // 若 cdq_get_front(d) 不等于 4) { 输出「FAIL 9 」); return 1; }
    free(d->data);
    free(d); // free(d 减 超过 data); free(d);
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS