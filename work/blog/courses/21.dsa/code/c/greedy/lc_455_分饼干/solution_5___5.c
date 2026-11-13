/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135096603 */
/* LeetCode 455. 分发饼干 — C 版（方案5） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static int find_content_children(int *g, int ng, int *s, int ns) { // 定义函数/方法 find_content_children
    qsort(g, ng, sizeof(int), cmp_int);                            // qsort(g, ng, sizeof(int), cmp_int);
    qsort(s, ns, sizeof(int), cmp_int); // qsort(字符串, ns, sizeof(int), cmp_int);
    int child = 0, cookie = 0;          // 把 0, cookie 赋值为 0 存入 子节点
    while (child < ng && cookie < ns) { // 循环，直到不满足「子节点 小于 ng 且 cookie 小于 ns」
        if (s[cookie] >= g[child])
            child++; // 若 字符串[cookie] 不低于 g[子节点]) 子节点 加一 ;
        cookie++;    // cookie 加一
    }
    return child; // 返回 子节点
}
int main(void) {                         // 程序入口：跑内嵌自测用例
    int g1[] = {1, 2, 3}, s1[] = {1, 1}; // 把 {1,2,3}, s1[] 赋值为 {1,1}; 写入 int g1[]
    int g2[] = {1, 2}, s2[] = {1, 2, 3}; // 把 {1,2}, s2[] 赋值为 {1,2,3}; 写入 int g2[]
    if (find_content_children(g1, 3, s1, 2) != 1) {
        printf("FAIL 1\n");
        return 1;
    }
    if (find_content_children(g2, 2, s2, 3) != 2) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
