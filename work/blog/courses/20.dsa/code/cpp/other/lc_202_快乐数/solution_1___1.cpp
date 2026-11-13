// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135124945
// LeetCode 202. 快乐数 — C++ 版（方案1）
#include <cassert>                           // 引入头文件
#include <iostream>                          // 引入头文件
#include <unordered_set>                     // 引入头文件
static long long bitSquareSum(long long n) { // static long long bitSquareSum(long long 元素个数) {
    long long s = 0;                         // 把 0 存入 字符串
    while (n > 0) {
        long long d = n % 10;
        s += d * d;
        n /= 10;
    }
    return s; // 返回 字符串
}
static bool isHappy(long long n) {      // 定义判定函数 isHappy
    std::unordered_set<long long> seen; // std::unordered_set 小于 long long 超过 已见集合;
    while (n != 1 && !seen.count(n)) { // 循环，直到不满足「元素个数 不等于 1 且 取反 已见集合.计数(元素个数」
        seen.insert(n);      // 已见集合 插入 元素个数);
        n = bitSquareSum(n); // 把 bitSquareSum(元素个数); 写入 元素个数
    }
    return n == 1; // 返回 元素个数 等于 1
}
int main() {                          // 程序入口：跑内嵌自测用例
    assert(bitSquareSum(1) == 1);     // 断言校验
    assert(bitSquareSum(19) == 82);   // 断言校验
    assert(bitSquareSum(82) == 68);   // 断言校验
    assert(isHappy(19));              // 断言校验
    assert(isHappy(1));               // 断言校验
    assert(!isHappy(2));              // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
