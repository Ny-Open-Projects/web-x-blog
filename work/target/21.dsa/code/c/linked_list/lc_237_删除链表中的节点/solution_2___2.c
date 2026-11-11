/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133886377 */
/* LeetCode 237. 删除链表中的节点 — C 版（方案2） */
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
static void delete_node(LNode *node) { // 定义函数/方法 delete_node
    LNode *next = node->next;          // 把 节点 减 超过 下一个; 写入 LNode *next
    node->val = next->val;             // 把 下一个 减 超过 值; 写入 node->val
    node->next = next->next;           // 把 下一个 减 超过 下一个; 写入 node->next
    free(next);                        // free(下一个);
}
int main(void) {                                   // 程序入口：跑内嵌自测用例
    LNode *l = build_list((int[]){4, 5, 1, 9}, 4); // 把 build_list((int[]){4,5,1,9}, 4); 写入 LNode *l
    delete_node(l->next);                          // delete_node(左指针 减 超过 下一个);
    int w1[] = {4, 1, 9};                          // 把 {4,1,9}; 写入 int w1[]
    if (!list_check(l, w1, 3)) {
        printf("FAIL 1\n");
        return 1;
    }             // 若 取反 list_check(左指针, w1, 3)) { 输出「FAIL 1 」); return 1; }
    free_list(l); // free_list(左指针);
    LNode *l2 = build_list((int[]){1, 2, 3}, 3); // 把 build_list((int[]){1,2,3}, 3); 写入 LNode *l2
    delete_node(l2->next);                       // delete_node(l2 减 超过 下一个);
    int w2[] = {1, 3};                           // 把 {1,3}; 写入 int w2[]
    if (!list_check(l2, w2, 2)) {
        printf("FAIL 2\n");
        return 1;
    }                 // 若 取反 list_check(l2, w2, 2)) { 输出「FAIL 2 」); return 1; }
    free_list(l2);    // free_list(l2);
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
