/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133874671 */
/* LeetCode 142. 环形链表II — C 版（方案2） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
typedef struct LNode {
    int val;
    struct LNode *next;
} LNode; // typedef struct LNode { int 值; struct LNode 乘 下一个; } LNode;
static LNode *build_with_cycle(const int *vals, int n, int pos) {
    LNode *head = NULL, **cur = &head, *tail_at = NULL;
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        LNode *node = malloc(sizeof(LNode)); // 把 malloc(sizeof(LNode)); 写入 LNode *node
        node->val = vals[i];
        node->next = NULL; // 把 vals[下标 i]; 节点 减 超过 下一个 赋值为 NULL; 写入 node->val
        *cur = node;
        cur = &node->next;
        if (i + 1 == pos)
            tail_at = node; // 若 下标 i 加 1 等于 pos) tail_at 赋值为 节点;
    }
    if (*cur == NULL) {
    }                   // 若 乘 当前值 等于 NULL) {}
    LNode *tail = head; // 把 头节点; 写入 LNode *tail
    while (tail && tail->next)
        tail = tail->next; // 循环，直到不满足「尾节点 且 尾节点 减 超过 下一个) 尾节点 赋值为 尾节点 减 超过
                           // 下一个;」
    if (tail && tail_at)
        tail->next = tail_at; // 若 尾节点 且 tail_at) 尾节点 减 超过 下一个 赋值为 tail_at;
    return head;              // 返回 头节点
}
static LNode *detect_cycle(LNode *head) { // static LNode 乘 detect_cycle(LNode 乘 头节点) {
    LNode *slow = head, *fast = head; // 把 头节点, 乘 快指针 赋值为 头节点; 写入 LNode *slow
    while (fast && fast->next) { // 循环，直到不满足「快指针 且 快指针 减 超过 下一个」
        slow = slow->next;       // 把 慢指针 减 超过 下一个; 写入 慢指针
        fast = fast->next->next; // 把 快指针 减 超过 下一个 减 超过 下一个; 写入 快指针
        if (slow == fast) {      // 若 慢指针 等于 快指针
            LNode *p1 = head, *p2 = slow; // 把 头节点, 乘 p2 赋值为 慢指针; 写入 LNode *p1
            while (p1 != p2) {
                p1 = p1->next;
                p2 = p2->next;
            }
            return p1; // 返回 p1
        }
    }
    return NULL; // 返回 NULL
}
int main(void) { // 程序入口：跑内嵌自测用例
    LNode *h = build_with_cycle((int[]){3, 2, 0, -4}, 4,
                                2); // 把 build_with_cycle((int[]){3,2,0, 减 4}, 4, 2); 写入 LNode *h
    LNode *e = detect_cycle(h);     // 把 detect_cycle(h); 写入 LNode *e
    if (!e || e->val != 2) {
        printf("FAIL 1\n");
        return 1;
    } // 若 取反 e 或 e 减 超过 值 不等于 2) { 输出「FAIL 1 」); return 1; }
    LNode *s = malloc(sizeof(LNode));
    s->val = 1;
    s->next = NULL;
    if (detect_cycle(s)) {
        printf("FAIL 2\n");
        return 1;
    }                 // 若 detect_cycle(字符串)) { 输出「FAIL 2 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
