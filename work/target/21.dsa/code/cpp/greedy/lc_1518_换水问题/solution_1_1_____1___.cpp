// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116
// LeetCode 1518. 换水问题 — C++ 版（方案1）
#include <cassert>                                            // 引入头文件
#include <iostream>                                           // 引入头文件
static int numWaterBottles(int numBottles, int numExchange) { // 定义函数/方法 numWaterBottles
    int ans = numBottles, empty = numBottles; // 把 numBottles, empty 赋值为 numBottles 存入 答案
    while (empty >= numExchange) {            // 循环，直到不满足「empty 不低于 numExchange」
        int newB = empty / numExchange;       // 把 empty 除以 numExchange 存入 newB
        ans += newB;                          // 答案累加 newB
        empty = newB + empty % numExchange;   // 把 newB 加 empty 对…取模 numExchange; 写入 empty
    }
    return ans; // 返回 答案
}
int main() {                              // 程序入口：跑内嵌自测用例
    assert(numWaterBottles(9, 3) == 13);  // 断言校验
    assert(numWaterBottles(15, 4) == 19); // 断言校验
    std::cout << "PASS" << std::endl;     // 全部用例通过，输出 PASS
    return 0;                             // 返回 0
}
