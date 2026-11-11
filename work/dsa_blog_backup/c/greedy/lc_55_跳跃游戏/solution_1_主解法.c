/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133844403 */
/* LeetCode 55. 跳跃游戏 — C 版（方案1） */
#include <stdio.h>                            // 引入头文件
static int can_jump(const int *nums, int n) { // 定义函数/方法 can_jump
    int max_reach = 0;                        // 把 0 存入 max_reach
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        if (i > max_reach)
            return 0; // 若 下标 i 超过 max_reach，直接返回 0
        if (i + nums[i] > max_reach)
            max_reach = i + nums[i];
    }
    return 1; // 返回 1
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (!can_jump((int[]){2, 3, 1, 1, 4}, 5)) {
        printf("FAIL 1\n");
        return 1;
    }
    if (can_jump((int[]){3, 2, 1, 0, 4}, 5)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
