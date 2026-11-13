/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133524779 */
/* LeetCode 167. 两数之和II — C 版（方案1） */
#include <stdio.h>                                                   // 引入头文件
static void two_sum(const int *n, int len, int target, int out[2]) { // 定义函数/方法 two_sum
    int l = 0, r = len - 1;  // 把 0, 右指针 赋值为 长度 减 1 存入 左指针
    while (l < r) {          // 循环，直到不满足「左指针 小于 右指针」
        int s = n[l] + n[r]; // 把 元素个数[左指针] 加 元素个数[右指针] 存入 字符串
        if (s == target) {
            out[0] = l + 1;
            out[1] = r + 1;
            return;
        }
        if (s < target)
            l++;
        else
            r--; // 若 字符串 小于 目标值) 左指针 加一 ; else 右指针 减一 ;
    }
    out[0] = out[1] = 0; // 把 out[1] 赋值为 0; 写入 out[0]
}
int main(void) {                               // 程序入口：跑内嵌自测用例
    int out[2];                                // int out[2];
    two_sum((int[]){2, 7, 11, 15}, 4, 9, out); // two_sum((int[]){2,7,11,15}, 4, 9, out);
    if (out[0] != 1 || out[1] != 2) {
        printf("FAIL 1\n");
        return 1;
    } // 若 out[0] 不等于 1 或 out[1] 不等于 2) { 输出「FAIL 1 」); return 1; }
    two_sum((int[]){2, 3, 4}, 3, 6, out); // two_sum((int[]){2,3,4}, 3, 6, out);
    if (out[0] != 1 || out[1] != 3) {
        printf("FAIL 2\n");
        return 1;
    } // 若 out[0] 不等于 1 或 out[1] 不等于 3) { 输出「FAIL 2 」); return 1; }
    two_sum((int[]){-1, 0}, 2, -1, out); // two_sum((int[]){ 减 1,0}, 2, 减 1, out);
    if (out[0] != 1 || out[1] != 2) {
        printf("FAIL 3\n");
        return 1;
    } // 若 out[0] 不等于 1 或 out[1] 不等于 2) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS