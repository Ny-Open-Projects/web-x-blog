/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案6：Matrix 公开 buf 直接访问）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

typedef struct {   // typedef struct {
    int row, col;  // int row, col;
    int buf[8][8]; // int buf[8][8];
} Matrix;          // } Matrix;

static void matrix_init(Matrix *m, int r, int c) { // 定义函数/方法 matrix_init
    m->row = r;                                    // 把 右指针; 写入 m->row
    m->col = c;                                    // 把 字符; 写入 m->col
    memset(m->buf, 0, sizeof(m->buf)); // memset(映射表 减 超过 buf, 0, sizeof(映射表 减 超过 buf));
}

static int matrix_call(const Matrix *m, int r, int c) { // 定义函数/方法 matrix_call
    return m->buf[r][c];                                // 返回 映射表 减 超过 buf[右指针][字符]
}

int main(void) {                    // 程序入口：跑内嵌自测用例
    Matrix m;                       // Matrix 映射表;
    matrix_init(&m, 4, 5);          // matrix_init( 按位与 映射表, 4, 5);
    for (int i = 0; i < 4; i++)     // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
        for (int j = 0; j < 5; j++) // 让 下标 j 从 0 开始计数，下标 j 小于 5 就继续
            m.buf[i][j] = i * j;
                /* 直接访问 buf */ // 把 下标 i 乘 下标 j; 除以 乘 直接访问 buf 乘 除以 写入 m.buf[i][j]
    if (matrix_call(&m, 2, 3) != 6) {
        printf("matrix call failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
