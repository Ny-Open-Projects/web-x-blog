/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案8：Filler 状态机 + hasNext 部分填充）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

typedef struct {                    // typedef struct {
    int row_num, col_num;           // int row_num, col_num;
    char rule[8];                   // char rule[8];
    int pos_row, pos_col;           // int pos_row, pos_col;
    int idx;                        // int idx;
    int r_min, c_min, r_max, c_max; // int r_min, c_min, r_max, c_max;
} Filler;                           // } Filler;

static void filler_init(Filler *f, int rn, int cn) { // 定义函数/方法 filler_init
    f->row_num = rn;                                 // 把 rn; 写入 f->row_num
    f->col_num = cn;                                 // 把 cn; 写入 f->col_num
    strcpy(f->rule, "ESVM");                         // strcpy(f 减 超过 rule, 「ESVM」);
    f->pos_row = 0;                                  // 把 0; 写入 f->pos_row
    f->pos_col = 0;                                  // 把 0; 写入 f->pos_col
    f->idx = 0;                                      // 把 0; 写入 f->idx
    f->r_min = 0;                                    // 把 0; 写入 f->r_min
    f->c_min = 0;                                    // 把 0; 写入 f->c_min
    f->r_max = rn - 1;                               // 把 rn 减 1; 写入 f->r_max
    f->c_max = cn - 1;                               // 把 cn 减 1; 写入 f->c_max
}

static void filler_set_rule(Filler *f, const char *r) { // 定义函数/方法 filler_set_rule
    strcpy(f->rule, r);                                 // strcpy(f 减 超过 rule, 右指针);
}

static int filler_has_next(const Filler *f) { // 定义函数/方法 filler_has_next
    return f->r_min <= f->pos_row && f->pos_row <= f->r_max && f->c_min <= f->pos_col &&
           f->pos_col <= f->c_max;
}

static void filler_next(Filler *f, int *out_r, int *out_c) { // 定义函数/方法 filler_next
    *out_r = f->pos_row;
    *out_c = f->pos_col;
    char cmd = f->rule[f->idx % 4]; // 把 f 减 超过 rule[f 减 超过 idx 对…取模 4]; 写入 char cmd
    if (cmd == 'E') {               // 若 cmd 等于 'E'
        f->pos_row += 1;            // 把 1; 写入 f->pos_row +
        if (f->pos_row == f->r_max) {
            f->idx += 1;
            f->c_min += 1;
        }
    } else if (cmd == 'S') { // 否则，若 cmd 等于 'S'
        f->pos_col += 1;     // 把 1; 写入 f->pos_col +
        if (f->pos_col == f->c_max) {
            f->idx += 1;
            f->r_max -= 1;
        }
    } else if (cmd == 'V') { // 否则，若 cmd 等于 'V'
        f->pos_row -= 1;     // 把 1; 写入 f->pos_row -
        if (f->pos_row == f->r_min) {
            f->idx += 1;
            f->c_max -= 1;
        }
    } else if (cmd == 'M') { // 否则，若 cmd 等于 'M'
        f->pos_col -= 1;     // 把 1; 写入 f->pos_col -
        if (f->pos_col == f->c_min) {
            f->idx += 1;
            f->r_min += 1;
        }
    }
}

static void fill_matrix(int rn, int cn, const char *rule, int mat[][8]) { // 定义函数/方法 fill_matrix
    for (int i = 0; i < rn; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 rn 就继续
        for (int j = 0; j < cn; j++)
            mat[i][j] = 0;        // 让 下标 j 从 0 开始计数，下标 j 小于 cn 就继续
    Filler f;                     // Filler f;
    filler_init(&f, rn, cn);      // filler_init( 按位与 f, rn, cn);
    filler_set_rule(&f, rule);    // filler_set_rule( 按位与 f, rule);
    int i = 1, r, c;              // 把 1, 右指针, 字符 存入 下标 i
    while (filler_has_next(&f)) { // 循环，直到不满足「filler_has_next( 按位与 f」
        filler_next(&f, &r, &c);  // filler_next( 按位与 f, 按位与 右指针, 按位与 字符);
        mat[r][c] = i;            // 把 下标 i; 写入 mat[r][c]
        i++;                      // 下标 i 加一
    }
}

int main(void) {   // 程序入口：跑内嵌自测用例
    int mat[8][8]; // int mat[8][8];
    int want1[6][6] = {
        // 把 { 写入 int want1[6][6]
        {1, 0, 0, 0, 0, 0}, {2, 0, 0, 0, 0, 0}, {3, 0, 0, 0, 0, 0},
        {4, 0, 0, 0, 0, 0}, {5, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0},
    };
    fill_matrix(6, 6, "ESVM", mat); // fill_matrix(6, 6, 「ESVM」, mat);
    for (int i = 0; i < 6; i++)     // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
        for (int j = 0; j < 6; j++) // 让 下标 j 从 0 开始计数，下标 j 小于 6 就继续
            if (mat[i][j] != want1[i][j]) {
                printf("case1 failed\n");
                return 1;
            }
    int want2[3][3] = {
        {1, 0, 0}, {2, 0, 0}, {0, 0, 0}}; // 把 {{1, 0, 0}, {2, 0, 0}, {0, 0, 0}}; 写入 int want2[3][3]
    fill_matrix(3, 3, "ESVM", mat);       // fill_matrix(3, 3, 「ESVM」, mat);
    for (int i = 0; i < 3; i++)           // 让 下标 i 从 0 开始计数，下标 i 小于 3 就继续
        for (int j = 0; j < 3; j++)       // 让 下标 j 从 0 开始计数，下标 j 小于 3 就继续
            if (mat[i][j] != want2[i][j]) {
                printf("case2 failed\n");
                return 1;
            }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
