// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133982215
// LeetCode 417. 太平洋大西洋水流问题 — C++ 版
#include <cassert>    // 引入头文件
#include <functional> // 引入头文件
#include <iostream>   // 引入头文件
#include <utility>    // 引入头文件
#include <vector>     // 引入头文件

using Cell = std::pair<int, int>; // 引入依赖

// 方案2（DFS 反向流动，从海洋边界出发）
std::vector<Cell> pacificAtlantic(const std::vector<std::vector<int>> *matrix) {
    if (matrix == nullptr || matrix->empty() ||
        (*matrix)[0].empty()) // 若 矩阵 等于 nullptr 或 矩阵 减 超过 empty() 或 ( 乘 矩阵)[0].empty(
        return {};            // 返回 {}
    const auto &mat = *matrix;            // 把 乘 矩阵; 写入 const auto &mat
    int m = static_cast<int>(mat.size()); // 把 static_cast 小于 int 超过 (mat.大小()) 存入 映射表
    int n = static_cast<int>(mat[0].size()); // 把 static_cast 小于 int 超过 (mat[0].大小()) 存入 元素个数
    std::vector<std::vector<bool>> pacific(m, std::vector<bool>(n, false));
    std::vector<std::vector<bool>> atlantic(m, std::vector<bool>(n, false));

    std::function<void(int, int, std::vector<std::vector<bool>> &)> dfs =
        [&](int r, int c, std::vector<std::vector<bool>> &flow) {
            flow[r][c] = true;               // 把 true; 写入 flow[r][c]
            const int dr[4] = {-1, 1, 0, 0}; // 把 { 减 1, 1, 0, 0}; 写入 const int dr[4]
            const int dc[4] = {0, 0, -1, 1}; // 把 {0, 0, 减 1, 1}; 写入 const int dc[4]
            for (int k = 0; k < 4; k++) {    // 让 下标 k 从 0 开始计数，下标 k 小于 4 就继续
                int nr = r + dr[k];          // 把 右指针 加 dr[下标 k] 存入 nr
                int nc = c + dc[k];          // 把 字符 加 dc[下标 k] 存入 nc
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !flow[nr][nc] &&
                    mat[nr][nc] >= mat[r][c]) { // 把 mat[右指针][字符]) { 写入 !flow[nr][nc] && mat[nr][nc] >
                    dfs(nr, nc, flow);          // dfs(nr, nc, flow);
                }
            }
        };

    for (int r = 0; r < m; r++) { // 让 右指针 从 0 开始计数，右指针 小于 映射表 就继续
        dfs(r, 0, pacific);       // dfs(右指针, 0, pacific);
        dfs(r, n - 1, atlantic);  // dfs(右指针, 元素个数 减 1, atlantic);
    }
    for (int c = 0; c < n; c++) { // 让 字符 从 0 开始计数，字符 小于 元素个数 就继续
        dfs(0, c, pacific);       // dfs(0, 字符, pacific);
        dfs(m - 1, c, atlantic);  // dfs(映射表 减 1, 字符, atlantic);
    }

    std::vector<Cell> res;          // std::vector 小于 Cell 超过 结果;
    for (int r = 0; r < m; r++)     // 让 右指针 从 0 开始计数，右指针 小于 映射表 就继续
        for (int c = 0; c < n; c++) // 让 字符 从 0 开始计数，字符 小于 元素个数 就继续
            if (pacific[r][c] && atlantic[r][c])
                res.emplace_back(r, c);
    return res; // 返回 结果
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::vector<int>> matrix = {
        // 把 { 写入 std::vector<std::vector<int>> matrix
        {1, 2, 2, 3, 5}, {3, 2, 3, 4, 4}, {2, 4, 5, 3, 1}, {6, 7, 1, 4, 5}, {5, 1, 1, 2, 4},
    };
    auto got = pacificAtlantic(&matrix); // 把 pacificAtlantic( 按位与 矩阵) 存入 got
    std::vector<Cell> expected = {
        // 把 { 写入 std::vector<Cell> expected
        {0, 4}, {1, 3}, {1, 4}, {2, 2}, {3, 0}, {3, 1}, {4, 0},
    };
    assert(got.size() == expected.size() && "length mismatch"); // 断言校验
    for (size_t i = 0; i < expected.size();
         i++) // 让 下标 i 从 0 开始计数，下标 i 小于 expected.大小() 就继续
        assert(got[i] == expected[i] && "cell mismatch"); // 断言校验
    std::cout << "PASS" << std::endl;                     // 全部用例通过，输出 PASS
    return 0;                                             // 返回 0
}
