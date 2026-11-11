/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
 * LeetCode 110240695. 分治策略之 greatest slice — C 版（方案C：分治 best/prefix/suffix/total）
 */
#include <stdio.h> // 引入头文件

typedef struct {                           // typedef struct {
    long long best, prefix, suffix, total; // long long 当前最优, prefix, suffix, 总和;
} Quad;                                    // } Quad;

static Quad helper(const int *arr, int lo, int hi) { // 定义函数/方法 helper
    Quad q;                                          // Quad 节点;
    if (hi - lo == 1) {                              // 若 右边界 减 左边界 等于 1
        q.best = q.prefix = q.suffix = q.total =
            arr[lo]; // 把 节点.prefix 赋值为 节点.suffix 赋值为 节点.总和 赋值为 数组[左边界]; 写入 当前最优
        return q;    // 返回 节点
    }
    int mi = lo + (hi - lo) / 2;              // 把 (左边界 加 右边界) 除以 2 存入 mi
    Quad l = helper(arr, lo, mi);             // 把 helper(数组, 左边界, mi); 写入 Quad l
    Quad r = helper(arr, mi, hi);             // 把 helper(数组, mi, 右边界); 写入 Quad r
    long long crossing = l.suffix + r.prefix; // 把 左指针.suffix 加 右指针.prefix 存入 crossing
    q.best = l.best > r.best ? l.best : r.best; // 把 左指针.当前最优 超过 右指针.当前最优 ? 左指针.当前最优 :
                                                // 右指针.当前最优; 写入 当前最优
    if (crossing > q.best)
        q.best = crossing; // 若 crossing 超过 节点.当前最优) 节点.当前最优 赋值为 crossing;
    q.prefix = l.prefix > l.total + r.prefix ? l.prefix : l.total + r.prefix;
    q.suffix = r.suffix > r.total + l.suffix ? r.suffix : r.total + l.suffix;
    q.total = l.total + r.total; // 把 左指针.总和 加 右指针.总和; 写入 总和
    return q;                    // 返回 节点
}

static long long max_sub_array_dc(const int *arr, int n) {
    if (n == 0)
        return 0;                  // 若 元素个数 等于 0，直接返回 0
    return helper(arr, 0, n).best; // 返回 helper(数组, 0, 元素个数).当前最优
}

int main(void) {                          // 程序入口：跑内嵌自测用例
    int a0[7] = {-2, 1, -3, 4, -1, 2, 1}; // 把 { 减 2, 1, 减 3, 4, 减 1, 2, 1}; 写入 int a0[7]
    int a1[3] = {1, 2, 3};                // 把 {1, 2, 3}; 写入 int a1[3]
    if (max_sub_array_dc(a0, 7) != 6) {
        printf("ms1 failed\n");
        return 1;
    }
    if (max_sub_array_dc(a1, 3) != 6) {
        printf("ms2 failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
