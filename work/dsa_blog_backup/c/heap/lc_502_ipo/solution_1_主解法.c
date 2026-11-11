/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136847926 */
/* LeetCode 502. IPO — C 版（方案1） */
#include <stdio.h> // 引入头文件
static long find_maximized_capital(int k, long w, const long *profits, const long *capital,
                                   int n) { // 定义函数/方法 find_maximized_capital
    int used[64] = {0};                     // 把 {0}; 写入 int used[64]
    for (int t = 0; t < k; t++) { // 让 另一字符串 从 0 开始计数，另一字符串 小于 下标 k 就继续
        long best = -1;           // 把 减 1; 写入 long best
        int best_j = -1;          // 把 减 1 存入 best_j
        for (int j = 0; j < n; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
            if (!used[j] && capital[j] <= w && profits[j] > best) {
                best = profits[j];
                best_j = j;
            }
        }
        if (best_j < 0)
            break;        // 若 best_j 小于 0) break;
        w += best;        // 权重累加 当前最优
        used[best_j] = 1; // 把 1; 写入 used[best_j]
    }
    return w; // 返回 权重
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (find_maximized_capital(2, 0, (long[]){1, 2, 3}, (long[]){0, 1, 1}, 3) != 4) {
        printf("FAIL 1\n");
        return 1;
    }
    if (find_maximized_capital(3, 0, (long[]){1, 2, 3}, (long[]){0, 1, 2}, 3) != 6) {
        printf("FAIL 2\n");
        return 1;
    }
    if (find_maximized_capital(1, 0, (long[]){1, 2}, (long[]){1, 2}, 2) != 0) {
        printf("FAIL 3\n");
        return 1;
    }
    if (find_maximized_capital(2, 1, (long[]){1, 2, 3}, (long[]){1, 1, 2}, 3) != 6) {
        printf("FAIL 4\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
