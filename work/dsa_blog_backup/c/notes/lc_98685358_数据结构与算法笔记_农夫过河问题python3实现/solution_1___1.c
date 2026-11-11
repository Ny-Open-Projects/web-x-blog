/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/98685358
 * LeetCode 98685358. 农夫过河问题 — C 版（农夫过河问题：BFS 求最短过河序列，状态 (农夫,狼,羊,菜)，0=左岸
 * 1=右岸） 状态编码为 4bit 整数：bit3=农夫 bit2=狼 bit1=羊 bit0=菜
 */
#include <stdio.h> // 引入头文件

static int is_safe(int s) { // 定义判定函数 is_safe
    int farmer = (s >> 3) & 1, wolf = (s >> 2) & 1, goat = (s >> 1) & 1, cabbage = s & 1;
    if (wolf == goat && farmer != wolf)
        return 0; // 若 wolf 等于 goat 且 farmer 不等于 wolf，直接返回 0
    if (goat == cabbage && farmer != goat)
        return 0; // 若 goat 等于 cabbage 且 farmer 不等于 goat，直接返回 0
    return 1;     // 返回 1
}

static void dec(int s, int out[4]) { // 定义函数/方法 dec
    out[0] = (s >> 3) & 1;
    out[1] = (s >> 2) & 1;
    out[2] = (s >> 1) & 1;
    out[3] = s & 1;
}

static int enc(int v[4]) {                        // 定义函数/方法 enc
    return v[0] * 8 + v[1] * 4 + v[2] * 2 + v[3]; // 返回 值[0] 乘 8 加 值[1] 乘 4 加 值[2] 乘 2 加 值[3]
}

static int solve(int path[][4]) { // 定义函数/方法 solve
    int start = 0, goal = 15;     // 把 0, goal 赋值为 15 存入 起点
    int prev[16];                 // int 前一个[16];
    for (int i = 0; i < 16; i++)
        prev[i] = -2; /* -2 未访问, -1 起点 */ // 让 下标 i 从 0 开始计数，下标 i 小于 16 就继续
    int q[16], head = 0, tail = 0;             // 把 0, 尾节点 赋值为 0; 写入 int q[16], head
    prev[start] = -1;                          // 把 减 1; 写入 prev[start]
    q[tail++] = start;                         // 把 起点; 写入 q[tail++]
    while (head < tail) {                      // 循环，直到不满足「头节点 小于 尾节点」
        int cur = q[head++];                   // 把 节点[头节点 加一 ] 存入 当前值
        if (cur == goal) {                     // 若 当前值 等于 goal
            int n = 0, tmp[16];                // 把 0, 临时变量[16] 存入 元素个数
            int k = cur;                       // 把 当前值 存入 下标 k
            while (k != -1) {
                tmp[n++] = k;
                k = prev[k];
            }
            for (int i = 0; i < n; i++)
                dec(tmp[n - 1 - i], path[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
            return n;                         // 返回 元素个数
        }
        int farmer = (cur >> 3) & 1;  // 把 (当前值 超过 超过 3) 按位与 1 存入 farmer
        for (int i = 0; i < 4; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
            if (i != 0 && ((cur >> (3 - i)) & 1) != farmer)
                continue;
            int v[4];          // int 值[4];
            dec(cur, v);       // dec(当前值, 值);
            v[0] = 1 - farmer; // 把 1 减 farmer; 写入 v[0]
            if (i != 0)
                v[i] = 1 - farmer; // 若 下标 i 不等于 0) 值[下标 i] 赋值为 1 减 farmer;
            int nk = enc(v);       // 把 enc(值) 存入 nk
            if (prev[nk] != -2)
                continue; // 若 前一个[nk] 不等于 减 2) continue;
            if (!is_safe(nk))
                continue;   // 若 取反 is_safe(nk)) continue;
            prev[nk] = cur; // 把 当前值; 写入 prev[nk]
            q[tail++] = nk; // 把 nk; 写入 q[tail++]
        }
    }
    return -1; // 返回 减 1
}

int main(void) { // 程序入口：跑内嵌自测用例
    int want[8][4] = {
        // 把 { 写入 int want[8][4]
        {0, 0, 0, 0}, {1, 0, 1, 0}, {0, 0, 1, 0}, {1, 1, 1, 0},
        {0, 1, 0, 0}, {1, 1, 0, 1}, {0, 1, 0, 1}, {1, 1, 1, 1},
    };
    int path[16][4];     // int 当前路径[16][4];
    int n = solve(path); // 把 solve(当前路径) 存入 元素个数
    if (n != 8) {
        printf("FAILED: path length %d\n", n);
        return 1;
    }
    for (int i = 0; i < 8; i++)             // 让 下标 i 从 0 开始计数，下标 i 小于 8 就继续
        for (int j = 0; j < 4; j++)         // 让 下标 j 从 0 开始计数，下标 j 小于 4 就继续
            if (path[i][j] != want[i][j]) { // 若 当前路径[下标 i][下标 j] 不等于 want[下标 i][下标 j]
                printf("FAILED: mismatch at %d,%d\n", i, j); // 打印输出
                return 1;                                    // 返回 1
            }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
