// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134026430
// LeetCode 54. 螺旋矩阵 — C++ 版
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

// 四边界逐层收缩（与 TS 事实源一致）
std::vector<int> spiralOrder(const std::vector<std::vector<int>> &matrix) {
    if (matrix.empty() || matrix[0].empty())
        return {};           // 若 矩阵 是否为空 或 矩阵[0] 是否为空，直接返回 {}
    std::vector<int> result; // std::vector 小于 int 超过 结果;
    long top = 0, bottom = static_cast<long>(matrix.size()) - 1;
    long left = 0, right = static_cast<long>(matrix[0].size()) - 1;
    while (top <= bottom && left <= right) { // 循环，直到不满足「top 不超过 bottom 且 左边界 不超过 右边界」
        for (long i = left; i <= right; ++i)
            result.push_back(matrix[top][i]);
        ++top; // 加一 top;
        for (long i = top; i <= bottom; ++i)
            result.push_back(matrix[i][right]);
        --right;             // 减一 右边界;
        if (top <= bottom) { // 若 top 不超过 bottom
            for (long i = right; i >= left; --i)
                result.push_back(matrix[bottom][i]);
            --bottom; // 减一 bottom;
        }
        if (left <= right) { // 若 左边界 不超过 右边界
            for (long i = bottom; i >= top; --i)
                result.push_back(matrix[i][left]);
            ++left; // 加一 左边界;
        }
    }
    return result; // 返回 结果
}

int main() { // 程序入口：跑内嵌自测用例
    // 与 TS 事实源内嵌用例一致：3x3 螺旋
    std::vector<int> exp = {1, 2, 3, 6, 9,
                            8, 7, 4, 5}; // 把 {1, 2, 3, 6, 9, 8, 7, 4, 5}; 写入 std::vector<int> exp
    auto got = spiralOrder(
        {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}); // 把 spiralOrder({{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}) 存入 got
    assert(got == exp && "FAILED");         // 断言校验
    std::cout << "PASS" << std::endl;       // 全部用例通过，输出 PASS
    return 0;                               // 返回 0
}
