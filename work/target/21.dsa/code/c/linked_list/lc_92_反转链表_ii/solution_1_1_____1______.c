/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133657416 */
/* LeetCode 92. 反转链表II — C 版（方案1） */
#include <stdio.h>                                                 // 引入头文件
static void reverse_between(int v[], int n, int left, int right) { // 定义函数/方法 reverse_between
    int l = left - 1, r = right - 1; // 把 左边界 减 1, 右指针 赋值为 右边界 减 1 存入 左指针
    while (l < r) {                  // 循环，直到不满足「左指针 小于 右指针」
        int t = v[l];
        v[l] = v[r];
        v[r] = t; // 把 值[左指针]; 值[左指针] 赋值为 值[右指针]; 值[右指针] 赋值为 另一字符串 存入 另一字符串
        l++;
        r--; // 左指针 加一 ; 右指针 减一 ;
    }
}
int main(void) {                  // 程序入口：跑内嵌自测用例
    int v1[] = {1, 2, 3, 4, 5};   // 把 {1,2,3,4,5}; 写入 int v1[]
    reverse_between(v1, 5, 2, 4); // reverse_between(v1, 5, 2, 4);
    if (!(v1[0] == 1 && v1[1] == 4 && v1[2] == 3 && v1[3] == 2 && v1[4] == 5)) {
        printf("FAIL 1\n");
        return 1;
    }
    int v2[] = {1, 2, 3, 4, 5};   // 把 {1,2,3,4,5}; 写入 int v2[]
    reverse_between(v2, 5, 1, 4); // reverse_between(v2, 5, 1, 4);
    if (!(v2[0] == 4 && v2[1] == 3 && v2[2] == 2 && v2[3] == 1 && v2[4] == 5)) {
        printf("FAIL 2\n");
        return 1;
    }
    int v3[] = {5};               // 把 {5}; 写入 int v3[]
    reverse_between(v3, 1, 1, 1); // reverse_between(v3, 1, 1, 1);
    if (v3[0] != 5) {
        printf("FAIL 3\n");
        return 1;
    }                 // 若 v3[0] 不等于 5) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
