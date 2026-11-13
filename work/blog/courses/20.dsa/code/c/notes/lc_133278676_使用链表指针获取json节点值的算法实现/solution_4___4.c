/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
 * LeetCode 133278676. 使用链表（指针链）获取 JSON 节点值 — C 版（方案B：逐键求值，合法路径直接索引）
 */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
#include <string.h> // 引入头文件

typedef struct JNode {         // typedef struct JNode {
    const char *key;           // const char 乘 key;
    int is_obj;                // int is_obj;
    int val;                   // int 值;
    struct JNode *children[8]; // 定义类型
    int nchildren;             // int nchildren;
} JNode;                       // } JNode;

static JNode *child(JNode *node,
                    const char *key) { // static JNode 乘 子节点(JNode 乘 节点, const char 乘 key) {
    for (int i = 0; i < node->nchildren;
         i++) // 让 下标 i 从 0 开始计数，下标 i 小于 节点 减 超过 nchildren 就继续
        if (strcmp(node->children[i]->key, key) == 0)
            return node->children[i];
    return NULL; // 返回 NULL
}

/* 直接求值：假定路径合法（与 TS get_value_eval 一致） */
static JNode *get_value_eval(JNode *data, const char **path, int n) {
    JNode *cur = data; // 把 data; 写入 JNode *cur
    for (int i = 0; i < n; i++)
        cur = child(cur, path[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    return cur;                    // 返回 当前值
}

int main(void) {                         // 程序入口：跑内嵌自测用例
    JNode *c = calloc(1, sizeof(JNode)); // 把 calloc(1, sizeof(JNode)); 写入 JNode *c
    c->key = "c";
    c->val = 1;                          // 把 「字符」; 字符 减 超过 值 赋值为 1; 写入 c->key
    JNode *b = calloc(1, sizeof(JNode)); // 把 calloc(1, sizeof(JNode)); 写入 JNode *b
    b->key = "b";
    b->is_obj = 1;
    b->children[0] = c;
    b->nchildren = 1;
    JNode *a = calloc(1, sizeof(JNode)); // 把 calloc(1, sizeof(JNode)); 写入 JNode *a
    a->key = "a";
    a->is_obj = 1;
    a->children[0] = b;
    a->nchildren = 1;
    JNode *e = calloc(1, sizeof(JNode)); // 把 calloc(1, sizeof(JNode)); 写入 JNode *e
    e->key = "e";
    e->val = 2;                          // 把 「e」; e 减 超过 值 赋值为 2; 写入 e->key
    JNode *d = calloc(1, sizeof(JNode)); // 把 calloc(1, sizeof(JNode)); 写入 JNode *d
    d->key = "d";
    d->is_obj = 1;
    d->children[0] = e;
    d->nchildren = 1;
    JNode *data = calloc(1, sizeof(JNode)); // 把 calloc(1, sizeof(JNode)); 写入 JNode *data
    data->key = "root";
    data->is_obj = 1; // 把 「根节点」; data 减 超过 is_obj 赋值为 1; 写入 data->key
    data->children[0] = a;
    data->children[1] = d;
    data->nchildren = 2;

    const char *p1[] = {"a", "b", "c"}; // 把 {「数组」, 「数组」, 「数组」}; 写入 const char *p1[]
    const char *p2[] = {"d", "e"};      // 把 {「d」, 「d」}; 写入 const char *p2[]
    if (get_value_eval(data, p1, 3)->val != 1) {
        printf("p1 failed\n");
        return 1;
    }
    if (get_value_eval(data, p2, 2)->val != 2) {
        printf("p2 failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
