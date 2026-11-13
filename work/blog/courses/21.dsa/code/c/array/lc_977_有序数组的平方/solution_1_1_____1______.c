/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134982348 */
/* LeetCode 977. 有序数组的平方 — C 版（方案1） */
#include <stdio.h>                                             // 引入头文件
#include <stdlib.h>                                            // 引入头文件
static void sorted_squares(const int *n, int len, int out[]) { // 定义函数/方法 sorted_squares
    int l = 0, r = len - 1, idx = len - 1; // 把 0, 右指针 赋值为 长度 减 1, idx 赋值为 长度 减 1 存入 左指针
    while (l <= r) {                       // 循环，直到不满足「左指针 不超过 右指针」
        long a = labs(n[l]),
             b = labs(n[r]); // 把 labs(元素个数[左指针]), b 赋值为 labs(元素个数[右指针]); 写入 long a
        if (a > b) {
            out[idx--] = (int)(a * a);
            l++;
        } // 若 数组 超过 b) { out[idx 减一 ] 赋值为 (int)(数组 乘 数组); 左指针 加一 ; }
        else {
            out[idx--] = (int)(b * b);
            r--;
        } // 否则
    }
}
int main(void) {                                       // 程序入口：跑内嵌自测用例
    int out[4096];                                     // int out[4096];
    sorted_squares((int[]){-4, -1, 0, 3, 10}, 5, out); // sorted_squares((int[]){ 减 4, 减 1,0,3,10}, 5, out);
    if (!(out[0] == 0 && out[1] == 1 && out[4] == 100)) {
        printf("FAIL 1\n");
        return 1;
    }
    sorted_squares((int[]){-7, -3, 2, 3, 11}, 5, out); // sorted_squares((int[]){ 减 7, 减 3,2,3,11}, 5, out);
    if (!(out[0] == 4 && out[4] == 121)) {
        printf("FAIL 2\n");
        return 1;
    }
    sorted_squares((int[]){1, 2, 3}, 3, out); // sorted_squares((int[]){1,2,3}, 3, out);
    if (!(out[0] == 1 && out[2] == 9)) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS