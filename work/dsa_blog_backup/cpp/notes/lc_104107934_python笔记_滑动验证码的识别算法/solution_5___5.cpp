// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — C++ 版（方案5：边缘匹配 findGap 响应曲线）
#include <cmath>    // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

static std::vector<bool> detect_edges(const std::vector<int> &image) {
    std::vector<bool> edges(image.size(), false); // std::vector 小于 bool 超过 边集(image.大小(), false);
    for (size_t i = 1; i < image.size(); ++i) { // 让 下标 i 从 1 开始计数，下标 i 小于 image.大小() 就继续
        edges[i] = std::abs(image[i] - image[i - 1]) > 50;
    }
    return edges; // 返回 边集
}

static std::pair<int, std::vector<long long>> find_gap(const std::vector<int> &bg,
                                                       const std::vector<int> &puzzle) {
    auto bg_edges = detect_edges(bg);         // 把 detect_edges(bg) 存入 bg_edges
    auto puzzle_edges = detect_edges(puzzle); // 把 detect_edges(puzzle) 存入 puzzle_edges
    std::vector<long long> responses;         // std::vector 小于 long long 超过 responses;
    for (size_t x = 0; x + puzzle.size() <= bg.size();
         ++x) { // 让 x 从 0 开始计数，x 加 puzzle.大小() 不超过 bg.大小() 就继续
        long long score = 0;                         // 把 0 存入 score
        for (size_t y = 0; y < puzzle.size(); ++y) { // 让 y 从 0 开始计数，y 小于 puzzle.大小() 就继续
            if (bg_edges[x + y] && puzzle_edges[y])
                ++score; // 若 bg_edges[x 加 y] 且 puzzle_edges[y]) 加一 score;
        }
        responses.push_back(score); // responses 追加 score);
    }
    int best_x = 0; // 把 0 存入 best_x
    for (size_t i = 1; i < responses.size();
         ++i) { // 让 下标 i 从 1 开始计数，下标 i 小于 responses.大小() 就继续
        if (responses[i] > responses[best_x])
            best_x = static_cast<int>(i);
    }
    return {best_x, responses}; // 返回 {best_x, responses}
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<int> bg = {10, 10, 10, 10, 200, 200, 200, 200};
    std::vector<int> puzzle = {10, 200, 200, 200}; // 把 {10, 200, 200, 200}; 写入 std::vector<int> puzzle
    auto [bx, resp] = find_gap(bg, puzzle);        // 把 find_gap(bg, puzzle); 写入 auto [bx, resp]
    if (bx != 3) {
        std::cout << "gap failed" << std::endl;
        return 1;
    }
    if (resp != std::vector<long long>({0, 0, 0, 1, 0})) {
        std::cout << "responses failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
