/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134283831 */
/* LeetCode 23. 合并K个升序链表 — C 版（方案4） */
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
    while (h) {                                            // 循环，直到不满足「h」
        if (i >= wn || h->val != want[i])
            return 0; // 若 下标 i 不低于 wn 或 h 减 超过 值 不等于 want[下标 i]，直接返回 0
        i++;          // 下标 i 加一
        h = h->next; // 把 h 减 超过 下一个; 写入 h
    }
    return i == wn; // 返回 下标 i 等于 wn
}
static LNode *merge_two(LNode *a, LNode *b) { // static LNode 乘 merge_two(LNode 乘 数组, LNode 乘 b) {
    LNode dummy = {0, NULL};                  // 把 {0, NULL}; 写入 LNode dummy
    LNode *cur = &dummy;                      // 把 按位与 哨兵节点; 写入 LNode *cur
    while (a && b) {                          // 循环，直到不满足「数组 且 b」
        if (a->val <= b->val) {
            cur->next = a;
            a = a->next;
        } else {
            cur->next = b;
            b = b->next;
        }                // 否则
        cur = cur->next; // 把 当前值 减 超过 下一个; 写入 当前值
    }
    cur->next = a ? a : b; // 把 数组 ? 数组 : b; 写入 cur->next
    return dummy.next;     // 返回 哨兵节点.下一个
}
static LNode *merge_k_lists(LNode **lists,
                            int k) { // static LNode 乘 merge_k_lists(LNode 乘 乘 lists, int 下标 k) {
    LNode *acc = NULL;               // 把 NULL; 写入 LNode *acc
    for (int i = 0; i < k; i++)
        acc = merge_two(acc, lists[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 下标 k 就继续
    return acc;                         // 返回 累加器
}
int main(void) {                                // 程序入口：跑内嵌自测用例
    LNode *lists[3];                            // LNode 乘 lists[3];
    lists[0] = build_list((int[]){1, 4, 5}, 3); // 把 build_list((int[]){1,4,5}, 3); 写入 lists[0]
    lists[1] = build_list((int[]){1, 3, 4}, 3); // 把 build_list((int[]){1,3,4}, 3); 写入 lists[1]
    lists[2] = build_list((int[]){2, 6}, 2);    // 把 build_list((int[]){2,6}, 2); 写入 lists[2]
    LNode *got = merge_k_lists(lists, 3);       // 把 merge_k_lists(lists, 3); 写入 LNode *got
    int want[] = {1, 1, 2, 3, 4, 4, 5, 6};      // 把 {1,1,2,3,4,4,5,6}; 写入 int want[]
    if (!list_check(got, want, 8)) {
        printf("FAIL 1\n");
        return 1;
    }               // 若 取反 list_check(got, want, 8)) { 输出「FAIL 1 」); return 1; }
    free_list(got); // free_list(got);
    if (merge_k_lists(NULL, 0) != NULL) {
        printf("FAIL 2\n");
        return 1;
    }
    LNode *lists2[1] = {NULL}; // 把 {NULL}; 写入 LNode *lists2[1]
    if (merge_k_lists(lists2, 1) != NULL) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
