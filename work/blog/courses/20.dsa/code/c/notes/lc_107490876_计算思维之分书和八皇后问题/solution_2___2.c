/* 来源：https://blog.csdn.net/tyro_java/article/details/107490876
 * LeetCode 107490876. 分书和八皇后问题 — C 版（方案2：分书，函数式不可变副本）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

static const int LIKE[5][5] = {
    // 把 { 写入 static const int LIKE[5][5]
    {0, 0, 1, 1, 0}, {1, 1, 0, 0, 1}, {0, 1, 1, 0, 1}, {0, 0, 0, 1, 0}, {0, 1, 0, 0, 1},
};

static int results[16][5];   // static int results[16][5];
static int result_count = 0; // 把 0; 写入 static int result_count

static void try_assign(int reader, const int assigned[5]) { // 定义函数/方法 try_assign
    if (reader == 5) {                                      // 若 reader 等于 5
        memcpy(results[result_count], assigned,
               sizeof(int) * 5); // memcpy(results[result_count], assigned, sizeof(int) 乘 5);
        result_count++;          // result_count 加一
        return;                  // return;
    }
    for (int book = 0; book < 5; book++) { // 让 book 从 0 开始计数，book 小于 5 就继续
        if (LIKE[reader][book] == 1 &&
            assigned[book] == -1) { // 若 LIKE[reader][book] 等于 1 且 assigned[book] 等于 减 1
            int nxt[5];             // int nxt[5];
            memcpy(nxt, assigned, sizeof(int) * 5); // memcpy(nxt, assigned, sizeof(int) 乘 5);
            nxt[book] = reader;                     // 把 reader; 写入 nxt[book]
            try_assign(reader + 1, nxt);            // try_assign(reader 加 1, nxt);
        }
    }
}

int main(void) { // 程序入口：跑内嵌自测用例
    int want[2][5] = {{1, 2, 0, 3, 4},
                      {1, 4, 0, 3, 2}}; // 把 {{1, 2, 0, 3, 4}, {1, 4, 0, 3, 2}}; 写入 int want[2][5]
    int init[5] = {-1, -1, -1, -1, -1}; // 把 { 减 1, 减 1, 减 1, 减 1, 减 1}; 写入 int init[5]
    try_assign(0, init);                // try_assign(0, init);
    if (result_count != 2) {
        printf("count mismatch\n");
        return 1;
    }                           // 若 result_count 不等于 2) { 输出「计数 mismatch 」); return 1; }
    for (int i = 0; i < 2; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 2 就继续
        for (int j = 0; j < 5; j++) // 让 下标 j 从 0 开始计数，下标 j 小于 5 就继续
            if (results[i][j] != want[i][j]) {
                printf("scheme %d mismatch\n", i);
                return 1;
            }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
