/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114454
 * LeetCode 26. 删除有序数组中的重复项 — C 版 */
#include <stdio.h> // 引入头文件

/* 方案3：快慢指针 —— fast 扫描，slow 指向已去重区间末尾 */
static int remove_duplicates(int *nums, int len) { // 定义函数/方法 remove_duplicates
    if (len == 0)
        return 0;                            // 若 长度 等于 0，直接返回 0
    int slow = 0;                            // 把 0 存入 慢指针
    for (int fast = 1; fast < len; fast++) { // 让 快指针 从 1 开始计数，快指针 小于 长度 就继续
        if (nums[fast] != nums[slow]) { // 若 数组[快指针] 不等于 数组[慢指针]
            slow++;                     // 慢指针 加一
            nums[slow] = nums[fast];    // 把 数组[快指针]; 写入 nums[slow]
        }
    }
    return slow + 1; // 返回 慢指针 加 1
}

static int eq_arr(const int *a, int alen, const int *b, int blen) { // 定义函数/方法 eq_arr
    if (alen != blen)
        return 0;                    // 若 alen 不等于 blen，直接返回 0
    for (int i = 0; i < alen; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 alen 就继续
        if (a[i] != b[i])
            return 0; // 若 数组[下标 i] 不等于 b[下标 i]，直接返回 0
    }
    return 1; // 返回 1
}

int main(void) { // 程序入口：跑内嵌自测用例
    /* 与 TS 事实源内嵌用例一致 */
    struct {
        int in[4];
        int in_len;
        int k;
        int pre[4];
        int pre_len;
    } cases[] = {
        {{1, 1, 2}, 3, 2, {1, 2}, 2},
        {{1, 2, 3}, 3, 3, {1, 2, 3}, 3},
        {{0}, 0, 0, {0}, 0},
    };
    int n = (int)(sizeof(cases) /
                  sizeof(cases[0])); // 把 (int)(sizeof(cases) 除以 sizeof(cases[0])) 存入 元素个数
    for (int ci = 0; ci < n; ci++) { // 让 ci 从 0 开始计数，ci 小于 元素个数 就继续
        int nums[4];                 // int 数组[4];
        for (int i = 0; i < cases[ci].in_len; i++)
            nums[i] = cases[ci].in[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 cases[ci].in_len 就继续
        int got = remove_duplicates(
            nums, cases[ci].in_len); // 把 remove_duplicates(数组, cases[ci].in_len) 存入 got
        if (got != cases[ci].k || !eq_arr(nums, got, cases[ci].pre, cases[ci].pre_len)) {
            printf("FAIL case %d k=%d\n", ci, got); // 打印输出
            return 1;                               // 返回 1
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
