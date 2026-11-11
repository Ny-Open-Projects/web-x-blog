/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134350547 */
/* LeetCode 384. 打乱数组 — C 版（方案1） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
typedef struct {
    int orig[4096];
    int cur[4096];
    int n;
} ShuffleArray;
static void sa_init(ShuffleArray *s, const int *vals, int n) { // 定义函数/方法 sa_init
    s->n = n;                                                  // 把 元素个数; 写入 s->n
    for (int i = 0; i < n; i++) {
        s->orig[i] = vals[i];
        s->cur[i] = vals[i];
    } // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
}
static int *sa_reset(ShuffleArray *s) { // static int 乘 sa_reset(ShuffleArray 乘 字符串) {
    for (int i = 0; i < s->n; i++)
        s->cur[i] = s->orig[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 字符串 减 超过 元素个数 就继续
    return s->cur; // 返回 字符串 减 超过 当前值
}
static int *sa_shuffle(ShuffleArray *s) { // static int 乘 sa_shuffle(ShuffleArray 乘 字符串) {
    for (int i = s->n - 1; i > 0;
         i--) { // 让 下标 i 从 字符串 减 超过 元素个数 减 1 开始计数，下标 i 超过 0 就继续
        int j = 0; /* 确定性：j=0 */ // 把 0; 除以 乘 确定性：下标 j 赋值为 0 乘 除以 存入 下标 j
        int t = s->cur[i];
        s->cur[i] = s->cur[j];
        s->cur[j] = t;
    }
    return s->cur; // 返回 字符串 减 超过 当前值
}
static int is_perm(const int *a, const int *b, int n) { // 定义判定函数 is_perm
    int ca[4096], cb[4096];                             // int ca[4096], cb[4096];
    for (int i = 0; i < n; i++) {
        ca[i] = a[i];
        cb[i] = b[i];
    } // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
            if (ca[i] > ca[j]) {
                int t = ca[i];
                ca[i] = ca[j];
                ca[j] = t;
            }
            if (cb[i] > cb[j]) {
                int t = cb[i];
                cb[i] = cb[j];
                cb[j] = t;
            }
        }
    for (int i = 0; i < n; i++)
        if (ca[i] != cb[i])
            return 0; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    return 1;         // 返回 1
}
int main(void) {                      // 程序入口：跑内嵌自测用例
    ShuffleArray s;                   // ShuffleArray 字符串;
    sa_init(&s, (int[]){1, 2, 3}, 3); // sa_init( 按位与 字符串, (int[]){1,2,3}, 3);
    int *sh = sa_shuffle(&s);         // 把 sa_shuffle( 按位与 字符串); 写入 int *sh
    if (!is_perm(sh, s.orig, 3)) {
        printf("FAIL 1\n");
        return 1;
    }                      // 若 取反 is_perm(sh, 字符串.orig, 3)) { 输出「FAIL 1 」); return 1; }
    int *r = sa_reset(&s); // 把 sa_reset( 按位与 字符串); 写入 int *r
    if (!(r[0] == 1 && r[1] == 2 && r[2] == 3)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS