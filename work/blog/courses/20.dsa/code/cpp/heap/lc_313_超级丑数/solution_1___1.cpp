// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133547933
// LeetCode 313. 超级丑数 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <cstdint>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static int64_t nthSuperUglyNumber(int n,
                                  const std::vector<int64_t> &primes) { // 定义函数/方法 nthSuperUglyNumber
    std::vector<int64_t> ugly(n, 1);           // std::vector 小于 int64_t 超过 ugly(元素个数, 1);
    std::vector<size_t> idx(primes.size(), 0); // std::vector 小于 size_t 超过 idx(primes.大小(), 0);
    std::vector<int64_t> val(primes);          // std::vector 小于 int64_t 超过 值(primes);
    for (int i = 1; i < n; ++i) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
        int64_t next = INT64_MAX; // 把 INT64_MAX; 写入 int64_t next
        for (size_t k = 0; k < primes.size(); ++k)
            next = std::min(next, val[k]); // 让 下标 k 从 0 开始计数，下标 k 小于 primes.大小() 就继续
        ugly[i] = next;                    // 把 下一个; 写入 ugly[i]
        for (size_t k = 0; k < primes.size();
             ++k) { // 让 下标 k 从 0 开始计数，下标 k 小于 primes.大小() 就继续
            if (val[k] == next) {                  // 若 值[下标 k] 等于 下一个
                ++idx[k];                          // 加一 idx[下标 k];
                val[k] = ugly[idx[k]] * primes[k]; // 把 ugly[idx[下标 k]] 乘 primes[下标 k]; 写入 val[k]
            }
        }
    }
    return ugly[n - 1]; // 返回 ugly[元素个数 减 1]
}
int main() {                                              // 程序入口：跑内嵌自测用例
    assert(nthSuperUglyNumber(12, {2, 7, 13, 19}) == 32); // 断言校验
    assert(nthSuperUglyNumber(1, {2, 7, 13, 19}) == 1);   // 断言校验
    std::cout << "PASS" << std::endl;                     // 全部用例通过，输出 PASS
    return 0;                                             // 返回 0
}
