/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134097112 */
/* 实现LRU缓存算法功能 — C 版（方案1） */
#include <stdio.h> // 引入头文件
typedef struct {
    int cap, n;
    int keys[256];
    int vals[256];
} NoteLru;
static void nl_init(NoteLru *c, int cap) {
    c->cap = cap;
    c->n = 0;
}
static int nl_find(NoteLru *c, int k) {
    for (int i = 0; i < c->n; i++)
        if (c->keys[i] == k)
            return i;
    return -1;
}
static void nl_remove_idx(NoteLru *c, int idx) { // 定义函数/方法 nl_remove_idx
    for (int i = idx; i + 1 < c->n; i++) {
        c->keys[i] = c->keys[i + 1];
        c->vals[i] = c->vals[i + 1];
    } // 让 下标 i 从 idx 开始计数，下标 i 加 1 小于 字符 减 超过 元素个数 就继续
    c->n--; // 字符 减 超过 元素个数 减一 ;
}
static int nl_get(NoteLru *c, int k) { // 定义函数/方法 nl_get
    int i = nl_find(c, k);             // 把 nl_find(字符, 下标 k) 存入 下标 i
    if (i < 0)
        return -1;       // 若 下标 i 小于 0，直接返回 减 1
    int v = c->vals[i];  // 把 字符 减 超过 vals[下标 i] 存入 值
    int kv = c->keys[i]; // 把 字符 减 超过 keys[下标 i] 存入 kv
    nl_remove_idx(c, i); // nl_remove_idx(字符, 下标 i);
    c->keys[c->n] = kv;
    c->vals[c->n] = v;
    c->n++;
    return v; // 返回 值
}
static void nl_put(NoteLru *c, int k, int v) { // 定义函数/方法 nl_put
    int i = nl_find(c, k);                     // 把 nl_find(字符, 下标 k) 存入 下标 i
    if (i >= 0) {                              // 若 下标 i 不低于 0
        nl_remove_idx(c, i);                   // nl_remove_idx(字符, 下标 i);
    } else if (c->n == c->cap) { // 否则，若 字符 减 超过 元素个数 等于 字符 减 超过 cap
        nl_remove_idx(c, 0);     // nl_remove_idx(字符, 0);
    }
    c->keys[c->n] = k;
    c->vals[c->n] = v;
    c->n++;
}
int main(void) {      // 程序入口：跑内嵌自测用例
    NoteLru c;        // NoteLru 字符;
    nl_init(&c, 2);   // nl_init( 按位与 字符, 2);
    nl_put(&c, 1, 1); // nl_put( 按位与 字符, 1, 1);
    nl_put(&c, 2, 2); // nl_put( 按位与 字符, 2, 2);
    if (nl_get(&c, 1) != 1) {
        printf("FAIL 1\n");
        return 1;
    }                 // 若 nl_get( 按位与 字符, 1) 不等于 1) { 输出「FAIL 1 」); return 1; }
    nl_put(&c, 3, 3); // nl_put( 按位与 字符, 3, 3);
    if (nl_get(&c, 2) != -1) {
        printf("FAIL 2\n");
        return 1;
    }                 // 若 nl_get( 按位与 字符, 2) 不等于 减 1) { 输出「FAIL 2 」); return 1; }
    nl_put(&c, 4, 4); // nl_put( 按位与 字符, 4, 4);
    if (nl_get(&c, 1) != -1) {
        printf("FAIL 3\n");
        return 1;
    } // 若 nl_get( 按位与 字符, 1) 不等于 减 1) { 输出「FAIL 3 」); return 1; }
    if (nl_get(&c, 3) != 3 || nl_get(&c, 4) != 4) {
        printf("FAIL 4\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS