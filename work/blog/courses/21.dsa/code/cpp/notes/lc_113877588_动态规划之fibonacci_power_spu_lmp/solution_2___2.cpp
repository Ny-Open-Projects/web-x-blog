// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588
// 动态规划之Fibonacci — C++ 版（方案2）
#include <cassert>                           // 引入头文件
#include <iostream>                          // 引入头文件
#include <unordered_map>                     // 引入头文件
static long long fibMemo(int n) {            // static long long fibMemo(int 元素个数) {
    std::unordered_map<int, long long> memo; // std::unordered_map 小于 int, long long 超过 记忆化表;
    std::function<long long(int)> go = [&](int k) -> long long {
        if (k <= 1)
            return k; // 若 下标 k 不超过 1，直接返回 下标 k
        if (memo.count(k))
            return memo[k]; // 若 记忆化表.计数(下标 k)，直接返回 记忆化表[下标 k]
        return memo[k] =
                   go(k - 1) + go(k - 2); // 返回 记忆化表[下标 k] 赋值为 go(下标 k 减 1) 加 go(下标 k 减 2)
    };
    return go(n); // 返回 go(元素个数)
}
int main() {
    assert(fibMemo(10) == 55);
    assert(fibMemo(20) == 6765);
    assert(fibMemo(0) == 0);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS