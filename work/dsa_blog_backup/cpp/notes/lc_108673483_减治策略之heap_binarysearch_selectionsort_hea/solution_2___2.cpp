// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
// LeetCode 108673483. 减治策略 — C++ 版（方案2：快速选择求第 k 小）
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

static int select_k(std::vector<int> &a, int lo, int hi, int k) { // 定义函数/方法 select_k
    if (lo == hi)
        return a[lo];               // 若 左边界 等于 右边界，直接返回 数组[左边界]
    int pivot = a[hi];              // 把 数组[右边界] 存入 pivot
    int i = lo;                     // 把 左边界 存入 下标 i
    for (int j = lo; j < hi; ++j) { // 让 下标 j 从 左边界 开始计数，下标 j 小于 右边界 就继续
        if (a[j] <= pivot) {        // 若 数组[下标 j] 不超过 pivot
            std::swap(a[i], a[j]); // 交换 数组[下标 i] 与 数组[下标 j]
            ++i;                   // 加一 下标 i;
        }
    }
    std::swap(a[i], a[hi]); // 交换 数组[下标 i] 与 数组[右边界]
    if (i == k)
        return a[i]; // 若 下标 i 等于 下标 k，直接返回 数组[下标 i]
    if (i > k)
        return select_k(a, lo, i - 1,
                        k); // 若 下标 i 超过 下标 k，直接返回 select_k(数组, 左边界, 下标 i 减 1, 下标 k)
    return select_k(a, i + 1, hi, k); // 返回 select_k(数组, 下标 i 加 1, 右边界, 下标 k)
}

int main() {                                       // 程序入口：跑内嵌自测用例
    std::vector<int> base{3, 1, 4, 1, 5, 9, 2, 6}; // std::vector 小于 int 超过 base{3, 1, 4, 1, 5, 9, 2, 6};
    int ks[4] = {2, 3, 0, 7};                      // 把 {2, 3, 0, 7}; 写入 int ks[4]
    int ws[4] = {2, 3, 1, 9};                      // 把 {2, 3, 1, 9}; 写入 int ws[4]
    for (int idx = 0; idx < 4; ++idx) {            // 让 idx 从 0 开始计数，idx 小于 4 就继续
        std::vector<int> a = base;                 // 把 base; 写入 std::vector<int> a
        int got = select_k(a, 0, static_cast<int>(a.size()) - 1, ks[idx]);
        if (got != ws[idx]) {
            std::cout << "case " << idx << " failed" << std::endl;
            return 1;
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
