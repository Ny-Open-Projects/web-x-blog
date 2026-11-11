/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145045460 */
/* LeetCode 503. 下一个更大元素 II — C 版（方案1） */
#include <stdio.h>                                                     // 引入头文件
static void next_greater_elements(const int *nums, int n, int out[]) { // 定义函数/方法 next_greater_elements
    for (int i = 0; i < n; i++)
        out[i] = -1;       // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    int st[8192], top = 0; // 把 0; 写入 int st[8192], top
    for (int i = 0; i < 2 * n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 2 乘 元素个数 就继续
        int ii = i % n;               // 把 下标 i 对…取模 元素个数 存入 ii
        while (top > 0 &&
               nums[st[top - 1]] <
                   nums[ii]) { // 循环，直到不满足「top 超过 0 且 数组[st[top 减 1]] 小于 数组[ii]」
            out[st[top - 1]] = nums[ii]; // 把 数组[ii]; 写入 out[st[top - 1]]
            top--;                       // top 减一
        }
        if (i < n)
            st[top++] = ii; // 若 下标 i 小于 元素个数) st[top 加一 ] 赋值为 ii;
    }
}
int main(void) {                                     // 程序入口：跑内嵌自测用例
    int out[8192];                                   // int out[8192];
    next_greater_elements((int[]){1, 2, 1}, 3, out); // next_greater_elements((int[]){1,2,1}, 3, out);
    if (!(out[0] == 2 && out[1] == -1 && out[2] == 2)) {
        printf("FAIL 1\n");
        return 1;
    }
    next_greater_elements((int[]){3, 2, 1}, 3, out); // next_greater_elements((int[]){3,2,1}, 3, out);
    if (!(out[0] == -1 && out[1] == 3 && out[2] == 3)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS