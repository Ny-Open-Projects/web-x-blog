// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130588647
// LeetCode 123. 买卖股票的最佳时机III — C++ 版（方案2）
#include <algorithm>                                      // 引入头文件
#include <cassert>                                        // 引入头文件
#include <iostream>                                       // 引入头文件
#include <vector>                                         // 引入头文件
static int maxProfitIII(const std::vector<int> &prices) { // 定义函数/方法 maxProfitIII
    int buy1 = -1000000000, sell1 = 0, buy2 = -1000000000, sell2 = 0;
    for (int p : prices) {                 // for (int 节点 : 价格序列) {
        buy1 = std::max(buy1, -p);         // 把 std::取较大值 buy1, 减 节点); 写入 buy1
        sell1 = std::max(sell1, buy1 + p); // 把 std::取较大值 sell1, buy1 加 节点); 写入 sell1
        buy2 = std::max(buy2, sell1 - p);  // 把 std::取较大值 buy2, sell1 减 节点); 写入 buy2
        sell2 = std::max(sell2, buy2 + p); // 把 std::取较大值 sell2, buy2 加 节点); 写入 sell2
    }
    return sell2; // 返回 sell2
}
int main() {                                             // 程序入口：跑内嵌自测用例
    assert(maxProfitIII({1, 2, 3}) == 2);                // 断言校验
    assert(maxProfitIII({1, 2, 3, 4, 5}) == 4);          // 断言校验
    assert(maxProfitIII({7, 6, 4, 3, 1}) == 0);          // 断言校验
    assert(maxProfitIII({3, 3, 5, 0, 0, 3, 1, 4}) == 6); // 断言校验
    assert(maxProfitIII({1}) == 0);                      // 断言校验
    assert(maxProfitIII({1, 2}) == 1);                   // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS