/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400 */
/* LeetCode 347. 前K个高频元素 — C 版（方案2） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
typedef struct {
    int v;
    long c;
} VC;                                             // typedef struct { int 值; long 字符; } VC;
static int cmp_vc(const void *a, const void *b) { // 定义函数/方法 cmp_vc
    const VC *x = a, *y = b;                      // 把 数组, 乘 y 赋值为 b; 写入 const VC *x
    if (x->c != y->c)
        return (x->c > y->c) ? -1 : 1;
    return x->v - y->v; // 返回 x 减 超过 值 减 y 减 超过 值
}
static int top_k_frequent(const int *nums, int n, int k, int out[]) { // 定义函数/方法 top_k_frequent
    VC vcs[4096];                                                     // VC vcs[4096];
    int m = 0;                                                        // 把 0 存入 映射表
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        int found = 0;            // 把 0 存入 found
        for (int j = 0; j < m; j++)
            if (vcs[j].v == nums[i]) {
                vcs[j].c++;
                found = 1;
                break;
            } // 让 下标 j 从 0 开始计数，下标 j 小于 映射表 就继续
        if (!found) {
            vcs[m].v = nums[i];
            vcs[m].c = 1;
            m++;
        }
    }
    qsort(vcs, m, sizeof(VC), cmp_vc); // qsort(vcs, 映射表, sizeof(VC), cmp_vc);
    for (int i = 0; i < k && i < m; i++)
        out[i] = vcs[i].v; // 让 下标 i 从 0 开始计数，下标 i 小于 下标 k 且 下标 i 小于 映射表 就继续
    return k < m ? k : m; // 返回 下标 k 小于 映射表 ? 下标 k : 映射表
}
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
int main(void) {    // 程序入口：跑内嵌自测用例
    int out[64], n; // int out[64], 元素个数;
    n = top_k_frequent((int[]){1, 1, 1, 2, 2, 3}, 6, 2,
                       out); // 把 top_k_frequent((int[]){1,1,1,2,2,3}, 6, 2, out); 写入 元素个数
    qsort(out, n, sizeof(int), cmp_int); // qsort(out, 元素个数, sizeof(int), cmp_int);
    if (n != 2 || out[0] != 1 || out[1] != 2) {
        printf("FAIL 1\n");
        return 1;
    }
    n = top_k_frequent((int[]){1}, 1, 1, out); // 把 top_k_frequent((int[]){1}, 1, 1, out); 写入 元素个数
    if (n != 1 || out[0] != 1) {
        printf("FAIL 2\n");
        return 1;
    } // 若 元素个数 不等于 1 或 out[0] 不等于 1) { 输出「FAIL 2 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
