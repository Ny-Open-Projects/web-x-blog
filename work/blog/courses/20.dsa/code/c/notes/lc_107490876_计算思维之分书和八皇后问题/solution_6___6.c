/* 来源：https://blog.csdn.net/tyro_java/article/details/107490876
 * LeetCode 107490876. 分书和八皇后问题 — C 版（方案6：八皇后不可变状态函数式）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

static const int LIKE_UNUSED = 0; // 把 0; 写入 static const int LIKE_UNUSED

typedef struct {    // typedef struct {
    int col_row[8]; // int col_row[8];
    int rows[8];    // int 行数[8];
    int diag1[16];  // int diag1[16];
    int diag2[16];  // int diag2[16];
} State;            // } State;

static int sols[100][8];  // static int sols[100][8];
static int sol_count = 0; // 把 0; 写入 static int sol_count

static void place(int col, int n, State st) { // 定义函数/方法 place
    if (col == n) {                           // 若 col 等于 元素个数
        memcpy(sols[sol_count], st.col_row,
               sizeof(int) * n); // memcpy(sols[sol_count], st.col_row, sizeof(int) 乘 元素个数);
        sol_count++;             // sol_count 加一
        return;                  // return;
    }
    for (int row = 0; row < n; row++) { // 让 row 从 0 开始计数，row 小于 元素个数 就继续
        int d1 = col - row + (n - 1);   // 把 col 减 row 加 (元素个数 减 1) 存入 d1
        int d2 = col + row;             // 把 col 加 row 存入 d2
        if (st.rows[row] && st.diag1[d1] && st.diag2[d2]) { // 若 st.行数[row] 且 st.diag1[d1] 且 st.diag2[d2]
            State ns = st;
                /* 值拷贝 = 不可变语义 */ // 把 st; 除以 乘 值拷贝 赋值为 不可变语义 乘 除以 写入 State ns
            ns.col_row[col] = row; // 把 row; 写入 ns.col_row[col]
            ns.rows[row] = 0;      // 把 0; 写入 ns.rows[row]
            ns.diag1[d1] = 0;      // 把 0; 写入 ns.diag1[d1]
            ns.diag2[d2] = 0;      // 把 0; 写入 ns.diag2[d2]
            place(col + 1, n, ns); // place(col 加 1, 元素个数, ns);
        }
    }
}

static int n_queens_func(int n) {          // 定义函数/方法 n_queens_func
    State init;                            // State init;
    memset(&init, 0, sizeof(init));        // memset( 按位与 init, 0, sizeof(init));
    memset(init.rows, 1, sizeof(int) * n); // memset(init.行数, 1, sizeof(int) 乘 元素个数);
    memset(init.diag1, 1,
           sizeof(int) * (2 * n - 1)); // memset(init.diag1, 1, sizeof(int) 乘 (2 乘 元素个数 减 1));
    memset(init.diag2, 1,
           sizeof(int) * (2 * n - 1)); // memset(init.diag2, 1, sizeof(int) 乘 (2 乘 元素个数 减 1));
    sol_count = 0;                     // 把 0; 写入 sol_count
    place(0, n, init);                 // place(0, 元素个数, init);
    return sol_count;                  // 返回 sol_count
}

int main(void) { // 程序入口：跑内嵌自测用例
    struct {
        int n;
        int count;
        int has_first;
        int first[8];
    } cases[] = {
        {8, 92, 1, {0, 4, 7, 5, 2, 6, 1, 3}},
        {1, 1, 1, {0}},
        {2, 0, 0, {0}},
        {4, 2, 1, {1, 3, 0, 2}},
    };
    for (int idx = 0; idx < 4; idx++) {          // 让 idx 从 0 开始计数，idx 小于 4 就继续
        int count = n_queens_func(cases[idx].n); // 把 n_queens_func(cases[idx].元素个数) 存入 计数
        if (count != cases[idx].count) {
            printf("case %d count %d\n", idx, count);
            return 1;
        }
        if (cases[idx].has_first) { // 若 cases[idx].has_first
            for (int j = 0; j < cases[idx].n;
                 j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 cases[idx].元素个数 就继续
                if (sols[0][j] != cases[idx].first[j]) {
                    printf("case %d first\n", idx);
                    return 1;
                }
            }
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
