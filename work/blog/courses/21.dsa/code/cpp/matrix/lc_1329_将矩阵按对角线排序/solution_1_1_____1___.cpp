// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381786
// LeetCode 1329. 将矩阵按对角线排序 — C++ 版
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <map>       // 引入头文件
#include <vector>    // 引入头文件

using Matrix = std::vector<std::vector<int>>; // 引入依赖

// 方案1：模拟 —— 按 r-c 分组收集对角线，升序排序，写回时按 shift（取队首）取值
// 按值传参等价于 TS 事实源中 m.map(r => r.slice()) 的深拷贝
Matrix diagonalSort(Matrix mat) { // 定义函数/方法 diagonalSort
    size_t rows = mat.size(),
           cols = mat[0].size(); // 把 mat.大小(), 列数 赋值为 mat[0].大小(); 写入 size_t rows
    std::map<int, std::vector<int>> diags; // std::映射表 小于 int, std::vector 小于 int 超过 超过 diags;
    for (size_t r = 0; r < rows; ++r) // 让 右指针 从 0 开始计数，右指针 小于 行数 就继续
        for (size_t c = 0; c < cols; ++c) // 让 字符 从 0 开始计数，字符 小于 列数 就继续
            diags[static_cast<int>(r) - static_cast<int>(c)].push_back(mat[r][c]);
    for (auto &kv : diags)                             // 逐个取出 diags 的元素（kv）
        std::sort(kv.second.begin(), kv.second.end()); // std::sort(kv.second 迭代位置 , kv.second.终点());
    std::map<int, size_t> pos;                         // std::映射表 小于 int, size_t 超过 pos;
    for (size_t r = 0; r < rows; ++r) // 让 右指针 从 0 开始计数，右指针 小于 行数 就继续
        for (size_t c = 0; c < cols; ++c) { // 让 字符 从 0 开始计数，字符 小于 列数 就继续
            int key = static_cast<int>(r) - static_cast<int>(c);
            mat[r][c] = diags[key][pos[key]++]; // 把 diags[key][pos[key] 加一 ]; 写入 mat[r][c]
        }
    return mat; // 返回 mat
}

int main() { // 程序入口：跑内嵌自测用例
    // 与 TS 事实源内嵌用例一致
    Matrix m = {{3, 3, 1, 1},
                {2, 2, 1, 2},
                {1, 1, 1, 2}}; // 把 {{3, 3, 1, 1}, {2, 2, 1, 2}, {1, 1, 1, 2}}; 写入 Matrix m
    Matrix exp = {{1, 1, 1, 1},
                  {1, 2, 2, 2},
                  {1, 2, 3, 3}};      // 把 {{1, 1, 1, 1}, {1, 2, 2, 2}, {1, 2, 3, 3}}; 写入 Matrix exp
    Matrix got = diagonalSort(m);     // 把 diagonalSort(映射表); 写入 Matrix got
    assert(got == exp && "FAILED");   // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
