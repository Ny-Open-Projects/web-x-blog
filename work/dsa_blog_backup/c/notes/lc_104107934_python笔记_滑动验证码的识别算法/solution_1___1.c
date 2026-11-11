/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
 * LeetCode 104107934. 滑动验证码识别 — C 版（方案1：前向差分边缘 + 匹配）
 */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件

static void detect_edges(const int *image, int n, int *edges) { // 定义函数/方法 detect_edges
    for (int i = 0; i < n; i++)
        edges[i] = 0; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (int i = 1; i < n; i++)
        edges[i] = abs(image[i] - image[i - 1]) > 50; // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
}

static int recognize_captcha(const int *bg, int bn, const int *puzzle,
                             int pn) {      // 定义函数/方法 recognize_captcha
    int bg_edges[64], puzzle_edges[64];     // int bg_edges[64], puzzle_edges[64];
    detect_edges(bg, bn, bg_edges);         // detect_edges(bg, bn, bg_edges);
    detect_edges(puzzle, pn, puzzle_edges); // detect_edges(puzzle, pn, puzzle_edges);
    int best_x = 0;                         // 把 0 存入 best_x
    long best_score = -1;                   // 把 减 1; 写入 long best_score
    for (int x = 0; x <= bn - pn; x++) {    // 让 x 从 0 开始计数，x 不超过 bn 减 pn 就继续
        long score = 0;                     // 把 0; 写入 long score
        for (int y = 0; y < pn; y++)        // 让 y 从 0 开始计数，y 小于 pn 就继续
            if (bg_edges[x + y] && puzzle_edges[y])
                score++; // 若 bg_edges[x 加 y] 且 puzzle_edges[y]) score 加一 ;
        if (score > best_score) {
            best_score = score;
            best_x = x;
        }
    }
    return best_x; // 返回 best_x
}

int main(void) { // 程序入口：跑内嵌自测用例
    int bg[8] = {10,  10,  10,  10,
                 200, 200, 200, 200};    // 把 {10, 10, 10, 10, 200, 200, 200, 200}; 写入 int bg[8]
    int puzzle[4] = {10, 200, 200, 200}; // 把 {10, 200, 200, 200}; 写入 int puzzle[4]
    if (recognize_captcha(bg, 8, puzzle, 4) != 3) {
        printf("gap failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
