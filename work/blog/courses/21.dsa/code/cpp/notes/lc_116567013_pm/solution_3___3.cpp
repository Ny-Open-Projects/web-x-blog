// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
// LeetCode 116567013. PM — C++ 版（方案3：KMP，next 表失配大步跳跃）
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

static long long kmp_match(const std::string &p, const std::string &t) {
    std::vector<long long> N = build_next(p); // 把 build_next(节点); 写入 std::vector<long long> N
    long long n = t.size(), m = p.size(); // 把 另一字符串.大小(), 映射表 赋值为 节点.大小() 存入 元素个数
    long long i = 0, j = 0; // 把 0, 下标 j 赋值为 0 存入 下标 i
    while (j < m && i < n) { // 循环，直到不满足「下标 j 小于 映射表 且 下标 i 小于 元素个数」
        if (j < 0 || t[i] == p[j]) { // 若 下标 j 小于 0 或 另一字符串[下标 i] 等于 节点[下标 j]
            ++i;
            ++j;      // 加一 下标 i; 加一 下标 j;
        } else {      // 否则
            j = N[j]; // 把 N[下标 j]; 写入 下标 j
        }
    }
    return j == m ? i - j : -1; // 返回 下标 j 等于 映射表 ? 下标 i 减 下标 j : 减 1
}

int main() { // 程序入口：跑内嵌自测用例
    std::string T = "now is the time for all good people to come";
    struct Case {
        std::string p, t;
        long long want;
    }; // 定义类型
    Case cases[] = {
        // 把 { 写入 Case cases[]
        {"people", T, 29}, {"all", T, 20}, {"no", T, 0}, {"xyz", T, -1}, {"a", "", -1},
    };
    for (int idx = 0; idx < 5; ++idx) { // 让 idx 从 0 开始计数，idx 小于 5 就继续
        if (kmp_match(cases[idx].p, cases[idx].t) != cases[idx].want) {
            std::cout << "case " << idx << " failed" << std::endl; // 打印输出
            return 1;                                              // 返回 1
        }
    }
    if (kmp_match("aaaa", "aaaaa") != 0) {
        std::cout << "overlap failed" << std::endl;
        return 1;
    }
    if (kmp_match("aaab", "aaabaaa") != 0) {
        std::cout << "reuse failed" << std::endl;
        return 1;
    }

    auto check_next = [](const std::string &p, const std::vector<long long> &want) {
        return build_next(p) == want; // 返回 build_next(节点) 等于 want
    };
    if (!check_next("ababaca", {-1, 0, 0, 1, 2, 3, 0})) {
        std::cout << "next ababaca failed" << std::endl;
        return 1;
    }
    if (!check_next("aaaa", {-1, 0, 1, 2})) {
        std::cout << "next aaaa failed" << std::endl;
        return 1;
    }
    if (!check_next("abcd", {-1, 0, 0, 0})) {
        std::cout << "next abcd failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
