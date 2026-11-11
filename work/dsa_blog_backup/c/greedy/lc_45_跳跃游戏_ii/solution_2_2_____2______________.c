/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133911745 */
/* LeetCode 45. 跳跃游戏II — C 版（方案2） */
#include <stdio.h>                        // 引入头文件
static int jump(const int *nums, int n) { // 定义函数/方法 jump
    int position = n - 1, steps = 0;      // 把 元素个数 减 1, steps 赋值为 0 存入 position
    while (position > 0) {                // 循环，直到不满足「position 超过 0」
        for (int i = 0; i < position; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 position 就继续
            if (i + nums[i] >= position) {
                position = i;
                steps++;
                break;
            }
        }
    }
    return steps; // 返回 steps
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (jump((int[]){2, 3, 1, 1, 4}, 5) != 2) {
        printf("FAIL 1\n");
        return 1;
    }
    if (jump((int[]){2, 3, 0, 1, 4}, 5) != 2) {
        printf("FAIL 2\n");
        return 1;
    }
    if (jump((int[]){1}, 1) != 0) {
        printf("FAIL 3\n");
        return 1;
    }                 // 若 jump((int[]){1}, 1) 不等于 0) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
