/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133982215
 * LeetCode 417. 太平洋大西洋水流问题 — C 版 */
#include <stdbool.h> // 引入头文件
#include <stdio.h>   // 引入头文件
#include <string.h>  // 引入头文件

#define MAXD 8 // #define MAXD 8

static int g_m, g_n;             // static int g_m, g_n;
static const int (*g_mat)[MAXD]; // static const int ( 乘 g_mat)[MAXD];

/* 方案1（DFS 反向流动，从海洋边界出发） */
static void dfs(int r, int c, bool flow[MAXD][MAXD]) { // 定义函数/方法 dfs
    flow[r][c] = true;                                 // 把 true; 写入 flow[r][c]
    static const int dr[4] = {-1, 1, 0, 0};            // 把 { 减 1, 1, 0, 0}; 写入 static const int dr[4]
    static const int dc[4] = {0, 0, -1, 1};            // 把 {0, 0, 减 1, 1}; 写入 static const int dc[4]
    for (int k = 0; k < 4; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 4 就继续
        int nr = r + dr[k];       // 把 右指针 加 dr[下标 k] 存入 nr
        int nc = c + dc[k];       // 把 字符 加 dc[下标 k] 存入 nc
        if (nr >= 0 && nr < g_m && nc >= 0 && nc < g_n && !flow[nr][nc] &&
            g_mat[nr][nc] >= g_mat[r][c]) { // 把 g_mat[右指针][字符]) { 写入 g_mat[nr][nc] >
            dfs(nr, nc, flow);              // dfs(nr, nc, flow);
        }
    }
}

/* 返回结果个数，res 按行优先填充 0 基坐标；mat 为 NULL 时返回 0 */
static int pacific_atlantic(const int (*mat)[MAXD], int m, int n,
                            int res[][2]) { // int 结果[][2]) {
    if (mat == NULL || m == 0 || n == 0)
        return 0; // 若 mat 等于 NULL 或 映射表 等于 0 或 元素个数 等于 0，直接返回 0
    g_m = m;      // 把 映射表; 写入 g_m
    g_n = n;      // 把 元素个数; 写入 g_n
    g_mat = mat;  // 把 mat; 写入 g_mat
    static bool pacific[MAXD][MAXD],
        atlantic[MAXD][MAXD];              // static bool pacific[MAXD][MAXD], atlantic[MAXD][MAXD];
    memset(pacific, 0, sizeof(pacific));   // memset(pacific, 0, sizeof(pacific));
    memset(atlantic, 0, sizeof(atlantic)); // memset(atlantic, 0, sizeof(atlantic));
    for (int r = 0; r < m; r++) { // 让 右指针 从 0 开始计数，右指针 小于 映射表 就继续
        dfs(r, 0, pacific);       // dfs(右指针, 0, pacific);
        dfs(r, n - 1, atlantic);  // dfs(右指针, 元素个数 减 1, atlantic);
    }
    for (int c = 0; c < n; c++) { // 让 字符 从 0 开始计数，字符 小于 元素个数 就继续
        dfs(0, c, pacific);       // dfs(0, 字符, pacific);
        dfs(m - 1, c, atlantic);  // dfs(映射表 减 1, 字符, atlantic);
    }
    int cnt = 0;                  // 把 0 存入 计数
    for (int r = 0; r < m; r++) { // 让 右指针 从 0 开始计数，右指针 小于 映射表 就继续
        for (int c = 0; c < n; c++) { // 让 字符 从 0 开始计数，字符 小于 元素个数 就继续
            if (pacific[r][c] && atlantic[r][c]) { // 若 pacific[右指针][字符] 且 atlantic[右指针][字符]
                res[cnt][0] = r;                   // 把 右指针; 写入 res[cnt][0]
                res[cnt][1] = c;                   // 把 字符; 写入 res[cnt][1]
                cnt++;                             // 计数 加一
            }
        }
    }
    return cnt; // 返回 计数
}

int main(void) { // 程序入口：跑内嵌自测用例
    /* 空输入：null 矩阵应返回 [] */
    int res[MAXD][2];                            // int 结果[MAXD][2];
    int got = pacific_atlantic(NULL, 5, 5, res); // 把 pacific_atlantic(NULL, 5, 5, 结果) 存入 got
    if (got != 0) {                              // 若 got 不等于 0
        printf("null matrix should yield []\n"); // 打印输出
        return 1;                                // 返回 1
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
