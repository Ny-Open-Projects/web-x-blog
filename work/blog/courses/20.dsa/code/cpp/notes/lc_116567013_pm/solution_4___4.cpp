// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
// LeetCode 116567013. PM — C++ 版（方案4：buildNext 单测）
#include <iostream> // 引入头文件
#include <string>   // 引入头文件
#include <vector>   // 引入头文件

static std::vector<long long> build_next(const std::string &p) {
    long long m =
        static_cast<long long>(p.size()); // 把 static_cast 小于 long long 超过 (节点.大小()) 存入 映射表
    std::vector<long long> N(m, -1); // std::vector 小于 long long 超过 N(映射表, 减 1);
    long long j = 0, t = -1;         // 把 0, 另一字符串 赋值为 减 1 存入 下标 j
    while (j < m - 1) {              // 循环，直到不满足「下标 j 小于 映射表 减 1」
        if (t < 0 || p[j] == p[t]) { // 若 另一字符串 小于 0 或 节点[下标 j] 等于 节点[另一字符串]
            ++j;
            ++t;      // 加一 下标 j; 加一 另一字符串;
            N[j] = t; // 把 另一字符串; 写入 N[j]
        } else {      // 否则
            t = N[t]; // 把 N[另一字符串]; 写入 另一字符串
        }
    }
    return N; // 返回 N
}

int main() { // 程序入口：跑内嵌自测用例
    if (build_next("ababaca") != std::vector<long long>({-1, 0, 0, 1, 2, 3, 0})) {
        std::cout << "ababaca failed" << std::endl;
        return 1;
    }
    if (build_next("aaaa") != std::vector<long long>({-1, 0, 1, 2})) {
        std::cout << "aaaa failed" << std::endl;
        return 1;
    }
    if (build_next("abcabc") != std::vector<long long>({-1, 0, 0, 0, 1, 2})) {
        std::cout << "abcabc failed" << std::endl;
        return 1;
    }
    if (build_next("abcd") != std::vector<long long>({-1, 0, 0, 0})) {
        std::cout << "abcd failed" << std::endl;
        return 1;
    }
    if (build_next("a") != std::vector<long long>({-1})) {
        std::cout << "a failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
