/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134773756 */
/* LeetCode 75. 颜色分类 — C 版（方案2） */
#include <stdio.h>                          // 引入头文件
static void sort_colors(int n[], int len) { // 定义函数/方法 sort_colors
    int p0 = 0, cur = 0, p2 = len - 1; // 把 0, 当前值 赋值为 0, p2 赋值为 长度 减 1 存入 p0
    while (cur <= p2) {                // 循环，直到不满足「当前值 不超过 p2」
        if (n[cur] == 0) {
            int t = n[p0];
            n[p0] = n[cur];
            n[cur] = t;
            p0++;
            cur++;
        } else if (n[cur] == 2) {
            int t = n[cur];
            n[cur] = n[p2];
            n[p2] = t;
            p2--;
        } else
            cur++; // 否则
    }
}
int main(void) {                   // 程序入口：跑内嵌自测用例
    int v1[] = {2, 0, 2, 1, 1, 0}; // 把 {2,0,2,1,1,0}; 写入 int v1[]
    sort_colors(v1, 6);            // sort_colors(v1, 6);
    if (!(v1[0] == 0 && v1[1] == 0 && v1[2] == 1 && v1[5] == 2)) {
        printf("FAIL 1\n");
        return 1;
    }
    int v2[] = {2, 0, 1}; // 把 {2,0,1}; 写入 int v2[]
    sort_colors(v2, 3);   // sort_colors(v2, 3);
    if (!(v2[0] == 0 && v2[1] == 1 && v2[2] == 2)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS