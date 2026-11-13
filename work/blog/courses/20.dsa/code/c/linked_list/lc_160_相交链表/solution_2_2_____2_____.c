/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133922762 */
/* LeetCode 160. 相交链表 — C 版（方案2） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
typedef struct LNode {
    int val;
    struct LNode *next;
} LNode; // typedef struct LNode { int 值; struct LNode 乘 下一个; } LNode;
static LNode *nnew(int v) {
    LNode *n = malloc(sizeof(LNode));
    n->val = v;
    n->next = NULL;
    return n;
}
static LNode *get_intersection_node(LNode *a, LNode *b) {
    if (!a || !b)
        return NULL;            // 若 取反 数组 或 取反 b，直接返回 NULL
    LNode *p1 = a, *p2 = b;     // 把 数组, 乘 p2 赋值为 b; 写入 LNode *p1
    while (p1 != p2) {          // 循环，直到不满足「p1 不等于 p2」
        p1 = p1 ? p1->next : b; // 把 p1 ? p1 减 超过 下一个 : b; 写入 p1
        p2 = p2 ? p2->next : a; // 把 p2 ? p2 减 超过 下一个 : 数组; 写入 p2
    }
    return p1; // 返回 p1
}
int main(void) {                  // 程序入口：跑内嵌自测用例
    LNode *shared = nnew(8);      // 把 nnew(8); 写入 LNode *shared
    shared->next = nnew(4);       // 把 nnew(4); 写入 shared->next
    shared->next->next = nnew(5); // 把 nnew(5); 写入 shared->next->next
    LNode *a = nnew(4);           // 把 nnew(4); 写入 LNode *a
    a->next = nnew(1);            // 把 nnew(1); 写入 a->next
    a->next->next = shared;       // 把 shared; 写入 a->next->next
    LNode *b = nnew(5);           // 把 nnew(5); 写入 LNode *b
    b->next = nnew(6);            // 把 nnew(6); 写入 b->next
    b->next->next = nnew(1);      // 把 nnew(1); 写入 b->next->next
    b->next->next->next = shared; // 把 shared; 写入 b->next->next->next
    if (get_intersection_node(a, b) != shared) {
        printf("FAIL 1\n");
        return 1;
    }
    if (get_intersection_node(nnew(1), nnew(1)) != NULL) {
        printf("FAIL 2\n");
        return 1;
    }
    if (get_intersection_node(NULL, NULL) != NULL) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
