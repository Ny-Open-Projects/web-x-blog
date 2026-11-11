/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134055742 */
/* LeetCode 283. 移动零 — C 版（方案1） */
#include <stdio.h>                          // 引入头文件
static void move_zeroes(int n[], int len) { // 定义函数/方法 move_zeroes
    int pos = 0;                            // 把 0 存入 pos
    for (int i = 0; i < len; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
        if (n[i] != 0) {
            int t = n[pos];
            n[pos] = n[i];
            n[i] = t;
            pos++;
        }
    }
}
int main(void) {                 // 程序入口：跑内嵌自测用例
    int v1[] = {0, 1, 0, 3, 12}; // 把 {0,1,0,3,12}; 写入 int v1[]
    move_zeroes(v1, 5);          // move_zeroes(v1, 5);
    if (!(v1[0] == 1 && v1[1] == 3 && v1[2] == 12 && v1[3] == 0 && v1[4] == 0)) {
        printf("FAIL 1\n");
        return 1;
    }
    int v2[] = {0};     // 把 {0}; 写入 int v2[]
    move_zeroes(v2, 1); // move_zeroes(v2, 1);
    if (v2[0] != 0) {
        printf("FAIL 2\n");
        return 1;
    } // 若 v2[0] 不等于 0) { 输出「FAIL 2 」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS