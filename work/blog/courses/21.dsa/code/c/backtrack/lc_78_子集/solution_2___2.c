/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134109616 */
/* LeetCode 78. 子集 — C 版（方案2） */
#include <stdio.h> // 引入头文件
static int res[256][8], res_lens[256], res_n, nums_g[8],
    n_g;                                // static int 结果[256][8], res_lens[256], res_n, nums_g[8], n_g;
static void dfs(int start, int depth) { // 定义函数/方法 dfs
    for (int i = 0; i < depth; i++)
        res[res_n][i] = nums_g[i];      // 让 下标 i 从 0 开始计数，下标 i 小于 深度 就继续
    res_lens[res_n] = depth;            // 把 深度; 写入 res_lens[res_n]
    res_n++;                            // res_n 加一
    for (int i = start; i < n_g; i++) { // 让 下标 i 从 起点 开始计数，下标 i 小于 n_g 就继续
        nums_g[depth] = res[res_n - 1][depth] /* placeholder */; // 把 结果[res_n 减 1][深度] 除以 乘
                                                                 // placeholder 乘 除以 ; 写入 nums_g[depth]
        /* 使用 path 数组单独维护 */
        break; // 跳出循环
    }
}
/* 重写：path 与 nums 分开 */
static int path[8];                      // static int 当前路径[8];
static void dfs2(int start, int depth) { // 定义函数/方法 dfs2
    for (int i = 0; i < depth; i++)
        res[res_n][i] = path[i];        // 让 下标 i 从 0 开始计数，下标 i 小于 深度 就继续
    res_lens[res_n] = depth;            // 把 深度; 写入 res_lens[res_n]
    res_n++;                            // res_n 加一
    for (int i = start; i < n_g; i++) { // 让 下标 i 从 起点 开始计数，下标 i 小于 n_g 就继续
        path[depth] = nums_g[i];        // 把 nums_g[下标 i]; 写入 path[depth]
        dfs2(i + 1, depth + 1);         // dfs2(下标 i 加 1, 深度 加 1);
    }
}
static int subsets(const int *nums, int n) { // 定义函数/方法 subsets
    n_g = n;
    res_n = 0; // 把 元素个数; res_n 赋值为 0; 写入 n_g
    for (int i = 0; i < n; i++)
        nums_g[i] = nums[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    dfs2(0, 0);              // dfs2(0, 0);
    return res_n;            // 返回 res_n
}
int main(void) {                          // 程序入口：跑内嵌自测用例
    int n = subsets((int[]){1, 2, 3}, 3); // 把 subsets((int[]){1,2,3}, 3) 存入 元素个数
    if (n != 8) {
        printf("FAIL cnt=%d\n", n);
        return 1;
    } // 若 元素个数 不等于 8) { 输出「FAIL 计数 赋值为 对…取模 d 」, 元素个数); return 1; }
    if (subsets((int[]){0}, 1) != 2) {
        printf("FAIL 2\n");
        return 1;
    }                 // 若 subsets((int[]){0}, 1) 不等于 2) { 输出「FAIL 2 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
