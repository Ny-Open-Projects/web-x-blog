/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130671359 */
/* LeetCode 337. 打家劫舍III — C 版（方案1） */
#include <stdio.h>                           // 引入头文件
#define NN (-2147483647 - 1) /* null 哨兵 */ // #define NN ( 减 2147483647 减 1) 除以 乘 null 哨兵 乘 除以
static void dfs(const int *vals, int n, int i, long *inc, long *exc) { // 定义函数/方法 dfs
    if (i >= n || vals[i] == NN) {
        *inc = 0;
        *exc = 0;
        return;
    }
    long li, le, ri, re;               // long li, le, ri, re;
    dfs(vals, n, 2 * i + 1, &li, &le); // dfs(vals, 元素个数, 2 乘 下标 i 加 1, 按位与 li, 按位与 le);
    dfs(vals, n, 2 * i + 2, &ri, &re); // dfs(vals, 元素个数, 2 乘 下标 i 加 2, 按位与 ri, 按位与 re);
    *inc = vals[i] + le + re;
    long lm = li > le ? li : le; // 把 li 超过 le ? li : le; 写入 long lm
    long rm = ri > re ? ri : re; // 把 ri 超过 re ? ri : re; 写入 long rm
    *exc = lm + rm;
}
static int rob_tree(const int *vals, int n) { // 定义函数/方法 rob_tree
    long inc, exc;                            // long inc, exc;
    dfs(vals, n, 0, &inc, &exc);              // dfs(vals, 元素个数, 0, 按位与 inc, 按位与 exc);
    return (int)(inc > exc ? inc : exc);      // 返回 (int)(inc 超过 exc ? inc : exc)
}
int main(void) {                        // 程序入口：跑内嵌自测用例
    int t1[] = {3, 2, 3, NN, 3, NN, 1}; // 把 {3,2,3,NN,3,NN,1}; 写入 int t1[]
    if (rob_tree(t1, 7) != 7) {
        printf("FAIL 1\n");
        return 1;
    }                                  // 若 rob_tree(t1, 7) 不等于 7) { 输出「FAIL 1 」); return 1; }
    int t2[] = {3, 4, 5, 1, 3, NN, 1}; // 把 {3,4,5,1,3,NN,1}; 写入 int t2[]
    if (rob_tree(t2, 7) != 9) {
        printf("FAIL 2\n");
        return 1;
    } // 若 rob_tree(t2, 7) 不等于 9) { 输出「FAIL 2 」); return 1; }
    if (rob_tree(t2, 0) != 0) {
        printf("FAIL 3\n");
        return 1;
    } // 若 rob_tree(t2, 0) 不等于 0) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS