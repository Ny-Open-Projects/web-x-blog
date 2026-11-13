// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
// LeetCode 116567013. PM — C++ 版（方案2：Brute-Force 双循环对齐）
#include <iostream> // 引入头文件
#include <string>   // 引入头文件

static long long match_v2(const std::string &p, const std::string &t) {
    long long n = t.size(), m = p.size(); // 把 另一字符串.大小(), 映射表 赋值为 节点.大小() 存入 元素个数
    if (m == 0 || n < m)
        return -1; // 若 映射表 等于 0 或 元素个数 小于 映射表，直接返回 减 1
    for (long long i = 0; i <= n - m;
         ++i) { // 让 下标 i 从 0 开始计数，下标 i 不超过 元素个数 减 映射表 就继续
        long long j = 0; // 把 0 存入 下标 j
        while (j < m && t[i + j] == p[j])
            ++j;
        if (j == m)
            return i; // 若 下标 j 等于 映射表，直接返回 下标 i
    }
    return -1; // 返回 减 1
}

int main() { // 程序入口：跑内嵌自测用例
    std::string T = "now is the time for all good people to come";
    struct Case {
        std::string p, t;
        long long want;
    }; // 定义类型
    Case cases[] = {
        // 把 { 写入 Case cases[]
        {"people", T, 29}, {"time", T, 11}, {"all", T, 20}, {"xyz", T, -1}, {"a", "", -1}, {"is", T, 4},
    };
    for (int idx = 0; idx < 6; ++idx) { // 让 idx 从 0 开始计数，idx 小于 6 就继续
        if (match_v2(cases[idx].p, cases[idx].t) != cases[idx].want) {
            std::cout << "case " << idx << " failed" << std::endl; // 打印输出
            return 1;                                              // 返回 1
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
