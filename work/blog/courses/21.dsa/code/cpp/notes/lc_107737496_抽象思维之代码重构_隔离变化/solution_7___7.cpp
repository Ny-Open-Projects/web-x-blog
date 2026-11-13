// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案7：螺旋矩阵分派表 place）
#include <functional> // 引入头文件
#include <iostream>   // 引入头文件
#include <map>        // 引入头文件
#include <vector>     // 引入头文件

static std::vector<int> place(int row, int col, char direction, int n,
                              const std::vector<std::vector<int>> &m) { // const std::vector 小于 std::vector
                                                                        // 小于 int 超过 超过 按位与 映射表) {
    // 返回 {row, col} 或 {row, col, direction}（长度 3 表示转向）
    std::map<char, std::function<std::vector<int>()>> handlers = {
        {'D',
         [&]() -> std::vector<int> { // {'D', [ 按位与 ]() 减 超过 std::vector 小于 int 超过 {
             if (row + 1 < n && m[row + 1][col] == 0)
                 return {row + 1, col};
             return {row, col + 1, 'R'}; // 返回 {row, col 加 1, 'R'}
         }},
        {'R',
         [&]() -> std::vector<int> { // {'R', [ 按位与 ]() 减 超过 std::vector 小于 int 超过 {
             if (col + 1 < n && m[row][col + 1] == 0)
                 return {row, col + 1};
             return {row - 1, col, 'U'}; // 返回 {row 减 1, col, 'U'}
         }},
        {'U',
         [&]() -> std::vector<int> { // {'U', [ 按位与 ]() 减 超过 std::vector 小于 int 超过 {
             if (row - 1 >= 0 && m[row - 1][col] == 0)
                 return {
                     row - 1,
                     col}; // 若 row 减 1 不低于 0 且 映射表[row 减 1][col] 等于 0，直接返回 {row 减 1, col}
             return {row, col - 1, 'L'}; // 返回 {row, col 减 1, 'L'}
         }},
        {'L',
         [&]() -> std::vector<int> { // {'L', [ 按位与 ]() 减 超过 std::vector 小于 int 超过 {
             if (col - 1 >= 0 && m[row][col - 1] == 0)
                 return {
                     row,
                     col -
                         1}; // 若 col 减 1 不低于 0 且 映射表[row][col 减 1] 等于 0，直接返回 {row, col 减 1}
             return {row + 1, col, 'D'}; // 返回 {row 加 1, col, 'D'}
         }},
    };
    return handlers[direction](); // 返回 handlers[direction]()
}

static std::vector<std::vector<int>> fill_spiral(int n) {
    std::vector<std::vector<int>> m(n, std::vector<int>(n, 0));
    int row = 0, col = 0;  // 把 0, col 赋值为 0 存入 row
    char direction = 'D';  // 把 'D'; 写入 char direction
    int num = 1;           // 把 1 存入 num
    while (num <= n * n) { // 循环，直到不满足「num 不超过 元素个数 乘 元素个数」
        m[row][col] = num; // 把 num; 写入 m[row][col]
        ++num;             // 加一 num;
        auto res =
            place(row, col, direction, n, m); // 把 place(row, col, direction, 元素个数, 映射表) 存入 结果
        row = res[0];                         // 把 结果[0]; 写入 row
        col = res[1];                         // 把 结果[1]; 写入 col
        if (res.size() == 3)
            direction = static_cast<char>(res[2]);
    }
    return m; // 返回 映射表
}

int main() { // 程序入口：跑内嵌自测用例
    if (fill_spiral(3) != std::vector<std::vector<int>>({{1, 8, 7}, {2, 9, 6}, {3, 4, 5}})) {
        std::cout << "spiral3 failed" << std::endl; // 打印输出
        return 1;                                   // 返回 1
    }
    if (fill_spiral(4) !=
        std::vector<std::vector<int>>({{1, 12, 11, 10}, {2, 13, 16, 9}, {3, 14, 15, 8}, {4, 5, 6, 7}})) {
        std::cout << "spiral4 failed" << std::endl; // 打印输出
        return 1;                                   // 返回 1
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
