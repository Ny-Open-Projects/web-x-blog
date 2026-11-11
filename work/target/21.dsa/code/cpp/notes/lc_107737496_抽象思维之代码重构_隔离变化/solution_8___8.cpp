// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案8：Filler 状态机 + hasNext 部分填充）
#include <iostream> // 引入头文件
#include <string>   // 引入头文件
#include <vector>   // 引入头文件

class Filler { // 定义类型
  public:      // public:
    Filler(int rn, int cn) : rowNum_(rn), colNum_(cn), rule_("ESVM") {
        reset(); // reset();
    }
    void setRule(const std::string &r) {
        rule_ = r;
    }                      // 把 右指针; } 写入 void setRule(const std::string &r) { rule_
    bool hasNext() const { // bool hasNext() const {
        return rMin_ <= posRow_ && posRow_ <= rMax_ && cMin_ <= posCol_ &&
               posCol_ <= cMax_; // 把 posCol_ 且 posCol_ 不超过 cMax_; 写入 cMin_ <
    }
    std::pair<int, int> next() {      // std::pair 小于 int, int 超过 下一个() {
        int r = posRow_, c = posCol_; // 把 posRow_, 字符 赋值为 posCol_ 存入 右指针
        advance();                    // advance();
        return {r, c};                // 返回 {右指针, 字符}
    }

  private:                     // private:
    void reset() {             // 定义函数/方法 reset
        posRow_ = posCol_ = 0; // 把 posCol_ 赋值为 0; 写入 posRow_
        idx_ = 0;              // 把 0; 写入 idx_
        rMin_ = cMin_ = 0;     // 把 cMin_ 赋值为 0; 写入 rMin_
        rMax_ = rowNum_ - 1;   // 把 rowNum_ 减 1; 写入 rMax_
        cMax_ = colNum_ - 1;   // 把 colNum_ 减 1; 写入 cMax_
    }
    void advance() {                // 定义函数/方法 advance
        char cmd = rule_[idx_ % 4]; // 把 rule_[idx_ 对…取模 4]; 写入 char cmd
        if (cmd == 'E') {           // 若 cmd 等于 'E'
            ++posRow_;              // 加一 posRow_;
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
    }

    int rowNum_, colNum_;           // int rowNum_, colNum_;
    std::string rule_;              // std::string rule_;
    int posRow_, posCol_, idx_;     // int posRow_, posCol_, idx_;
    int rMin_, cMin_, rMax_, cMax_; // int rMin_, cMin_, rMax_, cMax_;
};

static std::vector<std::vector<int>> fillMatrix(int rn, int cn, const std::string &rule) {
    std::vector<std::vector<int>> mat(rn, std::vector<int>(cn, 0));
    Filler f(rn, cn);           // Filler f(rn, cn);
    f.setRule(rule);            // f.setRule(rule);
    int i = 1;                  // 把 1 存入 下标 i
    while (f.hasNext()) {       // 循环，直到不满足「f.hasNext(」
        auto [r, c] = f.next(); // 把 f.下一个(); 写入 auto [r, c]
        mat[r][c] = i;          // 把 下标 i; 写入 mat[r][c]
        ++i;                    // 加一 下标 i;
    }
    return mat; // 返回 mat
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::vector<int>> want1 = {
        // 把 { 写入 std::vector<std::vector<int>> want1
        {1, 0, 0, 0, 0, 0}, {2, 0, 0, 0, 0, 0}, {3, 0, 0, 0, 0, 0},
        {4, 0, 0, 0, 0, 0}, {5, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0},
    };
    if (fillMatrix(6, 6, "ESVM") != want1) {
        std::cout << "case1 failed" << std::endl;
        return 1;
    }
    std::vector<std::vector<int>> want2 = {{1, 0, 0}, {2, 0, 0}, {0, 0, 0}};
    if (fillMatrix(3, 3, "ESVM") != want2) {
        std::cout << "case2 failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
