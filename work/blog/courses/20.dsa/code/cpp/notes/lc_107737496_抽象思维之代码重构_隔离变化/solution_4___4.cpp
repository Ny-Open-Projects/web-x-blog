// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案4：螺旋矩阵方向模拟 placeFill）
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

static std::vector<std::vector<int>> place_fill(int n) {
    std::vector<std::vector<int>> m(n, std::vector<int>(n, 0));
    int row = 0, col = 0;       // 把 0, col 赋值为 0 存入 row
    char direction = 'D';       // 把 'D'; 写入 char direction
    int num = 1;                // 把 1 存入 num
    int total = n * n;          // 把 元素个数 乘 元素个数 存入 总和
    while (num <= total) {      // 循环，直到不满足「num 不超过 总和」
        m[row][col] = num;      // 把 num; 写入 m[row][col]
        ++num;                  // 加一 num;
        if (direction == 'D') { // 若 direction 等于 'D'
            if (row + 1 < n && m[row + 1][col] == 0)
                ++row; // 若 row 加 1 小于 元素个数 且 映射表[row 加 1][col] 等于 0) 加一 row;
            else {
                direction = 'R';
                ++col;
            }                          // 否则
        } else if (direction == 'R') { // 否则，若 direction 等于 'R'
            if (col + 1 < n && m[row][col + 1] == 0)
                ++col; // 若 col 加 1 小于 元素个数 且 映射表[row][col 加 1] 等于 0) 加一 col;
            else {
                direction = 'U';
                --row;
            }                          // 否则
        } else if (direction == 'U') { // 否则，若 direction 等于 'U'
            if (row - 1 >= 0 && m[row - 1][col] == 0)
                --row; // 若 row 减 1 不低于 0 且 映射表[row 减 1][col] 等于 0) 减一 row;
            else {
                direction = 'L';
                --col;
            }    // 否则
        } else { // 否则
            if (col - 1 >= 0 && m[row][col - 1] == 0)
                --col; // 若 col 减 1 不低于 0 且 映射表[row][col 减 1] 等于 0) 减一 col;
            else {
                direction = 'D';
                ++row;
            } // 否则
        }
    }
    return m; // 返回 映射表
}

int main() {                   // 程序入口：跑内嵌自测用例
    auto got3 = place_fill(3); // 把 place_fill(3) 存入 got3
    if (got3 != std::vector<std::vector<int>>({{1, 8, 7}, {2, 9, 6}, {3, 4, 5}})) {
        std::cout << "place3 failed" << std::endl; // 打印输出
        return 1;                                  // 返回 1
    }
    auto got4 = place_fill(4); // 把 place_fill(4) 存入 got4
    if (got4 !=
        std::vector<std::vector<int>>({{1, 12, 11, 10}, {2, 13, 16, 9}, {3, 14, 15, 8}, {4, 5, 6, 7}})) {
        std::cout << "place4 failed" << std::endl; // 打印输出
        return 1;                                  // 返回 1
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
