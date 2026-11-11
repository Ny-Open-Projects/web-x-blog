/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134255301 */
/* LeetCode 380. O(1)时间插入删除和获取随机元素 — C 版（方案1） */
#include <stdio.h> // 引入头文件
typedef struct {
    int vals[4096];
    int pos[65536];
    int n;
} RandomizedSet;
static void rs_init(RandomizedSet *s) {
    s->n = 0;
    for (int i = 0; i < 65536; i++)
        s->pos[i] = -1;
}
static int rs_insert(RandomizedSet *s, int val) { // 定义函数/方法 rs_insert
    int idx = val + 32768;                        // 把 值 加 32768 存入 idx
    if (s->pos[idx] >= 0)
        return 0;          // 若 字符串 减 超过 pos[idx] 不低于 0，直接返回 0
    s->pos[idx] = s->n;    // 把 字符串 减 超过 元素个数; 写入 s->pos[idx]
    s->vals[s->n++] = val; // 把 值; 写入 s->vals[s->n++]
    return 1;              // 返回 1
}
static int rs_remove(RandomizedSet *s, int val) { // 定义函数/方法 rs_remove
    int idx = val + 32768;                        // 把 值 加 32768 存入 idx
    if (s->pos[idx] < 0)
        return 0;                 // 若 字符串 减 超过 pos[idx] 小于 0，直接返回 0
    int i = s->pos[idx];          // 把 字符串 减 超过 pos[idx] 存入 下标 i
    int last = s->vals[s->n - 1]; // 把 字符串 减 超过 vals[字符串 减 超过 元素个数 减 1] 存入 last
    s->vals[i] = last;            // 把 last; 写入 s->vals[i]
    s->pos[last + 32768] = i; // 把 下标 i; 写入 s->pos[last + 32768]
    s->n--;                   // 字符串 减 超过 元素个数 减一 ;
    s->pos[idx] = -1;         // 把 减 1; 写入 s->pos[idx]
    return 1;                 // 返回 1
}
static int rs_get_random(RandomizedSet *s) { return s->vals[s->n % s->n]; }
int main(void) {     // 程序入口：跑内嵌自测用例
    RandomizedSet s; // RandomizedSet 字符串;
    rs_init(&s);     // rs_init( 按位与 字符串);
    if (!rs_insert(&s, 1)) {
        printf("FAIL 1\n");
        return 1;
    } // 若 取反 rs_insert( 按位与 字符串, 1)) { 输出「FAIL 1 」); return 1; }
    if (rs_remove(&s, 2)) {
        printf("FAIL 2\n");
        return 1;
    } // 若 rs_remove( 按位与 字符串, 2)) { 输出「FAIL 2 」); return 1; }
    if (!rs_insert(&s, 2)) {
        printf("FAIL 3\n");
        return 1;
    } // 若 取反 rs_insert( 按位与 字符串, 2)) { 输出「FAIL 3 」); return 1; }
    int r = rs_get_random(&s); // 把 rs_get_random( 按位与 字符串) 存入 右指针
    if (r != 1 && r != 2) {
        printf("FAIL 4\n");
        return 1;
    } // 若 右指针 不等于 1 且 右指针 不等于 2) { 输出「FAIL 4 」); return 1; }
    if (!rs_remove(&s, 1)) {
        printf("FAIL 5\n");
        return 1;
    } // 若 取反 rs_remove( 按位与 字符串, 1)) { 输出「FAIL 5 」); return 1; }
    if (rs_insert(&s, 2)) {
        printf("FAIL 6\n");
        return 1;
    } // 若 rs_insert( 按位与 字符串, 2)) { 输出「FAIL 6 」); return 1; }
    if (rs_get_random(&s) != 2) {
        printf("FAIL 7\n");
        return 1;
    } // 若 rs_get_random( 按位与 字符串) 不等于 2) { 输出「FAIL 7 」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS