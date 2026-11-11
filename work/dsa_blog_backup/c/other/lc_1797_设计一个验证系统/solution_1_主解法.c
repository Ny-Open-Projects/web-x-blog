/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145634738 */
/* LeetCode 1797. 设计一个验证系统 — C 版（方案1） */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件
typedef struct {
    long ttl;
    char ids[64][32];
    long exps[64];
    int n;
} AuthManager;
static void am_init(AuthManager *m, long ttl) {
    m->ttl = ttl;
    m->n = 0;
}
static int am_find(AuthManager *m, const char *id) { // 定义函数/方法 am_find
    for (int i = 0; i < m->n; i++)
        if (strcmp(m->ids[i], id) == 0)
            return i; // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 减 超过 元素个数 就继续
    return -1; // 返回 减 1
}
static void am_generate(AuthManager *m, const char *id, long t) { // 定义函数/方法 am_generate
    int i = am_find(m, id); // 把 am_find(映射表, id) 存入 下标 i
    if (i < 0) {
        i = m->n++;
        strcpy(m->ids[i], id);
    }
    m->exps[i] = t + m->ttl; // 把 另一字符串 加 映射表 减 超过 ttl; 写入 m->exps[i]
}
static int am_count(AuthManager *m, long t) { // 定义函数/方法 am_count
    int cnt = 0;                              // 把 0 存入 计数
    for (int i = 0; i < m->n; i++)
        if (m->exps[i] > t)
            cnt++; // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 减 超过 元素个数 就继续
    return cnt; // 返回 计数
}
static int am_renew(AuthManager *m, const char *id, long t) { // 定义函数/方法 am_renew
    int i = am_find(m, id);                                   // 把 am_find(映射表, id) 存入 下标 i
    if (i >= 0 && m->exps[i] > t)
        m->exps[i] = t + m->ttl;
    return am_count(m, t); // 返回 am_count(映射表, 另一字符串)
}
int main(void) {               // 程序入口：跑内嵌自测用例
    AuthManager m;             // AuthManager 映射表;
    am_init(&m, 5);            // am_init( 按位与 映射表, 5);
    am_generate(&m, "aaa", 1); // am_generate( 按位与 映射表, 「aaa」, 1);
    if (am_count(&m, 3) != 1) {
        printf("FAIL c1\n");
        return 1;
    } // 若 am_count( 按位与 映射表, 3) 不等于 1) { 输出「FAIL c1 」); return 1; }
    if (am_renew(&m, "aaa", 4) != 1) {
        printf("FAIL r\n");
        return 1;
    }
    if (am_count(&m, 6) != 1) {
        printf("FAIL c2\n");
        return 1;
    } // 若 am_count( 按位与 映射表, 6) 不等于 1) { 输出「FAIL c2 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
