// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案9：规则串状态机，8 方向字母）
#include <iostream> // 引入头文件
#include <string>   // 引入头文件
#include <vector>   // 引入头文件

struct Location {         // 定义类型
    int row = 0, col = 0; // 把 0, col 赋值为 0 存入 row
};

class Filler { // 定义类型
  public:      // public:
    Filler(int rn, int cn) : rowNum_(rn), colNum_(cn), rMax_(rn - 1), cMax_(cn - 1) {}
    void setRule(const std::string &rule) {
        rule_ = rule;
    }                            // 把 rule; } 写入 void setRule(const std::string &rule) { rule_
    std::pair<int, int> next() { // std::pair 小于 int, int 超过 下一个() {
        std::pair<int, int> res{pos_.row, pos_.col}; // std::pair 小于 int, int 超过 结果{pos_.row, pos_.col};
        char ch = rule_[idx_ % rule_.size()]; // 把 rule_[idx_ 对…取模 rule_.大小()]; 写入 char ch
        if (ch == 'E') {                      // 若 字符 等于 'E'
            ++pos_.row;                       // 加一 pos_.row;
            if (pos_.row == rMax_) {
                ++idx_;
                ++cMin_;
            }                   // 若 pos_.row 等于 rMax_) { 加一 idx_; 加一 cMin_; }
        } else if (ch == 'S') { // 否则，若 字符 等于 'S'
            ++pos_.col;         // 加一 pos_.col;
            if (pos_.col == cMax_) {
                ++idx_;
                --rMax_;
            }                   // 若 pos_.col 等于 cMax_) { 加一 idx_; 减一 rMax_; }
        } else if (ch == 'V') { // 否则，若 字符 等于 'V'
            --pos_.row;         // 减一 pos_.row;
            if (pos_.row == rMin_) {
                ++idx_;
                --cMax_;
            }                   // 若 pos_.row 等于 rMin_) { 加一 idx_; 减一 cMax_; }
        } else if (ch == 'M') { // 否则，若 字符 等于 'M'
            --pos_.col;         // 减一 pos_.col;
            if (pos_.col == cMin_) {
                ++idx_;
                ++rMin_;
            }                   // 若 pos_.col 等于 cMin_) { 加一 idx_; 加一 rMin_; }
        } else if (ch == 'e') { // 否则，若 字符 等于 'e'
            ++pos_.row;         // 加一 pos_.row;
            if (pos_.row == rMax_) {
                ++idx_;
                --cMax_;
            }                   // 若 pos_.row 等于 rMax_) { 加一 idx_; 减一 cMax_; }
        } else if (ch == 's') { // 否则，若 字符 等于 '字符串'
            ++pos_.col;         // 加一 pos_.col;
            if (pos_.col == cMax_) {
                ++idx_;
                ++rMin_;
            }                   // 若 pos_.col 等于 cMax_) { 加一 idx_; 加一 rMin_; }
        } else if (ch == 'v') { // 否则，若 字符 等于 '值'
            --pos_.row;         // 减一 pos_.row;
            if (pos_.row == rMin_) {
                ++idx_;
                ++cMin_;
            }                   // 若 pos_.row 等于 rMin_) { 加一 idx_; 加一 cMin_; }
        } else if (ch == 'm') { // 否则，若 字符 等于 '映射表'
            --pos_.col;         // 减一 pos_.col;
            if (pos_.col == cMin_) {
                ++idx_;
                --rMax_;
            } // 若 pos_.col 等于 cMin_) { 加一 idx_; 减一 rMax_; }
        }
        return res; // 返回 结果
    }

  private:                                  // private:
    int rowNum_, colNum_;                   // int rowNum_, colNum_;
    Location pos_;                          // Location pos_;
    size_t idx_ = 0;                        // 把 0; 写入 size_t idx_
    int rMin_ = 0, cMin_ = 0, rMax_, cMax_; // 把 0, cMin_ 赋值为 0, rMax_, cMax_ 存入 rMin_
    std::string rule_ = "ESVM";             // 把 「ESVM」; 写入 std::string rule_
};

static std::vector<std::vector<int>> test_filler(const std::string &rule, int rn, int cn) {
    Filler obj(rn, cn);                // Filler obj(rn, cn);
    obj.setRule(rule);                 // obj.setRule(rule);
    std::vector<std::vector<int>> seq; // std::vector 小于 std::vector 小于 int 超过 超过 seq;
    for (int i = 0; i < rn * cn; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 rn 乘 cn 就继续
        auto [r, c] = obj.next();       // 把 obj.下一个(); 写入 auto [r, c]
        seq.push_back({r, c});          // seq 追加 {右指针, 字符});
    }
    return seq; // 返回 seq
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::vector<int>> want_esvm = {
        // 把 { 写入 std::vector<std::vector<int>> want_esvm
        {0, 0}, {1, 0}, {2, 0}, {3, 0}, {3, 1}, {3, 2}, {3, 3}, {2, 3},
        {1, 3}, {0, 3}, {0, 2}, {0, 1}, {1, 1}, {2, 1}, {2, 2}, {1, 2},
    };
    if (test_filler("ESVM", 4, 4) != want_esvm) {
        std::cout << "ESVM failed" << std::endl;
        return 1;
    }
    std::vector<std::vector<int>> want_semv = {
        // 把 { 写入 std::vector<std::vector<int>> want_semv
        {0, 0}, {0, 1}, {0, 2}, {0, 3}, {1, 3}, {2, 3}, {3, 3}, {3, 2},
        {3, 1}, {3, 0}, {2, 0}, {1, 0}, {1, 1}, {1, 2}, {2, 2}, {2, 1},
    };
    if (test_filler("semv", 4, 4) != want_semv) {
        std::cout << "semv failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
