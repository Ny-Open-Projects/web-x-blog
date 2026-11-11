// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — C++ 版（方案4：八皇后显式栈迭代）
#include <cmath>    // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

static bool valid(int x, const std::vector<int> &a) { // 定义函数/方法 valid
    int y = static_cast<int>(a.size()) + 1; // 把 static_cast 小于 int 超过 (数组.大小()) 加 1 存入 y
    for (int i = 1; i <= static_cast<int>(a.size());
         ++i) { // 让 下标 i 从 1 开始计数，下标 i 不超过 static_cast 小于 int 超过 (数组.大小()) 就继续
        if (x == a[i - 1] || std::abs(y - i) == std::abs(x - a[i - 1]))
            return false;
    }
    return true; // 返回 true
}

static std::vector<std::vector<int>> n_queens_stack(int n) {
    std::vector<std::vector<int>> solutions; // std::vector 小于 std::vector 小于 int 超过 超过 solutions;
    std::vector<std::vector<int>> stack{{}}; // std::vector 小于 std::vector 小于 int 超过 超过 栈{ {} };
    while (!stack.empty()) {                 // 循环，直到不满足「取反 栈.empty(」
        std::vector<int> a = stack.back(); // 把 栈.back(); 写入 std::vector<int> a
        stack.pop_back();                  // 弹出栈顶元素
        if (static_cast<int>(a.size()) == n) { // 若 static_cast 小于 int 超过 (数组.大小()) 等于 元素个数
            solutions.push_back(a);            // solutions 追加 数组);
        } else {                               // 否则
            for (int i = 1; i <= n; ++i) { // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
                if (valid(i, a)) {          // 若 valid(下标 i, 数组
                    std::vector<int> b = a; // 把 数组; 写入 std::vector<int> b
                    b.push_back(i);         // b 追加 下标 i);
                    stack.push_back(b);     // 栈 追加 b);
                }
            }
        }
    }
    return solutions; // 返回 solutions
}

int main() { // 程序入口：跑内嵌自测用例
    struct Case {
        int n;
        int count;
        bool has_first;
        std::vector<int> first;
    }; // 定义类型
    std::vector<Case> cases = {
        // 把 { 写入 std::vector<Case> cases
        {8, 92, true, {8, 4, 1, 3, 6, 2, 7, 5}},
        {1, 1, true, {1}},
        {2, 0, false, {}},
        {4, 2, true, {3, 1, 4, 2}},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) { // 让 idx 从 0 开始计数，idx 小于 cases.大小() 就继续
        auto sols = n_queens_stack(cases[idx].n); // 把 n_queens_stack(cases[idx].元素个数) 存入 sols
        if (static_cast<int>(sols.size()) != cases[idx].count) {
            std::cout << "case " << idx << " count" << std::endl;
            return 1;
        }
        if (cases[idx].has_first && sols[0] != cases[idx].first) {
            std::cout << "case " << idx << " first" << std::endl;
            return 1;
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
