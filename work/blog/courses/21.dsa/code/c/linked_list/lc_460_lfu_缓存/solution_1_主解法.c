/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137295891 */
/* LeetCode 460. LFU缓存 — C 版（方案1） */
#include <stdio.h> // 引入头文件
typedef struct {
    int cap, n;
    int keys[256];
    int vals[256];
    int freq[256];
    long stamp[256];
    long clock_;
} LfuSim;
static void lfu_init(LfuSim *s, int cap) {
    s->cap = cap;
    s->n = 0;
    s->clock_ = 0;
}
static int lfu_find(LfuSim *s, int k) {
    for (int i = 0; i < s->n; i++)
        if (s->keys[i] == k)
            return i;
    return -1;
}
static void lfu_remove_idx(LfuSim *s, int idx) { // 定义函数/方法 lfu_remove_idx
    for (int i = idx; i + 1 < s->n; i++) {
        s->keys[i] = s->keys[i + 1];
        s->vals[i] = s->vals[i + 1];
        s->freq[i] = s->freq[i + 1];
        s->stamp[i] = s->stamp[i + 1];
    } // 让 下标 i 从 idx 开始计数，下标 i 加 1 小于 字符串 减 超过 元素个数 就继续
    s->n--; // 字符串 减 超过 元素个数 减一 ;
}
static int lfu_get(LfuSim *s, int k) { // 定义函数/方法 lfu_get
    int i = lfu_find(s, k);            // 把 lfu_find(字符串, 下标 k) 存入 下标 i
    s->clock_++;                       // 字符串 减 超过 clock_ 加一 ;
    if (i < 0)
        return -1;           // 若 下标 i 小于 0，直接返回 减 1
    s->freq[i]++;            // 字符串 减 超过 频次表[下标 i] 加一 ;
    s->stamp[i] = s->clock_; // 把 字符串 减 超过 clock_; 写入 s->stamp[i]
    return s->vals[i];       // 返回 字符串 减 超过 vals[下标 i]
}
static void lfu_put(LfuSim *s, int k, int v) { // 定义函数/方法 lfu_put
    s->clock_++;                               // 字符串 减 超过 clock_ 加一 ;
    int i = lfu_find(s, k);                    // 把 lfu_find(字符串, 下标 k) 存入 下标 i
    if (i >= 0) {
        s->vals[i] = v;
        s->freq[i]++;
        s->stamp[i] = s->clock_;
        return;
    }
    if (s->cap == 0)
        return;           // 若 字符串 减 超过 cap 等于 0) return;
    if (s->n == s->cap) { // 若 字符串 减 超过 元素个数 等于 字符串 减 超过 cap
        int ev = 0;       // 把 0 存入 ev
        for (int j = 1; j < s->n;
             j++) { // 让 下标 j 从 1 开始计数，下标 j 小于 字符串 减 超过 元素个数 就继续
            if (s->freq[j] < s->freq[ev] || (s->freq[j] == s->freq[ev] && s->stamp[j] < s->stamp[ev]))
                ev = j;
        }
        lfu_remove_idx(s, ev); // lfu_remove_idx(字符串, ev);
    }
    s->keys[s->n] = k;
    s->vals[s->n] = v;
    s->freq[s->n] = 1;
    s->stamp[s->n] = s->clock_;
    s->n++;
}
int main(void) {     // 程序入口：跑内嵌自测用例
    LfuSim s;        // LfuSim 字符串;
    lfu_init(&s, 2); // lfu_init( 按位与 字符串, 2);
    lfu_put(&s, 1, 1);
    lfu_put(&s, 2, 2); // lfu_put( 按位与 字符串, 1, 1); lfu_put( 按位与 字符串, 2, 2);
    if (lfu_get(&s, 1) != 1) {
        printf("FAIL 1\n");
        return 1;
    } // 若 lfu_get( 按位与 字符串, 1) 不等于 1) { 输出「FAIL 1 」); return 1; }
    lfu_put(&s, 3, 3); // lfu_put( 按位与 字符串, 3, 3);
    if (lfu_get(&s, 2) != -1) {
        printf("FAIL 2\n");
        return 1;
    } // 若 lfu_get( 按位与 字符串, 2) 不等于 减 1) { 输出「FAIL 2 」); return 1; }
    if (lfu_get(&s, 3) != 3) {
        printf("FAIL 3\n");
        return 1;
    } // 若 lfu_get( 按位与 字符串, 3) 不等于 3) { 输出「FAIL 3 」); return 1; }
    lfu_put(&s, 4, 4); // lfu_put( 按位与 字符串, 4, 4);
    if (lfu_get(&s, 1) != -1) {
        printf("FAIL 4\n");
        return 1;
    } // 若 lfu_get( 按位与 字符串, 1) 不等于 减 1) { 输出「FAIL 4 」); return 1; }
    if (lfu_get(&s, 3) != 3 || lfu_get(&s, 4) != 4) {
        printf("FAIL 5\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
