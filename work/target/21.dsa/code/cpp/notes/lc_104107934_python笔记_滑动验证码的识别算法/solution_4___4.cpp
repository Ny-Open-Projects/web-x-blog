// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — C++ 版（方案4：SAD 绝对差和最佳窗口）
#include <cmath>    // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

static std::pair<int, long long> best_match_window(const std::vector<int> &bg,
                                                   const std::vector<int> &puzzle) {
    int best_x = 0;                   // 把 0 存入 best_x
    long long best_score = 1LL << 60; // 把 1LL 小于 小于 60 存入 best_score
    int n = static_cast<int>(puzzle.size()); // 把 static_cast 小于 int 超过 (puzzle.大小()) 存入 元素个数
    for (int x = 0; x + n <= static_cast<int>(bg.size()); ++x) {
        long long score = 0; // 把 0 存入 score
        for (int y = 0; y < n; ++y)
            score += std::abs(bg[x + y] - puzzle[y]); // 让 y 从 0 开始计数，y 小于 元素个数 就继续
        if (score < best_score) {
            best_score = score;
            best_x = x;
        }
    }
    return {best_x, best_score}; // 返回 {best_x, best_score}
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<int> bg = {10, 10, 10, 10, 200, 200, 200, 200};
    std::vector<int> puzzle = {10, 200, 200, 200}; // 把 {10, 200, 200, 200}; 写入 std::vector<int> puzzle
    auto [bx, bs] = best_match_window(bg, puzzle); // 把 best_match_window(bg, puzzle); 写入 auto [bx, bs]
    if (bx != 3 || bs != 0) {
        std::cout << "gap failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
