/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397311 */
/* LeetCode 面试题 03.05. 栈排序 — C 版（方案1） */
#include <stdio.h>                                            // 引入头文件
static int sorted_stack(const int *input, int n, int out[]) { // 定义函数/方法 sorted_stack
    int stk[4096], sn = 0;                                    // 把 0; 写入 int stk[4096], sn
    int temp[4096], tn = 0;                                   // 把 0; 写入 int temp[4096], tn
    for (int i = 0; i < n; i++)
        stk[sn++] = input[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    int on = 0;               // 把 0 存入 on
    while (sn > 0) {          // 循环，直到不满足「sn 超过 0」
        int v = stk[--sn];    // 把 栈[ 减一 sn] 存入 值
        while (tn > 0 && temp[tn - 1] > v)
            out[on++] = temp[--tn];
        temp[tn++] = v; // 把 值; 写入 temp[tn++]
    }
    while (tn > 0)
        out[on++] = temp[--tn]; // 循环，直到不满足「tn 超过 0) out[on 加一 ] 赋值为 临时变量[ 减一 tn];」
    /* 升序排 */
    for (int i = 0; i < on; i++)
        for (int j = i + 1; j < on; j++) { // 让 下标 i 从 0 开始计数，下标 i 小于 on 就继续
            if (out[i] > out[j]) {
                int t = out[i];
                out[i] = out[j];
                out[j] = t;
            }
        }
    return on; // 返回 on
}
int main(void) { // 程序入口：跑内嵌自测用例
    int out[4096], n = sorted_stack((int[]){5, 2, 1, 4, 3}, 5, out);
    if (n != 5 || !(out[0] == 1 && out[1] == 2 && out[2] == 3 && out[3] == 4 && out[4] == 5)) {
        printf("FAIL\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS