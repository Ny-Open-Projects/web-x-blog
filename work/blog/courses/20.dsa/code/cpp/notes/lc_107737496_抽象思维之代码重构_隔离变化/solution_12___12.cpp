// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案12：Location/Rule/Filler 组合）
#include <iostream> // 引入头文件
#include <string>   // 引入头文件
#include <vector>   // 引入头文件

class Rule { // 定义类型
  public:    // public:
    explicit Rule(const std::string &r) : data_(r), idx_(0) {}
    char current() const { return data_[idx_]; } // char current() const { return data_[idx_]; }
    void advance() {
        idx_ = (idx_ + 1) % data_.size();
    } // 把 (idx_ 加 1) 对…取模 data_.大小(); } 写入 void advance() { idx_

  private:             // private:
    std::string data_; // std::string data_;
    size_t idx_;       // size_t idx_;
};

class Filler {                                      // 定义类型
  public:                                           // public:
    Filler(int rn, int cn, const std::string &rule) // Filler(int rn, int cn, const std::string 按位与 rule)
        : rMax_(rn - 1), cMax_(cn - 1), cmd_(rule) {} // : rMax_(rn 减 1), cMax_(cn 减 1), cmd_(rule) {}
    std::pair<int, int> next() {                      // std::pair 小于 int, int 超过 下一个() {
        std::pair<int, int> res{posRow_, posCol_}; // std::pair 小于 int, int 超过 结果{posRow_, posCol_};
        char ch = cmd_.current();                  // 把 cmd_.current(); 写入 char ch
        if (ch == 'E') {                           // 若 字符 等于 'E'
            ++posRow_;                             // 加一 posRow_;
            if (posRow_ == rMax_) {
                cmd_.advance();
                ++cMin_;
            }                   // 若 posRow_ 等于 rMax_) { cmd_.advance(); 加一 cMin_; }
        } else if (ch == 'S') { // 否则，若 字符 等于 'S'
            ++posCol_;          // 加一 posCol_;
            if (posCol_ == cMax_) {
                cmd_.advance();
                --rMax_;
            }                   // 若 posCol_ 等于 cMax_) { cmd_.advance(); 减一 rMax_; }
        } else if (ch == 'V') { // 否则，若 字符 等于 'V'
            --posRow_;          // 减一 posRow_;
            if (posRow_ == rMin_) {
                cmd_.advance();
                --cMax_;
            }                   // 若 posRow_ 等于 rMin_) { cmd_.advance(); 减一 cMax_; }
        } else if (ch == 'M') { // 否则，若 字符 等于 'M'
            --posCol_;          // 减一 posCol_;
            if (posCol_ == cMin_) {
                cmd_.advance();
                ++rMin_;
            } // 若 posCol_ 等于 cMin_) { cmd_.advance(); 加一 rMin_; }
        }
        return res; // 返回 结果
    }

  private:                                  // private:
    int posRow_ = 0, posCol_ = 0;           // 把 0, posCol_ 赋值为 0 存入 posRow_
    int rMin_ = 0, cMin_ = 0, rMax_, cMax_; // 把 0, cMin_ 赋值为 0, rMax_, cMax_ 存入 rMin_
    Rule cmd_;                              // Rule cmd_;
};

int main() {                  // 程序入口：跑内嵌自测用例
    Filler obj(4, 4, "ESVM"); // Filler obj(4, 4, 「ESVM」);
    std::vector<std::pair<int, int>> want = {
        // 把 { 写入 std::vector<std::pair<int, int>> want
        {0, 0}, {1, 0}, {2, 0}, {3, 0}, {3, 1}, {3, 2}, {3, 3}, {2, 3},
        {1, 3}, {0, 3}, {0, 2}, {0, 1}, {1, 1}, {2, 1}, {2, 2}, {1, 2},
    };
    for (int i = 0; i < 16; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 16 就继续
        auto rc = obj.next();      // 把 obj.下一个() 存入 rc
        if (rc != want[i]) {
            std::cout << "filler4 at " << i << " failed" << std::endl;
            return 1;
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
