/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案9：规则串状态机，8 方向字母）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

typedef struct {                    // typedef struct {
    int row_num, col_num;           // int row_num, col_num;
    int pos_row, pos_col, idx;      // int pos_row, pos_col, idx;
    int r_min, c_min, r_max, c_max; // int r_min, c_min, r_max, c_max;
    char rule[8];                   // char rule[8];
} Filler;                           // } Filler;

static void filler_init(Filler *f, int rn, int cn) { // 定义函数/方法 filler_init
    f->row_num = rn;
    f->col_num = cn; // 把 rn; f 减 超过 col_num 赋值为 cn; 写入 f->row_num
    f->pos_row = f->pos_col = f->idx =
        0; // 把 f 减 超过 pos_col 赋值为 f 减 超过 idx 赋值为 0; 写入 f->pos_row
    f->r_min = f->c_min = 0; // 把 f 减 超过 c_min 赋值为 0; 写入 f->r_min
    f->r_max = rn - 1;       // 把 rn 减 1; 写入 f->r_max
    f->c_max = cn - 1;       // 把 cn 减 1; 写入 f->c_max
    strcpy(f->rule, "ESVM"); // strcpy(f 减 超过 rule, 「ESVM」);
}

static void filler_set_rule(Filler *f, const char *rule) { // 定义函数/方法 filler_set_rule
    strcpy(f->rule, rule);                                 // strcpy(f 减 超过 rule, rule);
}

static void filler_next(Filler *f, int *out_r, int *out_c) { // 定义函数/方法 filler_next
    *out_r = f->pos_row;
    *out_c = f->pos_col;
    char ch = f->rule[f->idx % strlen(f->rule)];
    if (ch == 'E') {  // 若 字符 等于 'E'
        f->pos_row++; // f 减 超过 pos_row 加一 ;
        if (f->pos_row == f->r_max) {
            f->idx++;
            f->c_min++;
        }
    } else if (ch == 'S') { // 否则，若 字符 等于 'S'
        f->pos_col++;       // f 减 超过 pos_col 加一 ;
        if (f->pos_col == f->c_max) {
            f->idx++;
            f->r_max--;
        }
    } else if (ch == 'V') { // 否则，若 字符 等于 'V'
        f->pos_row--;       // f 减 超过 pos_row 减一 ;
        if (f->pos_row == f->r_min) {
            f->idx++;
            f->c_max--;
        }
    } else if (ch == 'M') { // 否则，若 字符 等于 'M'
        f->pos_col--;       // f 减 超过 pos_col 减一 ;
        if (f->pos_col == f->c_min) {
            f->idx++;
            f->r_min++;
        }
    } else if (ch == 'e') { // 否则，若 字符 等于 'e'
        f->pos_row++;       // f 减 超过 pos_row 加一 ;
        if (f->pos_row == f->r_max) {
            f->idx++;
            f->c_max--;
        }
    } else if (ch == 's') { // 否则，若 字符 等于 '字符串'
        f->pos_col++;       // f 减 超过 pos_col 加一 ;
        if (f->pos_col == f->c_max) {
            f->idx++;
            f->r_min++;
        }
    } else if (ch == 'v') { // 否则，若 字符 等于 '值'
        f->pos_row--;       // f 减 超过 pos_row 减一 ;
        if (f->pos_row == f->r_min) {
            f->idx++;
            f->c_min++;
        }
    } else if (ch == 'm') { // 否则，若 字符 等于 '映射表'
        f->pos_col--;       // f 减 超过 pos_col 减一 ;
        if (f->pos_col == f->c_min) {
            f->idx++;
            f->r_max--;
        }
    }
}

static void test_filler(const char *rule, int rn, int cn, int seq[][2]) { // 定义函数/方法 test_filler
    Filler f;                                                             // Filler f;
    filler_init(&f, rn, cn);            // filler_init( 按位与 f, rn, cn);
    filler_set_rule(&f, rule);          // filler_set_rule( 按位与 f, rule);
    for (int i = 0; i < rn * cn; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 rn 乘 cn 就继续
        int r, c;                       // int 右指针, 字符;
        filler_next(&f, &r, &c);        // filler_next( 按位与 f, 按位与 右指针, 按位与 字符);
        seq[i][0] = r;                  // 把 右指针; 写入 seq[i][0]
        seq[i][1] = c;                  // 把 字符; 写入 seq[i][1]
    }
}

int main(void) {    // 程序入口：跑内嵌自测用例
    int seq[16][2]; // int seq[16][2];
    int want_esvm[16][2] = {
        // 把 { 写入 int want_esvm[16][2]
        {0, 0}, {1, 0}, {2, 0}, {3, 0}, {3, 1}, {3, 2}, {3, 3}, {2, 3},
        {1, 3}, {0, 3}, {0, 2}, {0, 1}, {1, 1}, {2, 1}, {2, 2}, {1, 2},
    };
    test_filler("ESVM", 4, 4, seq); // test_filler(「ESVM」, 4, 4, seq);
    for (int i = 0; i < 16; i++)    // 让 下标 i 从 0 开始计数，下标 i 小于 16 就继续
        if (seq[i][0] != want_esvm[i][0] || seq[i][1] != want_esvm[i][1]) {
            printf("ESVM failed\n");
            return 1;
        }
    int want_semv[16][2] = {
        // 把 { 写入 int want_semv[16][2]
        {0, 0}, {0, 1}, {0, 2}, {0, 3}, {1, 3}, {2, 3}, {3, 3}, {3, 2},
        {3, 1}, {3, 0}, {2, 0}, {1, 0}, {1, 1}, {1, 2}, {2, 2}, {2, 1},
    };
    test_filler("semv", 4, 4, seq); // test_filler(「semv」, 4, 4, seq);
    for (int i = 0; i < 16; i++)    // 让 下标 i 从 0 开始计数，下标 i 小于 16 就继续
        if (seq[i][0] != want_semv[i][0] || seq[i][1] != want_semv[i][1]) {
            printf("semv failed\n");
            return 1;
        }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
