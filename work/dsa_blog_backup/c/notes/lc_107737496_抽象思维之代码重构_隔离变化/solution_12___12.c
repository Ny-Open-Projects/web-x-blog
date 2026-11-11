/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案12：Location/Rule/Filler 组合）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

typedef struct {   // typedef struct {
    char data[16]; // char data[16];
    int idx;       // int idx;
    int length;    // int 长度;
} Rule;            // } Rule;

static void rule_init(Rule *r, const char *s) { // 定义函数/方法 rule_init
    strcpy(r->data, s);                         // strcpy(右指针 减 超过 data, 字符串);
    r->idx = 0;                                 // 把 0; 写入 r->idx
    r->length = (int)strlen(s);                 // 把 (int)strlen(字符串); 写入 r->length
}

static char rule_current(const Rule *r) { // 定义函数/方法 rule_current
    return r->data[r->idx];               // 返回 右指针 减 超过 data[右指针 减 超过 idx]
}

static void rule_advance(Rule *r) { // 定义函数/方法 rule_advance
    r->idx =
        (r->idx + 1) % r->length; // 把 (右指针 减 超过 idx 加 1) 对…取模 右指针 减 超过 长度; 写入 r->idx
}

typedef struct {                    // typedef struct {
    int pos_row, pos_col;           // int pos_row, pos_col;
    int r_min, c_min, r_max, c_max; // int r_min, c_min, r_max, c_max;
    Rule cmd;                       // Rule cmd;
} Filler;                           // } Filler;

static void filler_next(Filler *f, int *out_r, int *out_c) { // 定义函数/方法 filler_next
    *out_r = f->pos_row;
    *out_c = f->pos_col;
    char ch = rule_current(&f->cmd); // 把 rule_current( 按位与 f 减 超过 cmd); 写入 char ch
    if (ch == 'E') {                 // 若 字符 等于 'E'
        f->pos_row++;                // f 减 超过 pos_row 加一 ;
        if (f->pos_row == f->r_max) {
            rule_advance(&f->cmd);
            f->c_min++;
        }
    } else if (ch == 'S') { // 否则，若 字符 等于 'S'
        f->pos_col++;       // f 减 超过 pos_col 加一 ;
        if (f->pos_col == f->c_max) {
            rule_advance(&f->cmd);
            f->r_max--;
        }
    } else if (ch == 'V') { // 否则，若 字符 等于 'V'
        f->pos_row--;       // f 减 超过 pos_row 减一 ;
        if (f->pos_row == f->r_min) {
            rule_advance(&f->cmd);
            f->c_max--;
        }
    } else if (ch == 'M') { // 否则，若 字符 等于 'M'
        f->pos_col--;       // f 减 超过 pos_col 减一 ;
        if (f->pos_col == f->c_min) {
            rule_advance(&f->cmd);
            f->r_min++;
        }
    }
}

int main(void) {               // 程序入口：跑内嵌自测用例
    Filler f;                  // Filler f;
    f.pos_row = f.pos_col = 0; // 把 f.pos_col 赋值为 0; 写入 f.pos_row
    f.r_min = f.c_min = 0;     // 把 f.c_min 赋值为 0; 写入 f.r_min
    f.r_max = 3;               // 把 3; 写入 f.r_max
    f.c_max = 3;               // 把 3; 写入 f.c_max
    rule_init(&f.cmd, "ESVM"); // rule_init( 按位与 f.cmd, 「ESVM」);
    int want[16][2] = {
        // 把 { 写入 int want[16][2]
        {0, 0}, {1, 0}, {2, 0}, {3, 0}, {3, 1}, {3, 2}, {3, 3}, {2, 3},
        {1, 3}, {0, 3}, {0, 2}, {0, 1}, {1, 1}, {2, 1}, {2, 2}, {1, 2},
    };
    for (int i = 0; i < 16; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 16 就继续
        int r, c;                  // int 右指针, 字符;
        filler_next(&f, &r, &c);   // filler_next( 按位与 f, 按位与 右指针, 按位与 字符);
        if (r != want[i][0] || c != want[i][1]) {
            printf("filler4 at %d failed\n", i);
            return 1;
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
