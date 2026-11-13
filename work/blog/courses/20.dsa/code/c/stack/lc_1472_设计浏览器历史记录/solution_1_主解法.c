/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145338856 */
/* LeetCode 1472. 设计浏览器历史记录 — C 版（方案1） */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件
typedef struct {
    char history[64][64];
    int n;
    int cur;
} BrowserHistory;
static void bh_init(BrowserHistory *b, const char *homepage) { // 定义函数/方法 bh_init
    strcpy(b->history[0], homepage);                           // strcpy(b 减 超过 history[0], homepage);
    b->n = 1;                                                  // 把 1; 写入 b->n
    b->cur = 0;                                                // 把 0; 写入 b->cur
}
static void bh_visit(BrowserHistory *b, const char *url) { // 定义函数/方法 bh_visit
    b->n = b->cur + 1;                                     // 把 b 减 超过 当前值 加 1; 写入 b->n
    strcpy(b->history[b->n++], url); // strcpy(b 减 超过 history[b 减 超过 元素个数 加一 ], url);
    b->cur = b->n - 1;               // 把 b 减 超过 元素个数 减 1; 写入 b->cur
}
static const char *bh_back(BrowserHistory *b,
                           int steps) { // static const char 乘 bh_back(BrowserHistory 乘 b, int steps) {
    b->cur = b->cur - steps < 0 ? 0 : b->cur - steps;
    return b->history[b->cur]; // 返回 b 减 超过 history[b 减 超过 当前值]
}
static const char *bh_forward(BrowserHistory *b, int steps) {
    b->cur = b->cur + steps > b->n - 1 ? b->n - 1 : b->cur + steps;
    return b->history[b->cur]; // 返回 b 减 超过 history[b 减 超过 当前值]
}
int main(void) {                  // 程序入口：跑内嵌自测用例
    BrowserHistory b;             // BrowserHistory b;
    bh_init(&b, "leetcode.com");  // bh_init( 按位与 b, 「leetcode.com」);
    bh_visit(&b, "google.com");   // bh_visit( 按位与 b, 「google.com」);
    bh_visit(&b, "facebook.com"); // bh_visit( 按位与 b, 「facebook.com」);
    bh_visit(&b, "youtube.com");  // bh_visit( 按位与 b, 「youtube.com」);
    if (strcmp(bh_back(&b, 1), "facebook.com") != 0) {
        printf("FAIL 1\n");
        return 1;
    }
    if (strcmp(bh_back(&b, 1), "google.com") != 0) {
        printf("FAIL 2\n");
        return 1;
    }
    if (strcmp(bh_forward(&b, 1), "facebook.com") != 0) {
        printf("FAIL 3\n");
        return 1;
    }
    bh_visit(&b, "linkedin.com"); // bh_visit( 按位与 b, 「linkedin.com」);
    if (strcmp(bh_forward(&b, 2), "linkedin.com") != 0) {
        printf("FAIL 4\n");
        return 1;
    }
    if (strcmp(bh_back(&b, 2), "google.com") != 0) {
        printf("FAIL 5\n");
        return 1;
    }
    if (strcmp(bh_back(&b, 7), "leetcode.com") != 0) {
        printf("FAIL 6\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS