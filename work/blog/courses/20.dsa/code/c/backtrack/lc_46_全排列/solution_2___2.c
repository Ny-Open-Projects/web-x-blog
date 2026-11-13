/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133767953 */
/* LeetCode 46. 全排列 — C 版（方案2） */
#include <stdio.h> // 引入头文件
static int res[720][8], res_n, used[8], path[8], nums_g[8], n_g;
static void dfs(int depth) { // 定义函数/方法 dfs
    if (depth == n_g) {      // 若 深度 等于 n_g
        for (int i = 0; i < n_g; i++)
            res[res_n][i] = path[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 n_g 就继续
        res_n++;                     // res_n 加一
        return;                      // return;
    }
    for (int i = 0; i < n_g; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 n_g 就继续
        if (used[i])
            continue;            // 若 已用标记[下标 i]) continue;
        used[i] = 1;             // 把 1; 写入 used[i]
        path[depth] = nums_g[i]; // 把 nums_g[下标 i]; 写入 path[depth]
        dfs(depth + 1);          // dfs(深度 加 1);
        used[i] = 0;             // 把 0; 写入 used[i]
    }
}
static int permute(const int *nums, int n) { // 定义函数/方法 permute
    n_g = n;
    res_n = 0; // 把 元素个数; res_n 赋值为 0; 写入 n_g
    for (int i = 0; i < n; i++) {
        nums_g[i] = nums[i];
        used[i] = 0;
    }             // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    dfs(0);       // dfs(0);
    return res_n; // 返回 res_n
}
int main(void) {                          // 程序入口：跑内嵌自测用例
    int n = permute((int[]){1, 2, 3}, 3); // 把 permute((int[]){1,2,3}, 3) 存入 元素个数
    int w1[] = {1, 2, 3}, w2[] = {1, 3, 2}, w3[] = {2, 1, 3}, w6[] = {3, 2, 1};
    if (n != 6) {
        printf("FAIL cnt\n");
        return 1;
    }                             // 若 元素个数 不等于 6) { 输出「FAIL 计数 」); return 1; }
    for (int i = 0; i < 3; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 3 就继续
        if (res[0][i] != w1[i] || res[1][i] != w2[i] || res[2][i] != w3[i] || res[5][i] != w6[i]) {
            printf("FAIL perm\n");
            return 1;
        }
    }
    if (permute((int[]){0, 1}, 2) != 2) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
