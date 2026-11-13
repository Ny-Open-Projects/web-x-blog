/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134638462 */
/* LeetCode 605. 种花问题 — C 版（方案1） */
#include <stdio.h>                                             // 引入头文件
static int can_place_flowers(const int *bed, int len, int n) { // 定义函数/方法 can_place_flowers
    int v[4096];                                               // int 值[4096];
    for (int i = 0; i < len; i++)
        v[i] = bed[i];              // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
    int count = 0;                  // 把 0 存入 计数
    for (int i = 0; i < len; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
        if (v[i] == 0 && (i == 0 || v[i - 1] == 0) && (i == len - 1 || v[i + 1] == 0)) {
            v[i] = 1; // 把 1; 写入 v[i]
            count++;  // 计数 加一
        }
    }
    return count >= n; // 返回 计数 不低于 元素个数
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (!can_place_flowers((int[]){1, 0, 0, 0, 1}, 5, 1)) {
        printf("FAIL 1\n");
        return 1;
    }
    if (can_place_flowers((int[]){1, 0, 0, 0, 1}, 5, 2)) {
        printf("FAIL 2\n");
        return 1;
    }
    if (!can_place_flowers((int[]){0, 0, 1, 0, 0}, 5, 1)) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS