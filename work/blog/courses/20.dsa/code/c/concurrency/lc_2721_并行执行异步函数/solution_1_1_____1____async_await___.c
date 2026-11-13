/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386399 */
/* LeetCode 2721. 并行执行异步函数 — C 版（方案1） */
#include <stdio.h>                                          // 引入头文件
static void execute_all(const int *fns, int n, int out[]) { // 定义函数/方法 execute_all
    for (int i = 0; i < n; i++)
        out[i] = fns[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
}
int main(void) {             // 程序入口：跑内嵌自测用例
    int out[8];              // int out[8];
    int in[] = {1, 2, 3};    // 把 {1,2,3}; 写入 int in[]
    execute_all(in, 3, out); // execute_all(in, 3, out);
    for (int i = 0; i < 3; i++)
        if (out[i] != i + 1) {
            printf("FAIL\n");
            return 1;
        } // 让 下标 i 从 0 开始计数，下标 i 小于 3 就继续
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS