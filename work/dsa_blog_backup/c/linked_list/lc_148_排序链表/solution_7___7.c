/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133904873 */
/* LeetCode 148. 排序链表 — C 版（方案7） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static void sort_list(int v[], int n) { // 定义函数/方法 sort_list
    qsort(v, n, sizeof(int), cmp_int);  // qsort(值, 元素个数, sizeof(int), cmp_int);
}
int main(void) {             // 程序入口：跑内嵌自测用例
    int v1[] = {4, 2, 1, 3}; // 把 {4,2,1,3}; 写入 int v1[]
    sort_list(v1, 4);        // sort_list(v1, 4);
    if (!(v1[0] == 1 && v1[1] == 2 && v1[2] == 3 && v1[3] == 4)) {
        printf("FAIL 1\n");
        return 1;
    }
    int v2[] = {-1, 5, 3, 4, 0}; // 把 { 减 1,5,3,4,0}; 写入 int v2[]
    sort_list(v2, 5);            // sort_list(v2, 5);
    if (!(v2[0] == -1 && v2[1] == 0 && v2[2] == 3 && v2[3] == 4 && v2[4] == 5)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
