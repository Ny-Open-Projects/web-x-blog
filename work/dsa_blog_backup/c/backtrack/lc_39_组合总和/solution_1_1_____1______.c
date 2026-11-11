/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133865307 */
/* LeetCode 39. 组合总和 — C 版（方案1） */
#include <stdio.h> // 引入头文件
static int res[256][32], res_lens[256], res_n,
    path[32];                 // static int 结果[256][32], res_lens[256], res_n, 当前路径[32];
static int cands_g[32], nc_g; // static int cands_g[32], nc_g;
static void dfs(int start, int remaining, int depth) { // 定义函数/方法 dfs
    if (remaining == 0) {                              // 若 remaining 等于 0
        for (int i = 0; i < depth; i++)
            res[res_n][i] = path[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 深度 就继续
        res_lens[res_n] = depth;     // 把 深度; 写入 res_lens[res_n]
        res_n++;                     // res_n 加一
        return;                      // return;
    }
    if (remaining < 0)
        return;                          // 若 remaining 小于 0) return;
    for (int i = start; i < nc_g; i++) { // 让 下标 i 从 起点 开始计数，下标 i 小于 nc_g 就继续
        path[depth] = cands_g[i];        // 把 cands_g[下标 i]; 写入 path[depth]
        dfs(i, remaining - cands_g[i], depth + 1); // dfs(下标 i, remaining 减 cands_g[下标 i], 深度 加 1);
    }
}
static int combination_sum(const int *candidates, int nc, int target) { // 定义函数/方法 combination_sum
    nc_g = nc;
    res_n = 0; // 把 nc; res_n 赋值为 0; 写入 nc_g
    for (int i = 0; i < nc; i++)
        cands_g[i] = candidates[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 nc 就继续
    dfs(0, target, 0);              // dfs(0, 目标值, 0);
    return res_n;                   // 返回 res_n
}
int main(void) { // 程序入口：跑内嵌自测用例
    int n = combination_sum((int[]){2, 3, 6, 7}, 4,
                            7); // 把 combination_sum((int[]){2,3,6,7}, 4, 7) 存入 元素个数
    if (n != 2) {
        printf("FAIL cnt=%d\n", n);
        return 1;
    } // 若 元素个数 不等于 2) { 输出「FAIL 计数 赋值为 对…取模 d 」, 元素个数); return 1; }
    if (res_lens[0] != 3 || res[0][0] != 2 || res[0][1] != 2 || res[0][2] != 3) {
        printf("FAIL a\n");
        return 1;
    }
    if (res_lens[1] != 1 || res[1][0] != 7) {
        printf("FAIL b\n");
        return 1;
    }
    if (combination_sum((int[]){2, 3, 5}, 3, 8) != 3) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
