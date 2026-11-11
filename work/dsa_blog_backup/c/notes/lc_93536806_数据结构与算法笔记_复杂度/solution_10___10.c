/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806 */
/* 数据结构与算法笔记: 复杂度 — C 版（方案10） */
#include <stdio.h>              // 引入头文件
static long func_calls(int n) { // 定义函数/方法 func_calls
    if (n <= 1)
        return 1;                 // 若 元素个数 不超过 1，直接返回 1
    return 2 * func_calls(n - 1); // 返回 2 乘 func_calls(元素个数 减 1)
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (func_calls(1) != 1 || func_calls(2) != 2 || func_calls(5) != 16 || func_calls(10) != 512) {
        printf("FAIL\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS