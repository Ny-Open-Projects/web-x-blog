// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133925028
// LeetCode 122. 买卖股票的最佳时机II — C++ 版（方案5）
#include <cassert>                                     // 引入头文件
#include <iostream>                                    // 引入头文件
#include <vector>                                      // 引入头文件
static int maxProfit(const std::vector<int> &prices) { // 定义函数/方法 maxProfit
    int profit = 0;                                    // 把 0 存入 profit
    for (size_t i = 1; i < prices.size();
         ++i) { // 让 下标 i 从 1 开始计数，下标 i 小于 价格序列.大小() 就继续
        if (prices[i] > prices[i - 1])
            profit += prices[i] - prices[i - 1];
    }
    return profit; // 返回 profit
}
int main() {                                    // 程序入口：跑内嵌自测用例
    assert(maxProfit({7, 1, 5, 3, 6, 4}) == 7); // 断言校验
    assert(maxProfit({1, 2, 3, 4, 5}) == 4);    // 断言校验
    assert(maxProfit({7, 6, 4, 3, 1}) == 0);    // 断言校验
    std::cout << "PASS" << std::endl;           // 全部用例通过，输出 PASS
    return 0;                                   // 返回 0
}
