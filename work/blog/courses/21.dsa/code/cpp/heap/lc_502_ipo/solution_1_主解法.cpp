// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136847926
// LeetCode 502. IPO — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static long long findMaximizedCapital(int k, long long w, const std::vector<long long> &profits,
                                      const std::vector<long long> &capital) {
    int n = static_cast<int>(profits.size()); // 把 static_cast 小于 int 超过 (profits.大小()) 存入 元素个数
    std::vector<bool> used(n, false); // std::vector 小于 bool 超过 已用标记(元素个数, false);
    for (int t = 0; t < k; ++t) { // 让 另一字符串 从 0 开始计数，另一字符串 小于 下标 k 就继续
        long long best = -1;          // 把 减 1 存入 当前最优
        int best_j = -1;              // 把 减 1 存入 best_j
        for (int j = 0; j < n; ++j) { // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
            if (!used[j] && capital[j] <= w && profits[j] > best) {
                best = profits[j];
                best_j = j;
            }
        }
        if (best_j < 0)
            break;           // 若 best_j 小于 0) break;
        w += best;           // 权重累加 当前最优
        used[best_j] = true; // 把 true; 写入 used[best_j]
    }
    return w; // 返回 权重
}
int main() {                                                       // 程序入口：跑内嵌自测用例
    assert(findMaximizedCapital(2, 0, {1, 2, 3}, {0, 1, 1}) == 4); // 断言校验
    assert(findMaximizedCapital(3, 0, {1, 2, 3}, {0, 1, 2}) == 6); // 断言校验
    assert(findMaximizedCapital(1, 0, {1, 2}, {1, 2}) == 0);       // 断言校验
    assert(findMaximizedCapital(2, 1, {1, 2, 3}, {1, 1, 2}) == 6); // 断言校验
    std::cout << "PASS" << std::endl;                              // 全部用例通过，输出 PASS
    return 0;                                                      // 返回 0
}
