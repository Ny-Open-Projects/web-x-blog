// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — C++ 版（方案7：合成数据 + 识别全流程）
#include <algorithm> // 引入头文件
#include <cmath>     // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件

static std::vector<bool> detect_edges(const std::vector<int> &image) {
    std::vector<bool> edges(image.size(), false); // std::vector 小于 bool 超过 边集(image.大小(), false);
    for (size_t i = 1; i < image.size(); ++i) { // 让 下标 i 从 1 开始计数，下标 i 小于 image.大小() 就继续
        edges[i] = std::abs(image[i] - image[i - 1]) > 50;
    }
    return edges; // 返回 边集
}

static int recognize_captcha(const std::vector<int> &bg,
                             const std::vector<int> &puzzle) { // 定义函数/方法 recognize_captcha
    auto bg_edges = detect_edges(bg);                          // 把 detect_edges(bg) 存入 bg_edges
    auto puzzle_edges = detect_edges(puzzle);                  // 把 detect_edges(puzzle) 存入 puzzle_edges
    int best_x = 0;                                            // 把 0 存入 best_x
    long long best_score = -1;                                 // 把 减 1 存入 best_score
    for (size_t x = 0; x + puzzle.size() <= bg.size();
         ++x) { // 让 x 从 0 开始计数，x 加 puzzle.大小() 不超过 bg.大小() 就继续
        long long score = 0;                         // 把 0 存入 score
        for (size_t y = 0; y < puzzle.size(); ++y) { // 让 y 从 0 开始计数，y 小于 puzzle.大小() 就继续
            if (bg_edges[x + y] && puzzle_edges[y])
                ++score; // 若 bg_edges[x 加 y] 且 puzzle_edges[y]) 加一 score;
        }
        if (score > best_score) {
            best_score = score;
            best_x = static_cast<int>(x);
        }
    }
    return best_x; // 返回 best_x
}

static std::pair<std::vector<int>, std::vector<int>> build_synthetic(int bg_len, int gap_start,
                                                                     int puzzle_len) {
    std::vector<int> bg(bg_len, 10); // std::vector 小于 int 超过 bg(bg_len, 10);
    for (int i = gap_start; i < std::min(gap_start + puzzle_len, bg_len); ++i)
        bg[i] = 200;
    std::vector<int> puzzle(bg.begin() + gap_start, bg.begin() + std::min(gap_start + puzzle_len, bg_len));
    return {bg, puzzle}; // 返回 {bg, puzzle}
}

int main() {                                      // 程序入口：跑内嵌自测用例
    auto [bg, puzzle] = build_synthetic(8, 3, 4); // 把 build_synthetic(8, 3, 4); 写入 auto [bg, puzzle]
    // 与 TS 原文件一致：合成数据下 puzzle 边缘全平，识别结果为 0
    if (recognize_captcha(bg, puzzle) != 0) {
        std::cout << "synthetic failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
