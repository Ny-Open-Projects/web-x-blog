/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135749595 */
/* LeetCode 295. 数据流的中位数 — C 版（方案3） */
#include <stdio.h> // 引入头文件
/* 双堆：maxh 大根堆（存较小半），minh 小根堆（存较大半） */
static int maxh[8192], minhd[8192]; // static int maxh[8192], minhd[8192];
static int nmax, nmin;              // static int nmax, nmin;
static void push_maxh(int v) {      // 定义函数/方法 push_maxh
    maxh[++nmax] = v;               // 把 值; 写入 maxh[++nmax]
    int i = nmax;                   // 把 nmax 存入 下标 i
    while (i > 1 && maxh[i] > maxh[i / 2]) {
        int t = maxh[i];
        maxh[i] = maxh[i / 2];
        maxh[i / 2] = t;
        i /= 2;
    }
}
static void push_minh(int v) { // 定义函数/方法 push_minh
    minhd[++nmin] = v;         // 把 值; 写入 minhd[++nmin]
    int i = nmin;              // 把 nmin 存入 下标 i
    while (i > 1 && minhd[i] < minhd[i / 2]) {
        int t = minhd[i];
        minhd[i] = minhd[i / 2];
        minhd[i / 2] = t;
        i /= 2;
    }
}
static int pop_maxh(void) { // 定义函数/方法 pop_maxh
    int top = maxh[1];      // 把 maxh[1] 存入 top
    maxh[1] = maxh[nmax--]; // 把 maxh[nmax 减一 ]; 写入 maxh[1]
    int i = 1;              // 把 1 存入 下标 i
    while (1) {             // 循环，直到不满足「1」
        int l = 2 * i, r = 2 * i + 1,
            m = i; // 把 2 乘 下标 i, 右指针 赋值为 2 乘 下标 i 加 1, 映射表 赋值为 下标 i 存入 左指针
        if (l <= nmax && maxh[l] > maxh[m])
            m = l; // 若 左指针 不超过 nmax 且 maxh[左指针] 超过 maxh[映射表]) 映射表 赋值为 左指针;
        if (r <= nmax && maxh[r] > maxh[m])
            m = r; // 若 右指针 不超过 nmax 且 maxh[右指针] 超过 maxh[映射表]) 映射表 赋值为 右指针;
        if (m == i)
            break; // 若 映射表 等于 下标 i) break;
        int t = maxh[i];
        maxh[i] = maxh[m];
        maxh[m] = t;
        i = m;
    }
    return top; // 返回 top
}
static int pop_minh(void) {   // 定义函数/方法 pop_minh
    int top = minhd[1];       // 把 minhd[1] 存入 top
    minhd[1] = minhd[nmin--]; // 把 minhd[nmin 减一 ]; 写入 minhd[1]
    int i = 1;                // 把 1 存入 下标 i
    while (1) {               // 循环，直到不满足「1」
        int l = 2 * i, r = 2 * i + 1,
            m = i; // 把 2 乘 下标 i, 右指针 赋值为 2 乘 下标 i 加 1, 映射表 赋值为 下标 i 存入 左指针
        if (l <= nmin && minhd[l] < minhd[m])
            m = l; // 若 左指针 不超过 nmin 且 minhd[左指针] 小于 minhd[映射表]) 映射表 赋值为 左指针;
        if (r <= nmin && minhd[r] < minhd[m])
            m = r; // 若 右指针 不超过 nmin 且 minhd[右指针] 小于 minhd[映射表]) 映射表 赋值为 右指针;
        if (m == i)
            break; // 若 映射表 等于 下标 i) break;
        int t = minhd[i];
        minhd[i] = minhd[m];
        minhd[m] = t;
        i = m;
    }
    return top; // 返回 top
}
static void mf_add(int num) { // 定义函数/方法 mf_add
    if (nmax == 0 || num <= maxh[1])
        push_maxh(num); // 若 nmax 等于 0 或 num 不超过 maxh[1]) push_maxh(num);
    else
        push_minh(num); // 否则
    if (nmax > nmin + 1)
        push_minh(pop_maxh()); // 若 nmax 超过 nmin 加 1) push_minh(pop_maxh());
    else if (nmin > nmax)
        push_maxh(pop_minh()); // 否则，若 nmin 超过 nmax) push_maxh(pop_minh());
}
static double mf_median(void) { // 定义函数/方法 mf_median
    if (nmax == nmin)
        return (maxh[1] + minhd[1]) / 2.0; // 若 nmax 等于 nmin，直接返回 (maxh[1] 加 minhd[1]) 除以 2.0
    return maxh[1];                        // 返回 maxh[1]
}
int main(void) {                // 程序入口：跑内嵌自测用例
    nmax = nmin = 0;            // 把 nmin 赋值为 0; 写入 nmax
    int xs[] = {1, 2, 3, 4, 5}; // 把 {1, 2, 3, 4, 5}; 写入 int xs[]
    for (int i = 0; i < 5; i++)
        mf_add(xs[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
    if (mf_median() != 3.0) {
        printf("FAIL 1\n");
        return 1;
    }                // 若 mf_median() 不等于 3.0) { 输出「FAIL 1 」); return 1; }
    nmax = nmin = 0; // 把 nmin 赋值为 0; 写入 nmax
    mf_add(1);
    mf_add(2); // mf_add(1); mf_add(2);
    if (mf_median() != 1.5) {
        printf("FAIL 2\n");
        return 1;
    }          // 若 mf_median() 不等于 1.5) { 输出「FAIL 2 」); return 1; }
    mf_add(3); // mf_add(3);
    if (mf_median() != 2.0) {
        printf("FAIL 3\n");
        return 1;
    }                 // 若 mf_median() 不等于 2.0) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
