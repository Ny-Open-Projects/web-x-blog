/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133813394 */
/* LeetCode 203. 移除链表元素 — C 版（方案2） */
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
static int list_check(LNode *h, const int *want, int wn) { // 定义函数/方法 list_check
    int i = 0;                                             // 把 0 存入 下标 i
    while (h) {
        if (i >= wn || h->val != want[i])
            return 0;
        i++;
        h = h->next;
    }
    return i == wn; // 返回 下标 i 等于 wn
}
static LNode *remove_elements(LNode *head,
                              int val) { // static LNode 乘 remove_elements(LNode 乘 头节点, int 值) {
    LNode dummy = {0, NULL};             // 把 {0, NULL}; 写入 LNode dummy
    dummy.next = head;                   // 把 头节点; 写入 下一个
    LNode *cur = &dummy;                 // 把 按位与 哨兵节点; 写入 LNode *cur
    while (cur->next) {                  // 循环，直到不满足「当前值 减 超过 下一个」
        if (cur->next->val == val) {     // 若 当前值 减 超过 下一个 减 超过 值 等于 值
            LNode *rm = cur->next;       // 把 当前值 减 超过 下一个; 写入 LNode *rm
            cur->next = rm->next;        // 把 rm 减 超过 下一个; 写入 cur->next
            free(rm);                    // free(rm);
        } else {                         // 否则
            cur = cur->next;             // 把 当前值 减 超过 下一个; 写入 当前值
        }
    }
    return dummy.next; // 返回 哨兵节点.下一个
}
int main(void) {                               // 程序入口：跑内嵌自测用例
    int w1[] = {1, 2, 3, 4, 5}, w3[] = {1, 1}; // 把 {1,2,3,4,5}, w3[] 赋值为 {1,1}; 写入 int w1[]
    LNode *r = remove_elements(build_list((int[]){1, 2, 3, 4, 5, 6}, 6), 6);
    if (!list_check(r, w1, 5)) {
        printf("FAIL 1\n");
        return 1;
    }             // 若 取反 list_check(右指针, w1, 5)) { 输出「FAIL 1 」); return 1; }
    free_list(r); // free_list(右指针);
    if (remove_elements(build_list((int[]){7, 7, 7, 7}, 4), 7) != NULL) {
        printf("FAIL 2\n");
        return 1;
    }
    LNode *r3 = remove_elements(build_list((int[]){1, 2, 2, 1}, 4), 2);
    if (!list_check(r3, w3, 2)) {
        printf("FAIL 3\n");
        return 1;
    }                 // 若 取反 list_check(r3, w3, 2)) { 输出「FAIL 3 」); return 1; }
    free_list(r3);    // free_list(r3);
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
