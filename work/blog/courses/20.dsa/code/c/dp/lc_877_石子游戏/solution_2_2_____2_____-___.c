/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130709323 */
/* LeetCode 877. 石子游戏 — C 版（方案2） */
#include <stdio.h> // 引入头文件
static int stone_game(const int *piles, int n) {
    (void)piles;
    (void)n;
    return 1;
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (!stone_game((int[]){5, 3, 4, 5}, 4)) {
        printf("FAIL 1\n");
        return 1;
    }
    if (!stone_game((int[]){3, 7, 2, 3}, 4)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS