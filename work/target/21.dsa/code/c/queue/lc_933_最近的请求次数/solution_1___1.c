/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370
 * LeetCode 933. 最近的请求次数 — C 版 */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件

/* 方案1：push + 真出队（整体前移一位，等价 TS 数组 shift） */
typedef struct { // typedef struct {
    int *data;   // int 乘 data;
    int len;     // int 长度;
    int cap;     // int cap;
} RecentCounter; // } RecentCounter;

static RecentCounter *rc_new(void) { // static RecentCounter 乘 rc_new(void) {
    RecentCounter *c = (RecentCounter *)malloc(sizeof(RecentCounter));
    c->data = NULL; // 把 NULL; 写入 c->data
    c->len = 0;     // 把 0; 写入 c->len
    c->cap = 0;     // 把 0; 写入 c->cap
    return c;       // 返回 字符
}

static void rc_free(RecentCounter *c) { // 定义函数/方法 rc_free
    free(c->data);                      // free(字符 减 超过 data);
    free(c);                            // free(字符);
}

static int rc_ping(RecentCounter *c, int t) { // 定义函数/方法 rc_ping
    if (c->len == c->cap) {                   // 若 字符 减 超过 长度 等于 字符 减 超过 cap
        c->cap = c->cap ? c->cap * 2 : 8; // 把 字符 减 超过 cap ? 字符 减 超过 cap 乘 2 : 8; 写入 c->cap
        c->data = (int *)realloc(c->data, sizeof(int) * (size_t)c->cap);
    }
    c->data[c->len++] = t;                        // 把 另一字符串; 写入 c->data[c->len++]
    while (c->len > 0 && c->data[0] < t - 3000) { // 循环，直到不满足「字符 减 超过 长度 超过 0 且 字符 减
                                                  // 超过 data[0] 小于 另一字符串 减 3000」
        /* 真出队：整体前移一位 */
        for (int i = 1; i < c->len; i++)
            c->data[i - 1] = c->data[i]; // 让 下标 i 从 1 开始计数，下标 i 小于 字符 减 超过 长度 就继续
        c->len--;                        // 字符 减 超过 长度 减一 ;
    }
    return c->len; // 返回 字符 减 超过 长度
}

int main(void) { // 程序入口：跑内嵌自测用例
    /* 与 TS 事实源内嵌用例一致 */
    RecentCounter *c = rc_new();  // 把 rc_new(); 写入 RecentCounter *c
    int got[4];                   // int got[4];
    got[0] = rc_ping(c, 1);       // 把 rc_ping(字符, 1); 写入 got[0]
    got[1] = rc_ping(c, 100);     // 把 rc_ping(字符, 100); 写入 got[1]
    got[2] = rc_ping(c, 3001);    // 把 rc_ping(字符, 3001); 写入 got[2]
    got[3] = rc_ping(c, 3002);    // 把 rc_ping(字符, 3002); 写入 got[3]
    rc_free(c);                   // rc_free(字符);
    int want[4] = {1, 2, 3, 3};   // 把 { 1, 2, 3, 3 }; 写入 int want[4]
    for (int i = 0; i < 4; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
        if (got[i] != want[i]) {  // 若 got[下标 i] 不等于 want[下标 i]
            printf("FAIL case %d got %d want %d\n", i, got[i], want[i]); // 打印输出
            return 1;                                                    // 返回 1
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
