/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757 */
/* 栈排序分析 — C 版（方案1） */
#include <stdio.h>                                        // 引入头文件
static void stack_sort(const int *in, int n, int out[]) { // 定义函数/方法 stack_sort
    int st[4096];                                         // int st[4096];
    int top = 0;                                          // 把 0 存入 top
    for (int i = 0; i < n; i++)
        st[top++] = in[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (int i = 0; i < n; i++)
        out[i] = st[--top]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
}
int main(void) {                                // 程序入口：跑内嵌自测用例
    int out[64];                                // int out[64];
    stack_sort((int[]){3, 1, 5, 2, 4}, 5, out); // stack_sort((int[]){3,1,5,2,4}, 5, out);
    int w[] = {4, 2, 5, 1, 3};                  // 把 {4,2,5,1,3}; 写入 int w[]
    for (int i = 0; i < 5; i++)
        if (out[i] != w[i]) {
            printf("FAIL\n");
            return 1;
        } // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS