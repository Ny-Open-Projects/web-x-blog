/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134134491 */
/* LeetCode 47. 全排列II — C 版（方案1） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static int res[720][8], res_n, used[8], path[8], arr_g[8], n_g;
static void dfs(int depth) { // 定义函数/方法 dfs
    if (depth == n_g) {      // 若 深度 等于 n_g
        for (int i = 0; i < n_g; i++)
            res[res_n][i] = path[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 n_g 就继续
        res_n++;                     // res_n 加一
        return;                      // return;
    }
    for (int i = 0; i < n_g; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 n_g 就继续
        if (used[i])
            continue; // 若 已用标记[下标 i]) continue;
        if (i > 0 && arr_g[i] == arr_g[i - 1] && !used[i - 1])
            continue;
        used[i] = 1;            // 把 1; 写入 used[i]
        path[depth] = arr_g[i]; // 把 arr_g[下标 i]; 写入 path[depth]
        dfs(depth + 1);         // dfs(深度 加 1);
        used[i] = 0;            // 把 0; 写入 used[i]
    }
}
static int permute_unique(const int *nums, int n) { // 定义函数/方法 permute_unique
    n_g = n;
    res_n = 0; // 把 元素个数; res_n 赋值为 0; 写入 n_g
    for (int i = 0; i < n; i++) {
        arr_g[i] = nums[i];
        used[i] = 0;
    } // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    qsort(arr_g, n, sizeof(int), cmp_int); // qsort(arr_g, 元素个数, sizeof(int), cmp_int);
    dfs(0);                                // dfs(0);
    return res_n;                          // 返回 res_n
}
int main(void) {                                 // 程序入口：跑内嵌自测用例
    int n = permute_unique((int[]){1, 1, 2}, 3); // 把 permute_unique((int[]){1,1,2}, 3) 存入 元素个数
    if (n != 3) {
        printf("FAIL cnt=%d\n", n);
        return 1;
    } // 若 元素个数 不等于 3) { 输出「FAIL 计数 赋值为 对…取模 d 」, 元素个数); return 1; }
    if (res[0][0] != 1 || res[0][1] != 1 || res[0][2] != 2) {
        printf("FAIL p1\n");
        return 1;
    }
    if (res[1][0] != 1 || res[1][1] != 2 || res[1][2] != 1) {
        printf("FAIL p2\n");
        return 1;
    }
    if (res[2][0] != 2 || res[2][1] != 1 || res[2][2] != 1) {
        printf("FAIL p3\n");
        return 1;
    }
    if (permute_unique((int[]){1, 2, 3}, 3) != 6) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
