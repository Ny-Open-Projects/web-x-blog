/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
 * LeetCode 133278676. 使用链表（指针链）获取 JSON 节点值 — C 版（方案A：安全遍历（单用例），缺失返回 NULL）
 * 最小 JSON 对象模型：节点为对象（带命名子节点）或整数
 */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
#include <string.h> // 引入头文件

typedef struct JNode {                          // typedef struct JNode {
    const char *key;                            // const char 乘 key;
    int is_obj;                                 // int is_obj;
    int val; /* 叶子值 */                       // int 值; 除以 乘 叶子值 乘 除以
    struct JNode *children[8]; /* 对象子节点 */ // 定义类型
    int nchildren;                              // int nchildren;
} JNode;                                        // } JNode;

static JNode *obj(const char *key, JNode **children, int n) {
    JNode *j = malloc(sizeof(JNode)); // 把 malloc(sizeof(JNode)); 写入 JNode *j
    j->key = key;
    j->is_obj = 1;
    j->val = 0; // 把 key; 下标 j 减 超过 is_obj 赋值为 1; 下标 j 减 超过 值 赋值为 0; 写入 j->key
    for (int i = 0; i < n; i++)
        j->children[i] = children[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    j->nchildren = n;                 // 把 元素个数; 写入 j->nchildren
    return j;                         // 返回 下标 j
}

static JNode *leaf(const char *key, int val) { // static JNode 乘 leaf(const char 乘 key, int 值) {
    JNode *j = malloc(sizeof(JNode));          // 把 malloc(sizeof(JNode)); 写入 JNode *j
    j->key = key;
    j->is_obj = 0;
    j->val = val;
    j->nchildren = 0;
    return j; // 返回 下标 j
}

static JNode *child(JNode *node,
                    const char *key) { // static JNode 乘 子节点(JNode 乘 节点, const char 乘 key) {
    for (int i = 0; i < node->nchildren;
         i++) // 让 下标 i 从 0 开始计数，下标 i 小于 节点 减 超过 nchildren 就继续
        if (strcmp(node->children[i]->key, key) == 0)
            return node->children[i];
    return NULL; // 返回 NULL
}

static JNode *get_value(JNode *data, const char **path, int n) {
    JNode *node = data;           // 把 data; 写入 JNode *node
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        if (!node->is_obj)
            return NULL;             // 若 取反 节点 减 超过 is_obj，直接返回 NULL
        node = child(node, path[i]); // 把 子节点(节点, 当前路径[下标 i]); 写入 节点
        if (!node)
            return NULL; // 若 取反 节点，直接返回 NULL
    }
    return node; // 返回 节点
}

int main(void) {                                // 程序入口：跑内嵌自测用例
    JNode *c = leaf("c", 1);                    // 把 leaf(「字符」, 1); 写入 JNode *c
    JNode *b_children[1] = {c};                 // 把 {字符}; 写入 JNode *b_children[1]
    JNode *b = obj("b", b_children, 1);         // 把 obj(「b」, b_children, 1); 写入 JNode *b
    JNode *a_children[1] = {b};                 // 把 {b}; 写入 JNode *a_children[1]
    JNode *a = obj("a", a_children, 1);         // 把 obj(「数组」, a_children, 1); 写入 JNode *a
    JNode *e = leaf("e", 2);                    // 把 leaf(「e」, 2); 写入 JNode *e
    JNode *d_children[1] = {e};                 // 把 {e}; 写入 JNode *d_children[1]
    JNode *d = obj("d", d_children, 1);         // 把 obj(「d」, d_children, 1); 写入 JNode *d
    JNode *top_children[2] = {a, d};            // 把 {数组, d}; 写入 JNode *top_children[2]
    JNode *data = obj("root", top_children, 2); // 把 obj(「根节点」, top_children, 2); 写入 JNode *data

    const char *p1[] = {"a", "b", "c"}; // 把 {「数组」, 「数组」, 「数组」}; 写入 const char *p1[]
    const char *p2[] = {"a", "z"};      // 把 {「数组」, 「数组」}; 写入 const char *p2[]
    JNode *r1 = get_value(data, p1, 3); // 把 get_value(data, p1, 3); 写入 JNode *r1
    if (!r1 || r1->val != 1) {
        printf("p1 failed\n");
        return 1;
    } // 若 取反 r1 或 r1 减 超过 值 不等于 1) { 输出「p1 failed 」); return 1; }
    if (get_value(data, p2, 2) != NULL) {
        printf("p2 failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
