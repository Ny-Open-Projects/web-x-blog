/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/112548608
 * LeetCode 112548608. 计算思维之经典农夫过河问题C++实现（DFS 求任一可行过河序列）
 * 状态编码 4bit：bit3=农夫 bit2=狼(W) bit1=羊(S) bit0=菜(V)
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

static int invalid(int s) { // 定义函数/方法 invalid
    int h = (s >> 3) & 1, w = (s >> 2) & 1, sg = (s >> 1) & 1, v = s & 1;
    if (h != sg && sg == w)
        return 1; // 若 h 不等于 sg 且 sg 等于 权重，直接返回 1
    if (h != sg && sg == v)
        return 1; // 若 h 不等于 sg 且 sg 等于 值，直接返回 1
    return 0;     // 返回 0
}

static char path[16];    // static char 当前路径[16];
static int path_len = 0; // 把 0; 写入 static int path_len
static int visited[16];  // static int 已访问集合[16];

static int go(int st) { // 定义函数/方法 go
    if (st == 15)
        return 1; // 若 st 等于 15，直接返回 1
    if (visited[st])
        return 0;    // 若 已访问集合[st]，直接返回 0
    visited[st] = 1; // 把 1; 写入 visited[st]
    static const char roles[4] = {'-', 'W', 'S',
                                  'V'}; // 把 { ' 减 ', 'W', 'S', 'V' }; 写入 static const char roles[4]
    for (int ri = 0; ri < 4; ri++) {    // 让 ri 从 0 开始计数，ri 小于 4 就继续
        int shift = (ri == 0) ? -1 : (3 - ri); /* W->bit2 S->bit1 V->bit0 */
        int ns = st ^ 8; /* 农夫总是过河 */ // 把 st 按位异或 8; 除以 乘 农夫总是过河 乘 除以 存入 ns
        if (ri != 0) {                      // 若 ri 不等于 0
            if (((st >> 3) & 1) != ((st >> shift) & 1))
                continue;           /* 出发前同岸 */
            ns = ns ^ (1 << shift); // 把 ns 按位异或 (1 小于 小于 shift); 写入 ns
        }
        if (invalid(ns))
            continue;                     // 若 invalid(ns)) continue;
        if (go(ns)) {                     // 若 go(ns
            path[path_len++] = roles[ri]; // 把 roles[ri]; 写入 path[path_len++]
            return 1;                     // 返回 1
        }
    }
    return 0; // 返回 0
}

static int simulate(const char *p, int n) { // 定义函数/方法 simulate
    int st = 0;                             // 把 0 存入 st
    for (int i = n - 1; i >= 0; i--) {
        /* path 逆序存放，模拟按正序走 */ // 让 下标 i 从 元素个数 减 1 开始计数，下标 i 不低于 0 就继续
        char role = p[i];                 // 把 节点[下标 i]; 写入 char role
        int before = st;                  // 把 st 存入 before
        st ^= 8;                          // 把 8; 写入 st ^
        if (role != '-') { // 若 role 不等于 ' 减 '
            int shift = (role == 'W')   ? 2
                        : (role == 'S') ? 1
                                        : 0; // 把 (role 等于 'W') ? 2 : (role 等于 'S') ? 1 : 0 存入 shift
            if (((before >> 3) & 1) != ((before >> shift) & 1))
                return 0;
            st ^= (1 << shift); // 把 (1 小于 小于 shift); 写入 st ^
        }
        if (invalid(st))
            return 0; // 若 invalid(st)，直接返回 0
    }
    return st == 15; // 返回 st 等于 15
}

int main(void) { // 程序入口：跑内嵌自测用例
    const char want_path[7] = {'S', '-', 'W', 'S', 'V', '-', 'S'};
    const char *want_readable =
        "HS H HW HS HV H HS"; // 把 「HS H HW HS HV H HS」; 写入 const char *want_readable

    memset(visited, 0, sizeof(visited)); // memset(已访问集合, 0, sizeof(已访问集合));
    go(0);                               // go(0);

    /* case1: 路径一致（path 为逆序存放） */
    if (path_len != 7) {
        printf("FAIL length %d\n", path_len);
        return 1;
    }
    for (int i = 0; i < 7; i++) {          // 让 下标 i 从 0 开始计数，下标 i 小于 7 就继续
        if (path[6 - i] != want_path[i]) { // 若 当前路径[6 减 下标 i] 不等于 want_path[下标 i]
            printf("FAIL path[%d] got %c want %c\n", i, path[6 - i], want_path[i]); // 打印输出
            return 1;                                                               // 返回 1
        }
    }

    /* case2: 可读方案串 */
    char got_readable[64] = "";   // 把 「」; 写入 char got_readable[64]
    for (int i = 0; i < 7; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 7 就继续
        char role = path[6 - i];  // 把 当前路径[6 减 下标 i]; 写入 char role
        char piece[4];            // char piece[4];
        if (role != '-')
            snprintf(piece, sizeof(piece), "H%c", role);
        else
            snprintf(piece, sizeof(piece), "H"); // 否则
        if (i)
            strcat(got_readable, " "); // 若 下标 i) strcat(got_readable, 「 」);
        strcat(got_readable, piece);   // 打印输出
    }
    if (strcmp(got_readable, want_readable) != 0) {     // 若 strcmp(got_readable, want_readable) 不等于 0
        printf("FAIL readable got %s\n", got_readable); // 打印输出
        return 1;                                       // 返回 1
    }

    /* case3 + case4 */
    if (!simulate(path, path_len)) {
        printf("FAIL simulate\n");
        return 1;
    }

    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
