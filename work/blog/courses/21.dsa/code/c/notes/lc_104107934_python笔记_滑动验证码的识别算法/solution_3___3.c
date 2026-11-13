/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
 * LeetCode 104107934. 滑动验证码识别 — C 版（方案3：NCC 归一化互相关）
 */
#include <math.h>  // 引入头文件
#include <stdio.h> // 引入头文件

static int ncc_match(const int *bg, int bn, const int *puzzle, int pn) { // 定义函数/方法 ncc_match
    int best_x = 0;                                                      // 把 0 存入 best_x
    double best_score = -1.0 / 0.0;      // 把 减 1.0 除以 0.0 存入 best_score
    for (int x = 0; x <= bn - pn; x++) { // 让 x 从 0 开始计数，x 不超过 bn 减 pn 就继续
        double bw = 0, pw = 0;           // 把 0, pw 赋值为 0 存入 bw
        for (int i = 0; i < pn; i++) {   // 让 下标 i 从 0 开始计数，下标 i 小于 pn 就继续
            bw += bg[x + i];             // bw累加 bg[x 加 下标 i]
            pw += puzzle[i];             // pw累加 puzzle[下标 i]
        }
        bw /= pn;                       // 把 pn; 写入 bw /
        pw /= pn;                       // 把 pn; 写入 pw /
        double num = 0, db = 0, dp = 0; // 把 0, db 赋值为 0, DP 表 赋值为 0 存入 num
        for (int i = 0; i < pn; i++) {  // 让 下标 i 从 0 开始计数，下标 i 小于 pn 就继续
            double a = bg[x + i] - bw;  // 把 bg[x 加 下标 i] 减 bw 存入 数组
            double b = puzzle[i] - pw;  // 把 puzzle[下标 i] 减 pw 存入 b
            num += a * b;               // num累加 数组 乘 b
            db += a * a;                // db累加 数组 乘 数组
            dp += b * b;                // DP 表累加 b 乘 b
        }
        double denom = sqrt(db) * sqrt(dp); // 把 sqrt(db) 乘 sqrt(DP 表) 存入 denom
        double score =
            (denom != 0.0) ? (num / denom) : 0.0; // 把 (denom 不等于 0.0) ? (num 除以 denom) : 0.0 存入 score
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
    if (ncc_match(bg, 8, puzzle, 4) != 3) {
        printf("gap failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
