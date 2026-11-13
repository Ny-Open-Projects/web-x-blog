/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134178290 */
/* LeetCode 77. 组合 — C 版（方案3） */
#include <stdio.h>                      // 引入头文件
static int res[256][8], res_n, path[8]; // static int 结果[256][8], res_n, 当前路径[8];
static int n_g, k_g;                    // static int n_g, k_g;
static void dfs(int start, int depth) { // 定义函数/方法 dfs
    if (depth == k_g) {                 // 若 深度 等于 k_g
        for (int i = 0; i < depth; i++)
            res[res_n][i] = path[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 深度 就继续
        res_n++;                     // res_n 加一
        return;                      // return;
    }
    for (int i = start; i <= n_g - (k_g - depth) + 1;
         i++) { // 让 下标 i 从 起点 开始计数，下标 i 不超过 n_g 减 (k_g 减 深度) 加 1 就继续
        path[depth] = i;       // 把 下标 i; 写入 path[depth]
        dfs(i + 1, depth + 1); // dfs(下标 i 加 1, 深度 加 1);
    }
}
static int combine(int n, int k) { // 定义函数/方法 combine
    n_g = n;
    k_g = k;
    res_n = 0;    // 把 元素个数; k_g 赋值为 下标 k; res_n 赋值为 0; 写入 n_g
    dfs(1, 0);    // dfs(1, 0);
    return res_n; // 返回 res_n
}
int main(void) {           // 程序入口：跑内嵌自测用例
    int n = combine(4, 2); // 把 combine(4, 2) 存入 元素个数
    if (n != 6) {
        printf("FAIL cnt\n");
        return 1;
    } // 若 元素个数 不等于 6) { 输出「FAIL 计数 」); return 1; }
    if (res[0][0] != 1 || res[0][1] != 2 || res[5][0] != 3 || res[5][1] != 4) {
        printf("FAIL c\n");
        return 1;
    }
    if (combine(1, 1) != 1) {
        printf("FAIL 2\n");
        return 1;
    }                 // 若 combine(1, 1) 不等于 1) { 输出「FAIL 2 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
