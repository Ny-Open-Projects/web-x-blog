/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133531071 */
/* LeetCode 169. 多数元素 — C 版（方案1） */
#include <stdio.h>                                   // 引入头文件
static int majority_element(const int *n, int len) { // 定义函数/方法 majority_element
    int counts[65536] = {0};                         // 把 {0}; 写入 int counts[65536]
    int best = n[0], bn = 0;        // 把 元素个数[0], bn 赋值为 0 存入 当前最优
    for (int i = 0; i < len; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
        int idx = n[i] + 32768;     // 把 元素个数[下标 i] 加 32768 存入 idx
        counts[idx]++;              // counts[idx] 加一 ;
        if (counts[idx] > bn) {
            bn = counts[idx];
            best = n[i];
        }
    }
    return best; // 返回 当前最优
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (majority_element((int[]){3, 2, 3}, 3) != 3) {
        printf("FAIL 1\n");
        return 1;
    }
    if (majority_element((int[]){2, 2, 1, 1, 1, 2, 2}, 7) != 2) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS