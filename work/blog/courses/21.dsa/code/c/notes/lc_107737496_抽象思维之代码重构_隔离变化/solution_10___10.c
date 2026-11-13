/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案10：Filler+Matrix 组合 9x9 全螺旋）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

typedef struct {                    // typedef struct {
    int pos_row, pos_col, idx;      // int pos_row, pos_col, idx;
    int r_min, c_min, r_max, c_max; // int r_min, c_min, r_max, c_max;
} Filler;                           // } Filler;

static void filler_init(Filler *f, int rn, int cn) { // 定义函数/方法 filler_init
    f->pos_row = f->pos_col = f->idx =
        0; // 把 f 减 超过 pos_col 赋值为 f 减 超过 idx 赋值为 0; 写入 f->pos_row
    f->r_min = f->c_min = 0; // 把 f 减 超过 c_min 赋值为 0; 写入 f->r_min
    f->r_max = rn - 1;       // 把 rn 减 1; 写入 f->r_max
    f->c_max = cn - 1;       // 把 cn 减 1; 写入 f->c_max
}

static void filler_next(Filler *f, int *out_r, int *out_c) { // 定义函数/方法 filler_next
    *out_r = f->pos_row;
    *out_c = f->pos_col;
    const char *rule = "ESVM";   // 把 「ESVM」; 写入 const char *rule
    char cmd = rule[f->idx % 4]; // 把 rule[f 减 超过 idx 对…取模 4]; 写入 char cmd
    if (cmd == 'E') {            // 若 cmd 等于 'E'
        f->pos_row++;            // f 减 超过 pos_row 加一 ;
        if (f->pos_row == f->r_max) {
            f->idx++;
            f->c_min++;
        }
    } else if (cmd == 'S') { // 否则，若 cmd 等于 'S'
        f->pos_col++;        // f 减 超过 pos_col 加一 ;
        if (f->pos_col == f->c_max) {
            f->idx++;
            f->r_max--;
        }
    } else if (cmd == 'V') { // 否则，若 cmd 等于 'V'
        f->pos_row--;        // f 减 超过 pos_row 减一 ;
        if (f->pos_row == f->r_min) {
            f->idx++;
            f->c_max--;
        }
    } else if (cmd == 'M') { // 否则，若 cmd 等于 'M'
        f->pos_col--;        // f 减 超过 pos_col 减一 ;
        if (f->pos_col == f->c_min) {
            f->idx++;
            f->r_min++;
        }
    }
}

static void fmt_row(const int *row, int n, char *out) { // 定义函数/方法 fmt_row
    out[0] = 0;                                         // 把 0; 写入 out[0]
    char cell[8];                                       // char cell[8];
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        snprintf(cell, sizeof(cell), "%2d", row[i]); // 打印输出
        if (i)
            strcat(out, " "); // 若 下标 i) strcat(out, 「 」);
        strcat(out, cell);    // 打印输出
    }
}

int main(void) {                        // 程序入口：跑内嵌自测用例
    const int rn = 9, cn = 9;           // 把 9, cn 赋值为 9; 写入 const int rn
    Filler obj;                         // Filler obj;
    filler_init(&obj, rn, cn);          // filler_init( 按位与 obj, rn, cn);
    int m[9][9];                        // int 映射表[9][9];
    memset(m, 0, sizeof(m));            // memset(映射表, 0, sizeof(映射表));
    for (int i = 0; i < rn * cn; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 rn 乘 cn 就继续
        int r, c;                       // int 右指针, 字符;
        filler_next(&obj, &r, &c);      // filler_next( 按位与 obj, 按位与 右指针, 按位与 字符);
        m[r][c] = i + 1;                // 把 下标 i 加 1; 写入 m[r][c]
    }
    const char *want[9] = {
        // 把 { 写入 const char *want[9]
        " 1 32 31 30 29 28 27 26 25", " 2 33 56 55 54 53 52 51 24", " 3 34 57 72 71 70 69 50 23",
        " 4 35 58 73 80 79 68 49 22", " 5 36 59 74 81 78 67 48 21", " 6 37 60 75 76 77 66 47 20",
        " 7 38 61 62 63 64 65 46 19", " 8 39 40 41 42 43 44 45 18", " 9 10 11 12 13 14 15 16 17",
    };
    for (int i = 0; i < rn; i++) {       // 让 下标 i 从 0 开始计数，下标 i 小于 rn 就继续
        char got[64];                    // char got[64];
        fmt_row(m[i], cn, got);          // fmt_row(映射表[下标 i], cn, got);
        if (strcmp(got, want[i]) != 0) { // 若 strcmp(got, want[下标 i]) 不等于 0
            printf("matrix9 row %d failed: got [%s]\n", i, got); // 打印输出
            return 1;                                            // 返回 1
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
