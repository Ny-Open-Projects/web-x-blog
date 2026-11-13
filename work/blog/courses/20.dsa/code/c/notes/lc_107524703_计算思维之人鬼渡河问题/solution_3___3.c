/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
 * LeetCode 107524703. 人鬼渡河问题 — C 版（方案3：DFS+奇偶步求解）
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

static int dfs(int r, int g, int step) { // 定义函数/方法 dfs
    if (r == 0 && g == 0)
        return 1;          // 若 右指针 等于 0 且 g 等于 0，直接返回 1
    int parity = step % 2; // 把 步数 对…取模 2 存入 parity
    if (is_visited(r, g, parity))
        return 0;                       // 若 is_visited(右指针, g, parity)，直接返回 0
    mark(r, g, parity);                 // mark(右指针, g, parity);
    int odd = (step % 2 == 1);          // 把 (步数 对…取模 2 等于 1) 存入 odd
    for (int i = 0; i < 5; i++) {       // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
        int dr = D[i][0], dg = D[i][1]; // 把 D[下标 i][0], dg 赋值为 D[下标 i][1] 存入 dr
        int nr, ng;                     // int nr, ng;
        if (odd) {                      // 若 odd
            if (r < dr || g < dg)
                continue; // 若 右指针 小于 dr 或 g 小于 dg) continue;
            nr = r - dr;
            ng = g - dg; // 把 右指针 减 dr; ng 赋值为 g 减 dg; 写入 nr
        } else {         // 否则
            if ((3 - r) < dr || (3 - g) < dg)
                continue; // 若 (3 减 右指针) 小于 dr 或 (3 减 g) 小于 dg) continue;
            nr = r + dr;
            ng = g + dg; // 把 右指针 加 dr; ng 赋值为 g 加 dg; 写入 nr
        }
        if (!safe(nr, ng))
            continue;                // 若 取反 safe(nr, ng)) continue;
        if (dfs(nr, ng, step + 1)) { // 若 dfs(nr, ng, 步数 加 1
            path[path_len][0] = dr;
            path[path_len][1] = dg; // 把 dr; 当前路径[path_len][1] 赋值为 dg; 写入 path[path_len][0]
            path_len++;             // path_len 加一
            return 1;               // 返回 1
        }
    }
    return 0; // 返回 0
}

int main(void) { // 程序入口：跑内嵌自测用例
    int want[11][2] = {
        // 把 { 写入 int want[11][2]
        {1, 1}, {1, 0}, {0, 2}, {0, 1}, {2, 0}, {1, 1}, {2, 0}, {0, 1}, {0, 2}, {1, 0}, {1, 1},
    };
    dfs(3, 3, 1); // dfs(3, 3, 1);
    if (path_len != 11) {
        printf("solve length mismatch: %d\n", path_len);
        return 1;
    }
    for (int i = 0; i < 11; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 11 就继续
        /* path 逆序存放 */
        if (path[10 - i][0] != want[i][0] || path[10 - i][1] != want[i][1]) {
            printf("solve at %d mismatch\n", i); // 打印输出
            return 1;                            // 返回 1
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
