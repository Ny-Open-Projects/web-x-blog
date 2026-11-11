/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134859971 */
/* LeetCode 2050. 并行课程III — C 版（方案2） */
#include <stdio.h>                                                            // 引入头文件
static int minimum_time(int n, int relations[][2], int nr, const int *time) { // 定义函数/方法 minimum_time
    int next_[64][64], nnext[64] = {0}; // 把 {0}; 写入 int next_[64][64], nnext[64]
    int indeg[64] = {0};                // 把 {0}; 写入 int indeg[64]
    for (int i = 0; i < nr; i++) {      // 让 下标 i 从 0 开始计数，下标 i 小于 nr 就继续
        int u = relations[i][0],
            v = relations[i][1]; // 把 relations[下标 i][0], 值 赋值为 relations[下标 i][1] 存入 节点 u
        next_[u][nnext[u]++] = v; // 把 值; 写入 next_[u][nnext[u]++]
        indeg[v]++;               // indeg[值] 加一 ;
    }
    int finish[64] = {0};  // 把 {0}; 写入 int finish[64]
    int queue[64], qn = 0; // 把 0; 写入 int queue[64], qn
    for (int c = 1; c <= n; c++)
        if (indeg[c] == 0)
            queue[qn++] = c; // 让 字符 从 1 开始计数，字符 不超过 元素个数 就继续
    int total = 0;           // 把 0 存入 总和
    while (qn > 0) {         // 循环，直到不满足「qn 超过 0」
        int nq[64], nqn = 0; // 把 0; 写入 int nq[64], nqn
        for (int i = 0; i < qn; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 qn 就继续
            int c = queue[i];          // 把 队列[下标 i] 存入 字符
            finish[c] += time[c - 1];  // finish[c]累加 time[字符 减 1]
            if (finish[c] > total)
                total = finish[c]; // 若 finish[字符] 超过 总和) 总和 赋值为 finish[字符];
            for (int k = 0; k < nnext[c]; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 nnext[字符] 就继续
                int nx = next_[c][k]; // 把 next_[字符][下标 k] 存入 nx
                if (finish[nx] < finish[c])
                    finish[nx] =
                        finish[c]; // 若 finish[nx] 小于 finish[字符]) finish[nx] 赋值为 finish[字符];
                if (--indeg[nx] == 0)
                    nq[nqn++] = nx; // 若 减一 indeg[nx] 等于 0) nq[nqn 加一 ] 赋值为 nx;
            }
        }
        for (int i = 0; i < nqn; i++)
            queue[i] = nq[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 nqn 就继续
        qn = nqn;             // 把 nqn; 写入 qn
    }
    return total; // 返回 总和
}
int main(void) {                    // 程序入口：跑内嵌自测用例
    int r1[][2] = {{1, 3}, {2, 3}}; // 把 {{1,3},{2,3}}; 写入 int r1[][2]
    if (minimum_time(3, r1, 2, (int[]){3, 2, 5}) != 8) {
        printf("FAIL 1\n");
        return 1;
    }
    int r2[][2] = {{1, 2}, {2, 3}, {3, 4}, {4, 5}}; // 把 {{1,2},{2,3},{3,4},{4,5}}; 写入 int r2[][2]
    if (minimum_time(5, r2, 4, (int[]){1, 2, 3, 4, 5}) != 15) {
        printf("FAIL 2\n");
        return 1;
    }
    if (minimum_time(1, r2, 0, (int[]){5}) != 5) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS