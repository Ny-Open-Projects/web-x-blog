// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
// LeetCode 116567013. PM — C++ 版（方案1：Brute-Force 主串指针回退）
#include <iostream> // 引入头文件
#include <string>   // 引入头文件

static long long match_v1(const std::string &p, const std::string &t) {
    long long n = t.size(), m = p.size(); // 把 另一字符串.大小(), 映射表 赋值为 节点.大小() 存入 元素个数
    long long i = 0, j = 0; // 把 0, 下标 j 赋值为 0 存入 下标 i
    while (j < m && i < n) { // 循环，直到不满足「下标 j 小于 映射表 且 下标 i 小于 元素个数」
        if (t[i] == p[j]) { // 若 另一字符串[下标 i] 等于 节点[下标 j]
            ++i;
            ++j;        // 加一 下标 i; 加一 下标 j;
        } else {        // 否则
            i -= j - 1; // 主串回退到本次对齐的下一位置
            j = 0;      // 把 0; 写入 下标 j
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
        {"people", T, 29}, {"good", T, 24}, {"xyz", T, -1}, {"a", "", -1}, // 边界：空文本
        {"is", T, 4},
    };
    for (int idx = 0; idx < 5; ++idx) { // 让 idx 从 0 开始计数，idx 小于 5 就继续
        long long got = match_v1(
            cases[idx].p, cases[idx].t); // 把 match_v1(cases[idx].节点, cases[idx].另一字符串) 存入 got
        if (got != cases[idx].want) {                              // 若 got 不等于 cases[idx].want
            std::cout << "case " << idx << " failed" << std::endl; // 打印输出
            return 1;                                              // 返回 1
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
