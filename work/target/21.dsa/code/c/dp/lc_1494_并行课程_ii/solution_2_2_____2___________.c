/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134859412 */
/* LeetCode 1494. 并行课程II — C 版（方案2） */
#include <stdio.h>                 // 引入头文件
static int n_g, k_g, prereq_g[16]; // static int n_g, k_g, prereq_g[16];
static int go(int done) {          // 定义函数/方法 go
    if (done == (1 << n_g) - 1)
        return 0;                   // 若 done 等于 (1 小于 小于 n_g) 减 1，直接返回 0
    int avail = 0;                  // 把 0 存入 avail
    for (int i = 0; i < n_g; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 n_g 就继续
        if (!(done & (1 << i)) && (done & prereq_g[i]) == prereq_g[i])
            avail |= 1 << i;
    }
    int cnt = 0, chosen = 0, a = avail; // 把 0, chosen 赋值为 0, 数组 赋值为 avail 存入 计数
    while (a && cnt < k_g) {            // 循环，直到不满足「数组 且 计数 小于 k_g」
        int low = a & (-a);             // 把 数组 按位与 ( 减 数组) 存入 low
        chosen |= low;                  // 把 low; 写入 chosen |
        a ^= low;                       // 把 low; 写入 a ^
        cnt++;                          // 计数 加一
    }
    return 1 + go(done | chosen); // 返回 1 加 go(done 按位或 chosen)
}
static int min_number_of_semesters(int n, int relations[][2], int nr,
                                   int k) { // 定义函数/方法 min_number_of_semesters
    n_g = n;
    k_g = k; // 把 元素个数; k_g 赋值为 下标 k; 写入 n_g
    for (int i = 0; i < n; i++)
        prereq_g[i] = 0; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (int i = 0; i < nr; i++)
        prereq_g[relations[i][1] - 1] |=
            1 << (relations[i][0] - 1); // 让 下标 i 从 0 开始计数，下标 i 小于 nr 就继续
    return go(0);                       // 返回 go(0)
}
int main(void) {                            // 程序入口：跑内嵌自测用例
    int r1[][2] = {{2, 1}, {3, 1}, {1, 4}}; // 把 {{2,1},{3,1},{1,4}}; 写入 int r1[][2]
    if (min_number_of_semesters(4, r1, 3, 2) != 3) {
        printf("FAIL 1\n");
        return 1;
    }
    int r2[][2] = {{2, 1}, {3, 1}, {4, 1}, {1, 5}}; // 把 {{2,1},{3,1},{4,1},{1,5}}; 写入 int r2[][2]
    if (min_number_of_semesters(5, r2, 4, 3) != 3) {
        printf("FAIL 2\n");
        return 1;
    }
    if (min_number_of_semesters(3, r1, 0, 2) != 2) {
        printf("FAIL 3\n");
        return 1;
    }
    int r4[][2] = {{1, 2}, {2, 3}}; // 把 {{1,2},{2,3}}; 写入 int r4[][2]
    if (min_number_of_semesters(4, r4, 2, 1) != 4) {
        printf("FAIL 4\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS