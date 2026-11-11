/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107868749
 * LeetCode 107868749. 贪心策略 — C 版（贪心策略之 matrixSort / PFC 编码 / Huffman 树）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

#define MATRIX_SORT_INPLACE(rows, cols, m)                                                                   \
    do {                                                                                                     \
        for (int c = 0; c < (cols); c++) {                                                                   \
            for (int i = 0; i < (rows)-1; i++)                                                               \
                for (int j = 0; j < (rows)-1 - i; j++)                                                       \
                    if (m[j][c] > m[j + 1][c]) {                                                             \
                        int t = m[j][c];                                                                     \
                        m[j][c] = m[j + 1][c];                                                               \
                        m[j + 1][c] = t;                                                                     \
                    }                                                                                        \
        }                                                                                                    \
        for (int r = 0; r < (rows); r++) {                                                                   \
            for (int i = 0; i < (cols)-1; i++)                                                               \
                for (int j = 0; j < (cols)-1 - i; j++)                                                       \
                    if (m[r][j] > m[r][j + 1]) {                                                             \
                        int t = m[r][j];                                                                     \
                        m[r][j] = m[r][j + 1];                                                               \
                        m[r][j + 1] = t;                                                                     \
                    }                                                                                        \
        }                                                                                                    \
    } while (0) // } while (0)

/* Huffman 节点：left/right < 0 表示叶子 */
typedef struct {     // typedef struct {
    long long freq;  // long long 频次表;
    char sym;        // char sym;
    int left, right; // int 左边界, 右边界;
} HNode;             // } HNode;

static HNode tree[16]; // static HNode tree[16];
static int tree_n = 0; // 把 0; 写入 static int tree_n

static int build_huffman(const char *syms, const long long *freqs, int n) { // 定义函数/方法 build_huffman
    int order[16];                                                          // int order[16];
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        tree[i].freq = freqs[i];  // 把 freqs[下标 i]; 写入 频次表
        tree[i].sym = syms[i];    // 把 syms[下标 i]; 写入 tree[i].sym
        tree[i].left = tree[i].right = -1; // 把 tree[下标 i].右边界 赋值为 减 1; 写入 左边界
        order[i] = i;                      // 把 下标 i; 写入 order[i]
    }
    int count = n;      // 把 元素个数 存入 计数
    tree_n = n;         // 把 元素个数; 写入 tree_n
    while (count > 1) { // 循环，直到不满足「计数 超过 1」
        /* 找最小的两个（按 order 中未合并者）——用简单线性选择 */
        int a = -1, b = -1;                // 把 减 1, b 赋值为 减 1 存入 数组
        for (int i = 0; i < tree_n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 tree_n 就继续
            if (tree[i].freq < 0)
                continue; // 若 tree[下标 i].频次表 小于 0) continue;
            if (a < 0 || tree[i].freq < tree[a].freq) {
                b = a;
                a = i;
            } else if (b < 0 || tree[i].freq < tree[b].freq) {
                b = i;
            } // 否则，若 b 小于 0 或 tree[下标 i].频次表 小于 tree[b].频次表) { b 赋值为 下标 i; }
        }
        if (b < 0)
            break; // 若 b 小于 0) break;
        /* 合并（同权重时先取先出现的，保持与 JS 版本一致的稳定性不追求完全一致） */
        long long fa = tree[a].freq,
                  fb = tree[b].freq; // 把 tree[数组].频次表, fb 赋值为 tree[b].频次表 存入 fa
        if (fa > fb) {
            int t = a;
            a = b;
            b = t;
        } // 若 fa 超过 fb) { int 另一字符串 赋值为 数组; 数组 赋值为 b; b 赋值为 另一字符串; }
        tree[tree_n].freq =
            tree[a].freq + tree[b].freq; // 把 tree[数组].频次表 加 tree[b].频次表; 写入 频次表
        tree[tree_n].sym = 0;            // 把 0; 写入 tree[tree_n].sym
        tree[tree_n].left = a;           // 把 数组; 写入 左边界
        tree[tree_n].right = b;          // 把 b; 写入 右边界
        tree[a].freq = -1;               // 把 减 1; 写入 频次表
        tree[b].freq = -1;               // 把 减 1; 写入 频次表
        tree_n++;                        // tree_n 加一
        count--;                         // 计数 减一
    }
    /* 根 = 唯一 freq >= 0 的节点 */
    for (int i = 0; i < tree_n; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 tree_n 就继续
        if (tree[i].freq >= 0)
            return i; // 若 tree[下标 i].频次表 不低于 0，直接返回 下标 i
    return -1;        // 返回 减 1
}

static char codes[8][8]; // static char codes[8][8];
static int code_len[8];  // static int code_len[8];

static void walk(int node, char *prefix, int depth) {    // 定义函数/方法 walk
    if (tree[node].left < 0) {                           // 若 tree[节点].左边界 小于 0
        if (depth == 0) {                                // 若 深度 等于 0
            strcpy(codes[tree[node].sym - 'A'], "0");    // strcpy(codes[tree[节点].sym 减 'A'], 「0」);
            code_len[tree[node].sym - 'A'] = 1;          // 把 1; 写入 code_len[tree[node].sym - 'A']
        } else {                                         // 否则
            prefix[depth] = 0;                           // 把 0; 写入 prefix[depth]
            strcpy(codes[tree[node].sym - 'A'], prefix); // strcpy(codes[tree[节点].sym 减 'A'], prefix);
            code_len[tree[node].sym - 'A'] = depth;      // 把 深度; 写入 code_len[tree[node].sym - 'A']
        }
        return; // return;
    }
    prefix[depth] = '0';                       // 把 '0'; 写入 prefix[depth]
    walk(tree[node].left, prefix, depth + 1);  // walk(tree[节点].左边界, prefix, 深度 加 1);
    prefix[depth] = '1';                       // 把 '1'; 写入 prefix[depth]
    walk(tree[node].right, prefix, depth + 1); // walk(tree[节点].右边界, prefix, 深度 加 1);
}

int main(void) { // 程序入口：跑内嵌自测用例
    /* case1: matrixSort */
    int mat[3][3] = {
        {5, 3, 4}, {1, 6, 2}, {7, 9, 8}}; // 把 {{5, 3, 4}, {1, 6, 2}, {7, 9, 8}}; 写入 int mat[3][3]
    int want[3][3] = {
        {1, 2, 3}, {4, 5, 6}, {7, 8, 9}}; // 把 {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}; 写入 int want[3][3]
    MATRIX_SORT_INPLACE(3, 3, mat);       // MATRIX_SORT_INPLACE(3, 3, mat);
    for (int i = 0; i < 3; i++)           // 让 下标 i 从 0 开始计数，下标 i 小于 3 就继续
        for (int j = 0; j < 3; j++)       // 让 下标 j 从 0 开始计数，下标 j 小于 3 就继续
            if (mat[i][j] != want[i][j]) {
                printf("matrixSort mismatch\n");
                return 1;
            }

    /* case2: WPL（频次 5,9,12,13,16,45 的最优 WPL = 224） */
    const char syms[6] = {'A', 'B', 'C',
                          'D', 'E', 'F'}; // 把 {'A', 'B', 'C', 'D', 'E', 'F'}; 写入 const char syms[6]
    long long freqs[6] = {5, 9, 12, 13, 16, 45}; // 把 {5, 9, 12, 13, 16, 45}; 写入 long long freqs[6]
    int root = build_huffman(syms, freqs, 6);    // 把 build_huffman(syms, freqs, 6) 存入 根节点
    char prefix[16];                             // char prefix[16];
    memset(codes, 0, sizeof(codes));             // memset(codes, 0, sizeof(codes));
    walk(root, prefix, 0);                       // walk(根节点, prefix, 0);
    long long wpl = 0;                           // 把 0 存入 wpl
    for (int i = 0; i < 6; i++)
        wpl += freqs[i] * code_len[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
    if (wpl != 224) {
        printf("WPL mismatch: %lld\n", wpl);
        return 1;
    }

    /* case3: 前缀无关 */
    for (int i = 0; i < 6; i++)       // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
        for (int j = 0; j < 6; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 6 就继续
            if (i == j)
                continue; // 若 下标 i 等于 下标 j) continue;
            if (strncmp(codes[j], codes[i], strlen(codes[i])) == 0) {
                printf("not prefix-free\n"); // 打印输出
                return 1;                    // 返回 1
            }
        }

    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
