/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145398097 */
/* LeetCode 2637. 有时间限制的Promise对象 — C 版（方案1） */
#include <stdio.h> // 引入头文件
/* resolved=1 表示按时完成 val 有效；resolved=0 超时 → -1 */
static void promise_time_limit(const int *vals, const int *resolved, int n,
                               int out[]) { // 定义函数/方法 promise_time_limit
    for (int i = 0; i < n; i++)
        out[i] = resolved[i] ? vals[i] : -1; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
}
int main(void) {                                // 程序入口：跑内嵌自测用例
    int out[8];                                 // int out[8];
    int vals[] = {5, 0, 9};                     // 把 {5, 0, 9}; 写入 int vals[]
    int resolved[] = {1, 0, 1};                 // 把 {1, 0, 1}; 写入 int resolved[]
    promise_time_limit(vals, resolved, 3, out); // promise_time_limit(vals, resolved, 3, out);
    if (out[0] != 5 || out[1] != -1 || out[2] != 9) {
        printf("FAIL\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS