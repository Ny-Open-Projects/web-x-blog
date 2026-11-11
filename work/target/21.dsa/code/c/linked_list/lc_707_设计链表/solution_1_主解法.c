/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134120377 */
/* LeetCode 707. 设计链表 — C 版（方案1） */
#include <stdio.h> // 引入头文件
typedef struct {
    int items[4096];
    int n;
} MyList;                                    // typedef struct { int items[4096]; int 元素个数; } MyList;
static void ml_init(MyList *l) { l->n = 0; } // 把 0; } 写入 static void ml_init(MyList *l) { l->n
static void ml_add_head(MyList *l, int x) {  // 定义函数/方法 ml_add_head
    for (int i = l->n; i > 0; i--)
        l->items[i] = l->items[i - 1]; // 让 下标 i 从 左指针 减 超过 元素个数 开始计数，下标 i 超过 0 就继续
    l->items[0] = x; // 把 x; 写入 l->items[0]
    l->n++;          // 左指针 减 超过 元素个数 加一 ;
}
static void ml_add_tail(MyList *l, int x) { l->items[l->n++] = x; }
static void ml_add_at(MyList *l, int idx, int x) { // 定义函数/方法 ml_add_at
    if (idx < 0)
        idx = 0; // 若 idx 小于 0) idx 赋值为 0;
    if (idx > l->n)
        return; // 若 idx 超过 左指针 减 超过 元素个数) return;
    for (int i = l->n; i > idx; i--)
        l->items[i] =
            l->items[i - 1]; // 让 下标 i 从 左指针 减 超过 元素个数 开始计数，下标 i 超过 idx 就继续
    l->items[idx] = x; // 把 x; 写入 l->items[idx]
    l->n++;            // 左指针 减 超过 元素个数 加一 ;
}
static int ml_get(MyList *l, int idx) { // 定义函数/方法 ml_get
    if (idx < 0 || idx >= l->n)
        return -1; // 若 idx 小于 0 或 idx 不低于 左指针 减 超过 元素个数，直接返回 减 1
    return l->items[idx]; // 返回 左指针 减 超过 items[idx]
}
static void ml_del(MyList *l, int idx) { // 定义函数/方法 ml_del
    if (idx < 0 || idx >= l->n)
        return; // 若 idx 小于 0 或 idx 不低于 左指针 减 超过 元素个数) return;
    for (int i = idx; i + 1 < l->n; i++)
        l->items[i] =
            l->items[i + 1]; // 让 下标 i 从 idx 开始计数，下标 i 加 1 小于 左指针 减 超过 元素个数 就继续
    l->n--; // 左指针 减 超过 元素个数 减一 ;
}
int main(void) {         // 程序入口：跑内嵌自测用例
    MyList l;            // MyList 左指针;
    ml_init(&l);         // ml_init( 按位与 左指针);
    ml_add_head(&l, 1);  // ml_add_head( 按位与 左指针, 1);
    ml_add_tail(&l, 3);  // ml_add_tail( 按位与 左指针, 3);
    ml_add_at(&l, 1, 2); // ml_add_at( 按位与 左指针, 1, 2);
    if (ml_get(&l, 1) != 2) {
        printf("FAIL 1\n");
        return 1;
    }              // 若 ml_get( 按位与 左指针, 1) 不等于 2) { 输出「FAIL 1 」); return 1; }
    ml_del(&l, 1); // ml_del( 按位与 左指针, 1);
    if (ml_get(&l, 1) != 3) {
        printf("FAIL 2\n");
        return 1;
    }                 // 若 ml_get( 按位与 左指针, 1) 不等于 3) { 输出「FAIL 2 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
