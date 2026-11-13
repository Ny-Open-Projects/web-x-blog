// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — C++ 版（方案6：合成滑块数据 buildSynthetic）
#include <algorithm> // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件

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
    if (bg != std::vector<int>({10, 10, 10, 200, 200, 200, 200, 10})) {
        std::cout << "bg failed" << std::endl;
        return 1;
    }
    if (puzzle != std::vector<int>({200, 200, 200, 200})) {
        std::cout << "puzzle failed" << std::endl;
        return 1;
    }
    if (puzzle.size() != 4 || bg.size() != 8) {
        std::cout << "lens failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
