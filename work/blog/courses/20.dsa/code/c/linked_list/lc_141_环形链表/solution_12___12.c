/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133816714 */
/* LeetCode 141. 环形链表 — C 版（方案12） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
typedef struct LNode {
    int val;
    struct LNode *next;
} LNode; // typedef struct LNode { int 值; struct LNode 乘 下一个; } LNode;
static LNode *build_list(const int *vals,
                         int n) { // static LNode 乘 build_list(const int 乘 vals, int 元素个数) {
    LNode *head = NULL, **cur = &head; // 把 NULL, 乘 乘 当前值 赋值为 按位与 头节点; 写入 LNode *head
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        LNode *node = malloc(sizeof(LNode)); // 把 malloc(sizeof(LNode)); 写入 LNode *node
        node->val = vals[i];
        node->next = NULL; // 把 vals[下标 i]; 节点 减 超过 下一个 赋值为 NULL; 写入 node->val
        *cur = node;
        cur = &node->next;
    }
    return head; // 返回 头节点
}
static void free_list(LNode *h) {
    while (h) {
        LNode *n = h->next;
        free(h);
        h = n;
    }
}
static int has_cycle(LNode *head) {   // 定义函数/方法 has_cycle
    LNode *slow = head, *fast = head; // 把 头节点, 乘 快指针 赋值为 头节点; 写入 LNode *slow
    while (fast && fast->next) { // 循环，直到不满足「快指针 且 快指针 减 超过 下一个」
        slow = slow->next;       // 把 慢指针 减 超过 下一个; 写入 慢指针
        fast = fast->next->next; // 把 快指针 减 超过 下一个 减 超过 下一个; 写入 快指针
        if (slow == fast)
            return 1; // 若 慢指针 等于 快指针，直接返回 1
    }
    return 0; // 返回 0
}
int main(void) {                                    // 程序入口：跑内嵌自测用例
    LNode *l = build_list((int[]){3, 2, 0, -4}, 4); // 把 build_list((int[]){3,2,0, 减 4}, 4); 写入 LNode *l
    if (has_cycle(l)) {
        printf("FAIL 1\n");
        return 1;
    }                                     // 若 has_cycle(左指针)) { 输出「FAIL 1 」); return 1; }
    free_list(l);                         // free_list(左指针);
    LNode *h = build_list((int[]){1}, 1); // 把 build_list((int[]){1}, 1); 写入 LNode *h
    h->next = h;                          // 把 h; 写入 h->next
    if (!has_cycle(h)) {
        printf("FAIL 2\n");
        return 1;
    }        // 若 取反 has_cycle(h)) { 输出「FAIL 2 」); return 1; }
    free(h); // free(h);
    if (has_cycle(NULL)) {
        printf("FAIL 3\n");
        return 1;
    }                 // 若 has_cycle(NULL)) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
