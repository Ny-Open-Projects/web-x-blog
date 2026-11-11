// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130741193
// LeetCode 714. 买卖股票的最佳时机含手续费 — C++ 版（方案1）
#include <algorithm>                                               // 引入头文件
#include <cassert>                                                 // 引入头文件
#include <iostream>                                                // 引入头文件
#include <vector>                                                  // 引入头文件
static int maxProfitFee(const std::vector<int> &prices, int fee) { // 定义函数/方法 maxProfitFee
    int hold = -prices[0], sold = 0; // 把 减 价格序列[0], sold 赋值为 0 存入 hold
    for (size_t i = 1; i < prices.size();
         ++i) { // 让 下标 i 从 1 开始计数，下标 i 小于 价格序列.大小() 就继续
        int nh = std::max(hold, sold - prices[i]); // 把 std::取较大值 hold, sold 减 价格序列[下标 i]) 存入 nh
        int ns = std::max(sold, hold + prices[i] -
                                    fee); // 把 std::取较大值 sold, hold 加 价格序列[下标 i] 减 fee) 存入 ns
        hold = nh;                        // 把 nh; 写入 hold
        sold = ns;                        // 把 ns; 写入 sold
    }
    return sold; // 返回 sold
}
int main() {
    assert(maxProfitFee({1, 3, 2, 8, 4, 9}, 2) == 8);
    assert(maxProfitFee({1}, 1) == 0);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS