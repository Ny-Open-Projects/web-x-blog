/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734875 */
/* LeetCode 682. 棒球比赛 — C 版（方案2） */
#include <stdio.h>                               // 引入头文件
#include <stdlib.h>                              // 引入头文件
#include <string.h>                              // 引入头文件
static int cal_points(const char **ops, int n) { // 定义函数/方法 cal_points
    int st[4096];                                // int st[4096];
    int top = 0;                                 // 把 0 存入 top
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        if (strcmp(ops[i], "+") == 0) {          // 若 strcmp(ops[下标 i], 「 加 」) 等于 0
            st[top] = st[top - 1] + st[top - 2]; // 把 st[top 减 1] 加 st[top 减 2]; 写入 st[top]
            top++;                               // top 加一
        } else if (strcmp(ops[i], "D") == 0) {   // 否则，若 strcmp(ops[下标 i], 「D」) 等于 0
            st[top] = st[top - 1] * 2;           // 把 st[top 减 1] 乘 2; 写入 st[top]
            top++;                               // top 加一
        } else if (strcmp(ops[i], "C") == 0) {   // 否则，若 strcmp(ops[下标 i], 「C」) 等于 0
            top--;                               // top 减一
        } else {                                 // 否则
            st[top++] = atoi(ops[i]);            // 把 atoi(ops[下标 i]); 写入 st[top++]
        }
    }
    int sum = 0; // 把 0 存入 累计和
    for (int i = 0; i < top; i++)
        sum += st[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 top 就继续
    return sum;       // 返回 累计和
}
int main(void) {                                  // 程序入口：跑内嵌自测用例
    const char *t1[] = {"5", "2", "C", "D", "+"}; // 把 {「5」,「5」,「5」,「5」,「5」}; 写入 const char *t1[]
    const char *t2[] = {
        "5", "-2", "4", "C",
        "D", "9",  "+", "+"}; // 把 {「5」,「5」,「5」,「5」,「5」,「5」,「5」,「5」}; 写入 const char *t2[]
    const char *t3[] = {"1", "C"}; // 把 {「1」,「1」}; 写入 const char *t3[]
    if (cal_points(t1, 5) != 30) {
        printf("FAIL 1\n");
        return 1;
    } // 若 cal_points(t1, 5) 不等于 30) { 输出「FAIL 1 」); return 1; }
    if (cal_points(t2, 8) != 27) {
        printf("FAIL 2\n");
        return 1;
    } // 若 cal_points(t2, 8) 不等于 27) { 输出「FAIL 2 」); return 1; }
    if (cal_points(t3, 2) != 0) {
        printf("FAIL 3\n");
        return 1;
    } // 若 cal_points(t3, 2) 不等于 0) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS