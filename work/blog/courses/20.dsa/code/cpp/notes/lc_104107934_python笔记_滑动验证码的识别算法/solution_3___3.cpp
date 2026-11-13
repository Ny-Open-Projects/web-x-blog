// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — C++ 版（方案3：NCC 归一化互相关）
#include <cmath>    // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

static int ncc_match(const std::vector<int> &bg, const std::vector<int> &puzzle) { // 定义函数/方法 ncc_match
    int best_x = 0;                                                                // 把 0 存入 best_x
    double best_score = -1.0 / 0.0;          // 把 减 1.0 除以 0.0 存入 best_score
    int n = static_cast<int>(puzzle.size()); // 把 static_cast 小于 int 超过 (puzzle.大小()) 存入 元素个数
    for (int x = 0; x + n <= static_cast<int>(bg.size()); ++x) {
        double bw = 0, pw = 0;        // 把 0, pw 赋值为 0 存入 bw
        for (int i = 0; i < n; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
            bw += bg[x + i];          // bw累加 bg[x 加 下标 i]
            pw += puzzle[i];          // pw累加 puzzle[下标 i]
        }
        bw /= n;                        // 把 元素个数; 写入 bw /
        pw /= n;                        // 把 元素个数; 写入 pw /
        double num = 0, db = 0, dp = 0; // 把 0, db 赋值为 0, DP 表 赋值为 0 存入 num
        for (int i = 0; i < n; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
            double a = bg[x + i] - bw; // 把 bg[x 加 下标 i] 减 bw 存入 数组
            double b = puzzle[i] - pw; // 把 puzzle[下标 i] 减 pw 存入 b
            num += a * b;              // num累加 数组 乘 b
            db += a * a;               // db累加 数组 乘 数组
            dp += b * b;               // DP 表累加 b 乘 b
        }
        double denom = std::sqrt(db) * std::sqrt(dp); // 把 std::sqrt(db) 乘 std::sqrt(DP 表) 存入 denom
        double score =
            (denom != 0.0) ? (num / denom) : 0.0; // 把 (denom 不等于 0.0) ? (num 除以 denom) : 0.0 存入 score
        if (score > best_score) {
            best_score = score;
            best_x = x;
        }
    }
    return best_x; // 返回 best_x
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<int> bg = {10, 10, 10, 10, 200, 200, 200, 200};
    std::vector<int> puzzle = {10, 200, 200, 200}; // 把 {10, 200, 200, 200}; 写入 std::vector<int> puzzle
    if (ncc_match(bg, puzzle) != 3) {
        std::cout << "gap failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
