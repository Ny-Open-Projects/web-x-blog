// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — C++ 版（方案2：Sobel 中心差分边缘 + 匹配）
#include <cmath>    // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

static std::vector<bool> detect_edges_sobel(const std::vector<int> &image) {
    int n = static_cast<int>(image.size()); // 把 static_cast 小于 int 超过 (image.大小()) 存入 元素个数
    std::vector<bool> edges(n, false); // std::vector 小于 bool 超过 边集(元素个数, false);
    if (n < 2)
        return edges; // 若 元素个数 小于 2，直接返回 边集
    edges[0] =
        std::abs(image[1] - image[0]) > 50; // 把 std::取绝对值 image[1] 减 image[0]) 超过 50; 写入 edges[0]
    for (int i = 1; i < n - 1; ++i) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 减 1 就继续
        edges[i] = std::abs(image[i + 1] - image[i - 1]) > 50;
    }
    edges[n - 1] = std::abs(image[n - 1] - image[n - 2]) > 50;
    return edges; // 返回 边集
}

static int recognize_captcha(const std::vector<int> &bg,
                             const std::vector<int> &puzzle) { // 定义函数/方法 recognize_captcha
    auto bg_edges = detect_edges_sobel(bg);                    // 把 detect_edges_sobel(bg) 存入 bg_edges
    auto puzzle_edges = detect_edges_sobel(puzzle); // 把 detect_edges_sobel(puzzle) 存入 puzzle_edges
    int best_x = 0;                                 // 把 0 存入 best_x
    long long best_score = -1;                      // 把 减 1 存入 best_score
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

int main() { // 程序入口：跑内嵌自测用例
    std::vector<int> bg = {10, 10, 10, 10, 200, 200, 200, 200};
    std::vector<int> puzzle = {10, 200, 200, 200}; // 把 {10, 200, 200, 200}; 写入 std::vector<int> puzzle
    if (recognize_captcha(bg, puzzle) != 3) {
        std::cout << "gap failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
