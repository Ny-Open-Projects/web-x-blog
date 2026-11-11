// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134032039
// LeetCode 48. 旋转矩阵 — C++ 版
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <utility>  // 引入头文件
#include <vector>   // 引入头文件

using Matrix = std::vector<std::vector<int>>; // 引入依赖

// 方案2：先上下翻转行（交换行向量），再沿主对角线转置（原地修改）
void rotate(Matrix &matrix) { // 定义函数/方法 rotate
    size_t n = matrix.size(); // 把 矩阵.大小(); 写入 size_t n
    for (size_t i = 0; i < n / 2; ++i) // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 除以 2 就继续
        std::swap(matrix[i], matrix[n - 1 - i]); // 交换整行
    for (size_t i = 0; i < n; ++i) // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (size_t j = 0; j < i; ++j) // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
            std::swap(matrix[i][j], matrix[j][i]); // 交换 矩阵[下标 i][下标 j] 与 矩阵[下标 j][下标 i]
}

static bool eq_matrix(const Matrix &a, const Matrix &b) { // 定义函数/方法 eq_matrix
    if (a.size() != b.size())
        return false;                       // 若 数组.大小() 不等于 b.大小()，直接返回 false
    for (size_t i = 0; i < a.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
        if (a[i].size() != b[i].size())
            return false; // 若 数组[下标 i].大小() 不等于 b[下标 i].大小()，直接返回 false
        for (size_t j = 0; j < a[i].size();
             ++j) // 让 下标 j 从 0 开始计数，下标 j 小于 数组[下标 i].大小() 就继续
            if (a[i][j] != b[i][j])
                return false; // 若 数组[下标 i][下标 j] 不等于 b[下标 i][下标 j]，直接返回 false
    }
    return true; // 返回 true
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::pair<Matrix, Matrix>> cases = {
        // 把 { 写入 std::vector<std::pair<Matrix, Matrix>> cases
        {{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, {{7, 4, 1}, {8, 5, 2}, {9, 6, 3}}},
        {{{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}},
         {{15, 13, 2, 5}, {14, 3, 4, 1}, {12, 6, 8, 9}, {16, 7, 10, 11}}},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) { // 让 idx 从 0 开始计数，idx 小于 cases.大小() 就继续
        rotate(cases[idx].first);                     // rotate(cases[idx].first);
        assert(eq_matrix(cases[idx].first, cases[idx].second) && "case failed"); // 断言校验
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
