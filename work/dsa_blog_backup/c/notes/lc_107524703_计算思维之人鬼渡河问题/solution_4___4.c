/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
 * LeetCode 107524703. 人鬼渡河问题 — C 版（方案4：方向入状态的 DFS 变体，断言无可行路径）
 */
#include <stdio.h> // 引入头文件

static const int D[5][2] = {{2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}};
static int path[32][2];  // static int 当前路径[32][2];
static int path_len = 0; // 把 0; 写入 static int path_len
static int visited_r[64], visited_g[64], visited_p[64], visited_n = 0;

static int safe(int r, int g) { // 定义函数/方法 safe
    return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

static int is_visited(int r, int g, int parity) { // 定义判定函数 is_visited
    for (int i = 0; i < visited_n; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 visited_n 就继续
        if (visited_r[i] == r && visited_g[i] == g && visited_p[i] == parity)
            return 1;
    return 0; // 返回 0
}

static void mark(int r, int g, int parity) { // 定义函数/方法 mark
    visited_r[visited_n] = r;
    visited_g[visited_n] = g;
    visited_p[visited_n] = parity;
    visited_n++; // visited_n 加一
}

static int jump(int dir, int r, int g, int step) { // 定义函数/方法 jump
    if (r == 0 && g == 0 && step % 2 == 0)
        return 1; // 若 右指针 等于 0 且 g 等于 0 且 步数 对…取模 2 等于 0，直接返回 1
    int parity = step % 2; // 把 步数 对…取模 2 存入 parity
    if (is_visited(r, g, parity))
        return 0;                       // 若 is_visited(右指针, g, parity)，直接返回 0
    mark(r, g, parity);                 // mark(右指针, g, parity);
    for (int i = 0; i < 5; i++) {       // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
        int dr = D[i][0], dg = D[i][1]; // 把 D[下标 i][0], dg 赋值为 D[下标 i][1] 存入 dr
        int nr = r + dir * dr;          // 把 右指针 加 dir 乘 dr 存入 nr
        int ng = g + dir * dg;          // 把 g 加 dir 乘 dg 存入 ng
        if (!safe(nr, ng))
            continue;                       // 若 取反 safe(nr, ng)) continue;
        if (jump(-dir, nr, ng, step + 1)) { // 若 jump( 减 dir, nr, ng, 步数 加 1
            path[path_len][0] = dr;
            path[path_len][1] = dg; // 把 dr; 当前路径[path_len][1] 赋值为 dg; 写入 path[path_len][0]
            path_len++;             // path_len 加一
            return 1;               // 返回 1
        }
    }
    return 0; // 返回 0
}

int main(void) {       // 程序入口：跑内嵌自测用例
    jump(-1, 3, 3, 0); // jump( 减 1, 3, 3, 0);
    /* 与 TS 原文件一致：该变体断言返回空路径（parity 约束下无解） */
    if (path_len != 0) {
        printf("FAIL: got %d moves\n", path_len);
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
