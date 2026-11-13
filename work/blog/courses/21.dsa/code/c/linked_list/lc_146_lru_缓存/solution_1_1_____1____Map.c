/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134537871 */
/* LeetCode 146. LRU缓存 — C 版（方案1） */
#include <stdio.h> // 引入头文件
/* 简易 LRU：时间戳法（容量小，线性扫描） */
typedef struct {
    int cap, n;
    int keys[256];
    int vals[256];
    long stamp[256];
    long clock_;
} LruSim;
static void lru_init(LruSim *s, int cap) {
    s->cap = cap;
    s->n = 0;
    s->clock_ = 0;
}
static int lru_find(LruSim *s, int k) { // 定义函数/方法 lru_find
    for (int i = 0; i < s->n; i++)
        if (s->keys[i] == k)
            return i; // 让 下标 i 从 0 开始计数，下标 i 小于 字符串 减 超过 元素个数 就继续
    return -1; // 返回 减 1
}
static void lru_remove_idx(LruSim *s, int idx) { // 定义函数/方法 lru_remove_idx
    for (int i = idx; i + 1 < s->n; i++) {
        s->keys[i] = s->keys[i + 1];
        s->vals[i] = s->vals[i + 1];
        s->stamp[i] = s->stamp[i + 1];
    } // 让 下标 i 从 idx 开始计数，下标 i 加 1 小于 字符串 减 超过 元素个数 就继续
    s->n--; // 字符串 减 超过 元素个数 减一 ;
}
static int lru_get(LruSim *s, int k) { // 定义函数/方法 lru_get
    int i = lru_find(s, k);            // 把 lru_find(字符串, 下标 k) 存入 下标 i
    if (i < 0)
        return -1;             // 若 下标 i 小于 0，直接返回 减 1
    s->stamp[i] = ++s->clock_; // 把 加一 字符串 减 超过 clock_; 写入 s->stamp[i]
    return s->vals[i];         // 返回 字符串 减 超过 vals[下标 i]
}
static void lru_put(LruSim *s, int k, int v) { // 定义函数/方法 lru_put
    int i = lru_find(s, k);                    // 把 lru_find(字符串, 下标 k) 存入 下标 i
    if (i >= 0) {
        s->vals[i] = v;
        s->stamp[i] = ++s->clock_;
        return;
    }
    if (s->n == s->cap) { // 若 字符串 减 超过 元素个数 等于 字符串 减 超过 cap
        int oldest = 0;   // 把 0 存入 oldest
        for (int j = 1; j < s->n; j++)
            if (s->stamp[j] < s->stamp[oldest])
                oldest = j; // 让 下标 j 从 1 开始计数，下标 j 小于 字符串 减 超过 元素个数 就继续
        lru_remove_idx(s, oldest); // lru_remove_idx(字符串, oldest);
    }
    s->keys[s->n] = k;
    s->vals[s->n] = v;
    s->stamp[s->n] = ++s->clock_;
    s->n++;
}
int main(void) {     // 程序入口：跑内嵌自测用例
    LruSim s;        // LruSim 字符串;
    lru_init(&s, 2); // lru_init( 按位与 字符串, 2);
    lru_put(&s, 1, 1);
    lru_put(&s, 2, 2); // lru_put( 按位与 字符串, 1, 1); lru_put( 按位与 字符串, 2, 2);
    if (lru_get(&s, 1) != 1) {
        printf("FAIL 1\n");
        return 1;
    } // 若 lru_get( 按位与 字符串, 1) 不等于 1) { 输出「FAIL 1 」); return 1; }
    lru_put(&s, 3, 3); // lru_put( 按位与 字符串, 3, 3);
    if (lru_get(&s, 2) != -1) {
        printf("FAIL 2\n");
        return 1;
    } // 若 lru_get( 按位与 字符串, 2) 不等于 减 1) { 输出「FAIL 2 」); return 1; }
    lru_put(&s, 4, 4); // lru_put( 按位与 字符串, 4, 4);
    if (lru_get(&s, 1) != -1) {
        printf("FAIL 3\n");
        return 1;
    } // 若 lru_get( 按位与 字符串, 1) 不等于 减 1) { 输出「FAIL 3 」); return 1; }
    if (lru_get(&s, 3) != 3 || lru_get(&s, 4) != 4) {
        printf("FAIL 4\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
