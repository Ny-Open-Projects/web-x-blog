/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107836586
 * LeetCode 107836586. Big-O 记号 — C 版（Big-O 记号：按最高次非零系数给出多项式复杂度分类）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

/* coeffs[i] 为 n^i 的系数，deg_count 为个数 */
static void classify(const long long *coeffs, int deg_count, char *out,
                     int out_size) {                 // 定义函数/方法 classify
    for (int deg = deg_count - 1; deg >= 0; deg--) { // 让 deg 从 deg_count 减 1 开始计数，deg 不低于 0 就继续
        if (coeffs[deg] != 0) {                      // 若 coeffs[deg] 不等于 0
            if (deg > 1)
                snprintf(out, out_size, "O(n^%d)", deg);
            else if (deg == 1)
                snprintf(out, out_size,
                         "O(n)"); // 否则，若 deg 等于 1) snprintf(out, out_size, 「O(元素个数)」);
            else
                snprintf(out, out_size, "O(1)"); // 否则
            return;                              // return;
        }
    }
    snprintf(out, out_size, "O(1)"); // 打印输出
}

int main(void) {                     // 程序入口：跑内嵌自测用例
    long long c0[4] = {1, 0, 0, 0};  // 把 {1, 0, 0, 0}; 写入 long long c0[4]
    long long c1[4] = {0, 0, 0, 35}; // 把 {0, 0, 0, 35}; 写入 long long c1[4]
    long long c2[4] = {0, 0, 1, 0};  // 把 {0, 0, 1, 0}; 写入 long long c2[4]
    long long c3[4] = {0, 1, 0, 0};  // 把 {0, 1, 0, 0}; 写入 long long c3[4]
    const char *wants[4] = {"O(1)", "O(n^3)", "O(n^2)",
                            "O(n)"}; // 把 {「O(1)」, 「O(1)」, 「O(1)」, 「O(1)」}; 写入 const char *wants[4]
    long long *as[4] = {c0, c1, c2, c3};      // 把 {c0, c1, c2, c3}; 写入 long long *as[4]
    char got[32];                             // char got[32];
    for (int i = 0; i < 4; i++) {             // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
        classify(as[i], 4, got, sizeof(got)); // classify(as[下标 i], 4, got, sizeof(got));
        if (strcmp(got, wants[i]) != 0) {     // 若 strcmp(got, wants[下标 i]) 不等于 0
            printf("case %d failed: got %s want %s\n", i, got, wants[i]); // 打印输出
            return 1;                                                     // 返回 1
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
