/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133594090 */
/* LeetCode 21. 合并两个有序链表 — C 版（方案4） */
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
        i++;
        h = h->next; // 把 h 减 超过 下一个; 写入 i++; h
    }
    return i == wn; // 返回 下标 i 等于 wn
}
static LNode *merge_two_lists(LNode *list1, LNode *list2) {
    LNode dummy = {0, NULL}; // 把 {0, NULL}; 写入 LNode dummy
    LNode *p = &dummy;       // 把 按位与 哨兵节点; 写入 LNode *p
    while (list1 && list2) { // 循环，直到不满足「list1 且 list2」
        if (list1->val < list2->val) {
            p->next = list1;
            list1 = list1->next;
        } else {
            p->next = list2;
            list2 = list2->next;
        }            // 否则
        p = p->next; // 把 节点 减 超过 下一个; 写入 节点
    }
    p->next = list1 ? list1 : list2; // 把 list1 ? list1 : list2; 写入 p->next
    return dummy.next;               // 返回 哨兵节点.下一个
}
int main(void) { // 程序入口：跑内嵌自测用例
    LNode *got = merge_two_lists(build_list((int[]){1, 2, 4}, 3), build_list((int[]){1, 3, 4}, 3));
    int w1[] = {1, 1, 2, 3, 4, 4}; // 把 {1,1,2,3,4,4}; 写入 int w1[]
    if (!list_check(got, w1, 6)) {
        printf("FAIL 1\n");
        return 1;
    }               // 若 取反 list_check(got, w1, 6)) { 输出「FAIL 1 」); return 1; }
    free_list(got); // free_list(got);
    LNode *got2 = merge_two_lists(NULL, NULL); // 把 merge_two_lists(NULL, NULL); 写入 LNode *got2
    if (got2 != NULL) {
        printf("FAIL 2\n");
        return 1;
    } // 若 got2 不等于 NULL) { 输出「FAIL 2 」); return 1; }
    LNode *got3 = merge_two_lists(NULL, build_list((int[]){0}, 1));
    int w3[] = {0}; // 把 {0}; 写入 int w3[]
    if (!list_check(got3, w3, 1)) {
        printf("FAIL 3\n");
        return 1;
    }                 // 若 取反 list_check(got3, w3, 1)) { 输出「FAIL 3 」); return 1; }
    free_list(got3);  // free_list(got3);
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
