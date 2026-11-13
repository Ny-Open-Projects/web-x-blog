// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
// LeetCode 110240695. 分治策略之 greatest slice — C++ 版（方案A：暴力枚举所有子段）
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

static long long max_sub_array_bf(const std::vector<int> &arr) {
    long long best = 0;                       // 把 0 存入 当前最优
    bool first = true;                        // 把 true 存入 first
    for (size_t i = 0; i < arr.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
        long long s = 0;                      // 把 0 存入 字符串
        for (size_t j = i; j < arr.size();
             ++j) {      // 让 下标 j 从 下标 i 开始计数，下标 j 小于 数组.大小() 就继续
            s += arr[j]; // 字符串累加 数组[下标 j]
            if (first || s > best) {
                best = s;
                first = false;
            } // 若 first 或 字符串 超过 当前最优) { 当前最优 赋值为 字符串; first 赋值为 false; }
        }
    }
    return best; // 返回 当前最优
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::pair<std::vector<int>, long long>> cases = {
        {{-2, 1, -3, 4, -1, 2, 1, -5, 4}, 6},
        {{1}, 1},
        {{-1, -2, -3}, -1},
        {{5, 4, -1, 7, 8}, 23},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) { // 让 idx 从 0 开始计数，idx 小于 cases.大小() 就继续
        if (max_sub_array_bf(cases[idx].first) !=
            cases[idx].second) { // 若 max_sub_array_bf(cases[idx].first) 不等于 cases[idx].second
            std::cout << "case " << idx << " failed" << std::endl; // 打印输出
            return 1;                                              // 返回 1
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
