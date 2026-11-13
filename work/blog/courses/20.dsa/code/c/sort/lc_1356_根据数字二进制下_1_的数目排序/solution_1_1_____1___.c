/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138671078 */
/* LeetCode 1356. 根据数字二进制下1的数目排序 — C 版（方案1） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
static int count_bits(int n) {
    int c = 0;
    while (n) {
        c += n & 1;
        n >>= 1;
    }
    return c;
}
static int cmp_bits(const void *a, const void *b) { // 定义函数/方法 cmp_bits
    int x = *(const int *)a,
        y = *(const int *)b; // 把 乘 (const int 乘 )数组, y 赋值为 乘 (const int 乘 )b 存入 x
    int bx = count_bits(x), by = count_bits(y); // 把 count_bits(x), by 赋值为 count_bits(y) 存入 bx
    if (bx != by)
        return bx - by; // 若 bx 不等于 by，直接返回 bx 减 by
    return x - y;       // 返回 x 减 y
}
static void sort_by_bits(const int *nums, int n, int out[]) { // 定义函数/方法 sort_by_bits
    for (int i = 0; i < n; i++)
        out[i] = nums[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    qsort(out, n, sizeof(int), cmp_bits); // qsort(out, 元素个数, sizeof(int), cmp_bits);
}
int main(void) {                           // 程序入口：跑内嵌自测用例
    int out[64];                           // int out[64];
    int w[] = {0, 1, 2, 4, 8, 3, 5, 6, 7}; // 把 {0,1,2,4,8,3,5,6,7}; 写入 int w[]
    sort_by_bits((int[]){0, 1, 2, 3, 4, 5, 6, 7, 8}, 9,
                 out); // sort_by_bits((int[]){0,1,2,3,4,5,6,7,8}, 9, out);
    for (int i = 0; i < 9; i++)
        if (out[i] != w[i]) {
            printf("FAIL %d\n", i);
            return 1;
        }             // 让 下标 i 从 0 开始计数，下标 i 小于 9 就继续
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
