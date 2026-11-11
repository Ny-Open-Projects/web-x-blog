/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135167617 */
/* LeetCode 860. 柠檬水找零 — C 版（方案6） */
#include <stdio.h>                                    // 引入头文件
static int lemonade_change(const int *bills, int n) { // 定义函数/方法 lemonade_change
    int f5 = 0, f10 = 0;                              // 把 0, f10 赋值为 0 存入 f5
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        if (bills[i] == 5)
            f5++; // 若 bills[下标 i] 等于 5) f5 加一 ;
        else if (bills[i] == 10) {
            f10++;
            f5--;
        }      // 否则，若 bills[下标 i] 等于 10) { f10 加一 ; f5 减一 ; }
        else { // 否则
            if (f10 > 0) {
                f10--;
                f5--;
            } else
                f5 -= 3; // 若 f10 超过 0) { f10 减一 ; f5 减一 ; } else f5 累减 3;
        }
        if (f5 < 0)
            return 0; // 若 f5 小于 0，直接返回 0
    }
    return 1; // 返回 1
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (!lemonade_change((int[]){5, 5, 5, 10, 20}, 5)) {
        printf("FAIL 1\n");
        return 1;
    }
    if (lemonade_change((int[]){5, 5, 10, 10, 20}, 5)) {
        printf("FAIL 2\n");
        return 1;
    }
    if (!lemonade_change((int[]){5, 5, 5, 5, 20}, 5)) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
