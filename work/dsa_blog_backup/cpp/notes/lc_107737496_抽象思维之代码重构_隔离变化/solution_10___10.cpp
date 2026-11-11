// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案10：Filler+Matrix 组合 9x9 全螺旋）
#include <iostream> // 引入头文件
#include <sstream>  // 引入头文件
#include <string>   // 引入头文件
#include <vector>   // 引入头文件

class Filler { // 定义类型
  public:      // public:
    Filler(int rn, int cn)
        : rMax_(rn - 1), cMax_(cn - 1) {} // Filler(int rn, int cn) : rMax_(rn 减 1), cMax_(cn 减 1) {}
    std::pair<int, int> next() {          // std::pair 小于 int, int 超过 下一个() {
        std::pair<int, int> res{posRow_, posCol_}; // std::pair 小于 int, int 超过 结果{posRow_, posCol_};
        const std::string rule = "ESVM";           // 把 「ESVM」; 写入 const std::string rule
        char cmd = rule[idx_ % 4];                 // 把 rule[idx_ 对…取模 4]; 写入 char cmd
        if (cmd == 'E') {                          // 若 cmd 等于 'E'
            ++posRow_;                             // 加一 posRow_;
            if (posRow_ == rMax_) {
                ++idx_;
                ++cMin_;
            }                    // 若 posRow_ 等于 rMax_) { 加一 idx_; 加一 cMin_; }
        } else if (cmd == 'S') { // 否则，若 cmd 等于 'S'
            ++posCol_;           // 加一 posCol_;
            if (posCol_ == cMax_) {
                ++idx_;
                --rMax_;
            }                    // 若 posCol_ 等于 cMax_) { 加一 idx_; 减一 rMax_; }
        } else if (cmd == 'V') { // 否则，若 cmd 等于 'V'
            --posRow_;           // 减一 posRow_;
            if (posRow_ == rMin_) {
                ++idx_;
                --cMax_;
            }                    // 若 posRow_ 等于 rMin_) { 加一 idx_; 减一 cMax_; }
        } else if (cmd == 'M') { // 否则，若 cmd 等于 'M'
            --posCol_;           // 减一 posCol_;
            if (posCol_ == cMin_) {
                ++idx_;
                ++rMin_;
            } // 若 posCol_ 等于 cMin_) { 加一 idx_; 加一 rMin_; }
        }
        return res; // 返回 结果
    }

  private:                                  // private:
    int posRow_ = 0, posCol_ = 0, idx_ = 0; // 把 0, posCol_ 赋值为 0, idx_ 赋值为 0 存入 posRow_
    int rMin_ = 0, cMin_ = 0, rMax_, cMax_; // 把 0, cMin_ 赋值为 0, rMax_, cMax_ 存入 rMin_
};

static std::string fmt_row(const std::vector<int> &row) {
    std::ostringstream oss;                   // std::ostringstream oss;
    for (size_t i = 0; i < row.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 row.大小() 就继续
        if (i)
            oss << " "; // 若 下标 i) oss 小于 小于 「 」;
        oss.width(2);   // oss.width(2);
        oss << row[i];  // oss 小于 小于 row[下标 i];
    }
    return oss.str(); // 返回 oss.str()
}

int main() {                  // 程序入口：跑内嵌自测用例
    const int rn = 9, cn = 9; // 把 9, cn 赋值为 9; 写入 const int rn
    Filler obj(rn, cn);       // Filler obj(rn, cn);
    std::vector<std::vector<int>> m(rn, std::vector<int>(cn, 0));
    for (int i = 0; i < rn * cn; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 rn 乘 cn 就继续
        auto [r, c] = obj.next();       // 把 obj.下一个(); 写入 auto [r, c]
        m[r][c] = i + 1;                // 把 下标 i 加 1; 写入 m[r][c]
    }
    const char *want[9] = {
        // 把 { 写入 const char *want[9]
        " 1 32 31 30 29 28 27 26 25", " 2 33 56 55 54 53 52 51 24", " 3 34 57 72 71 70 69 50 23",
        " 4 35 58 73 80 79 68 49 22", " 5 36 59 74 81 78 67 48 21", " 6 37 60 75 76 77 66 47 20",
        " 7 38 61 62 63 64 65 46 19", " 8 39 40 41 42 43 44 45 18", " 9 10 11 12 13 14 15 16 17",
    };
    for (int i = 0; i < rn; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 rn 就继续
        if (fmt_row(m[i]) != want[i]) {
            std::cout << "matrix9 row " << i << " failed" << std::endl;
            return 1;
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
