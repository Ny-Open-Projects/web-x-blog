// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107836586
// LeetCode 107836586. Big-O 记号 — C++ 版（Big-O 记号：按最高次非零系数给出多项式复杂度分类）
#include <iostream> // 引入头文件
#include <string>   // 引入头文件
#include <vector>   // 引入头文件

// coeffs[i] 为 n^i 的系数，返回最高次非零项对应的复杂度记号
static std::string classify(const std::vector<long long> &coeffs) {
    for (int deg = static_cast<int>(coeffs.size()) - 1; deg >= 0; --deg) {
        if (coeffs[deg] != 0) { // 若 coeffs[deg] 不等于 0
            if (deg > 1)
                return "O(n^" + std::to_string(deg) + ")";
            if (deg == 1)
                return "O(n)"; // 若 deg 等于 1，直接返回 「O(元素个数)」
            return "O(1)";     // 返回 「O(1)」
        }
    }
    return "O(1)"; // 返回 「O(1)」
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::pair<std::vector<long long>, std::string>> cases = {
        {{1, 0, 0, 0}, "O(1)"},
        {{0, 0, 0, 35}, "O(n^3)"},
        {{0, 0, 1, 0}, "O(n^2)"},
        {{0, 1, 0, 0}, "O(n)"},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) { // 让 idx 从 0 开始计数，idx 小于 cases.大小() 就继续
        std::string got = classify(cases[idx].first); // 把 classify(cases[idx].first); 写入 std::string got
        if (got != cases[idx].second) {               // 若 got 不等于 cases[idx].second
            std::cout << "case " << idx << " failed: got " << got << " want " << cases[idx].second
                      << std::endl; // 打印输出
            return 1;               // 返回 1
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
