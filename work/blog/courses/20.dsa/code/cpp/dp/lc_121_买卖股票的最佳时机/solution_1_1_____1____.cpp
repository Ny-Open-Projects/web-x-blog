// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130515763
// LeetCode 121. 买卖股票的最佳时机 — C++ 版（方案1）
#include <algorithm>                                   // 引入头文件
#include <cassert>                                     // 引入头文件
#include <iostream>                                    // 引入头文件
#include <vector>                                      // 引入头文件
static int maxProfit(const std::vector<int> &prices) { // 定义函数/方法 maxProfit
    int minP = -1, best = 0;                           // 把 减 1, 当前最优 赋值为 0 存入 minP
    for (int p : prices) {                             // for (int 节点 : 价格序列) {
        if (minP == -1 || p < minP)
            minP = p; // 若 minP 等于 减 1 或 节点 小于 minP) minP 赋值为 节点;
        if (p - minP > best)
            best = p - minP; // 若 节点 减 minP 超过 当前最优) 当前最优 赋值为 节点 减 minP;
    }
    return best; // 返回 当前最优
}
int main() {
    assert(maxProfit({7, 1, 5, 3, 6, 4}) == 5);
    assert(maxProfit({7, 6, 4, 3, 1}) == 0);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS