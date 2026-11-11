// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116
// LeetCode 3100. 换水问题 II — C++ 版（方案2）
#include <cassert>                                            // 引入头文件
#include <iostream>                                           // 引入头文件
static int maxBottlesDrunk(int numBottles, int numExchange) { // 定义函数/方法 maxBottlesDrunk
    int drunk = numBottles, empty = numBottles; // 把 numBottles, empty 赋值为 numBottles 存入 drunk
    while (empty >= numExchange) {              // 循环，直到不满足「empty 不低于 numExchange」
        empty -= numExchange;                   // empty累减 numExchange
        ++numExchange;                          // 加一 numExchange;
        ++drunk;                                // 加一 drunk;
        ++empty;                                // 加一 empty;
    }
    return drunk; // 返回 drunk
}
int main() {
    assert(maxBottlesDrunk(10, 3) == 13);
    assert(maxBottlesDrunk(1, 2) == 1);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS