/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133785568 */
/* LeetCode 206. 反转链表 — C 版（方案3） */
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
static LNode *reverse_list(LNode *head) { // static LNode 乘 reverse_list(LNode 乘 头节点) {
    LNode *prev = NULL, *cur = head;      // 把 NULL, 乘 当前值 赋值为 头节点; 写入 LNode *prev
    while (cur) {                         // 循环，直到不满足「当前值」
        LNode *nxt = cur->next;           // 把 当前值 减 超过 下一个; 写入 LNode *nxt
        cur->next = prev;                 // 把 前一个; 写入 cur->next
        prev = cur;                       // 把 当前值; 写入 前一个
        cur = nxt;                        // 把 nxt; 写入 当前值
    }
    return prev; // 返回 前一个
}
int main(void) { // 程序入口：跑内嵌自测用例
    LNode *r = reverse_list(build_list((int[]){1, 2, 3, 4, 5}, 5));
    int w1[] = {5, 4, 3, 2, 1}; // 把 {5,4,3,2,1}; 写入 int w1[]
    if (!list_check(r, w1, 5)) {
        printf("FAIL 1\n");
        return 1;
    }             // 若 取反 list_check(右指针, w1, 5)) { 输出「FAIL 1 」); return 1; }
    free_list(r); // free_list(右指针);
    if (reverse_list(NULL) != NULL) {
        printf("FAIL 2\n");
        return 1;
    } // 若 reverse_list(NULL) 不等于 NULL) { 输出「FAIL 2 」); return 1; }
    LNode *r3 =
        reverse_list(build_list((int[]){1}, 1)); // 把 reverse_list(build_list((int[]){1}, 1)); 写入 LNode *r3
    int w3[] = {1};                              // 把 {1}; 写入 int w3[]
    if (!list_check(r3, w3, 1)) {
        printf("FAIL 3\n");
        return 1;
    }                 // 若 取反 list_check(r3, w3, 1)) { 输出「FAIL 3 」); return 1; }
    free_list(r3);    // free_list(r3);
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
