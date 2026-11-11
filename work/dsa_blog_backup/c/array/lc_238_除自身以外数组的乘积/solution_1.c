/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133907522 */
/* LeetCode 238. 除自身以外数组的乘积 — C 版（方案1） */
#include <stdio.h>                                                  // 引入头文件
static void product_except_self(const int *n, int len, int out[]) { // 定义函数/方法 product_except_self
    long left = 1;                                                  // 把 1; 写入 long left
    for (int i = 0; i < len; i++) {
        out[i] = (int)left;
        left *= n[i];
    }               // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
    long right = 1; // 把 1; 写入 long right
    for (int i = len - 1; i >= 0; i--) {
        out[i] = (int)(out[i] * right);
        right *= n[i];
    } // 让 下标 i 从 长度 减 1 开始计数，下标 i 不低于 0 就继续
}
int main(void) {                                      // 程序入口：跑内嵌自测用例
    int out[8];                                       // int out[8];
    product_except_self((int[]){1, 2, 3, 4}, 4, out); // product_except_self((int[]){1,2,3,4}, 4, out);
    if (!(out[0] == 24 && out[1] == 12 && out[2] == 8 && out[3] == 6)) {
        printf("FAIL 1\n");
        return 1;
    }
    product_except_self((int[]){-1, 1, 0, -3, 3}, 5,
                        out); // product_except_self((int[]){ 减 1,1,0, 减 3,3}, 5, out);
    if (!(out[0] == 0 && out[2] == 9)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS