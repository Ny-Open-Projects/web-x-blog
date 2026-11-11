// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案11：Rule 循环游标）
#include <iostream> // 引入头文件
#include <string>   // 引入头文件
#include <vector>   // 引入头文件

class Rule { // 定义类型
  public:    // public:
    explicit Rule(const std::string &r) : data_(r.begin(), r.end()), idx_(0), length_(r.size()) {}
    char next() {                    // 定义函数/方法 next
        char ch = data_[idx_];       // 把 data_[idx_]; 写入 char ch
        idx_ = (idx_ + 1) % length_; // 把 (idx_ 加 1) 对…取模 length_; 写入 idx_
        return ch;                   // 返回 字符
    }
    char peek() const {     // char peek() const {
        return data_[idx_]; // 返回 data_[idx_]
    }

  private:                   // private:
    std::vector<char> data_; // std::vector 小于 char 超过 data_;
    size_t idx_;             // size_t idx_;
    size_t length_;          // size_t length_;
};

int main() {        // 程序入口：跑内嵌自测用例
    Rule r("ESVM"); // Rule 右指针(「ESVM」);
    std::string s1; // std::string s1;
    for (int i = 0; i < 10; ++i)
        s1 += r.next(); // 让 下标 i 从 0 开始计数，下标 i 小于 10 就继续
    Rule r2("semv");    // Rule r2(「semv」);
    std::string s2;     // std::string s2;
    for (int i = 0; i < 6; ++i)
        s2 += r2.next(); // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
    if (s1 != "ESVMESVMES") {
        std::cout << "rule1 failed" << std::endl;
        return 1;
    }
    if (s2 != "semvse") {
        std::cout << "rule2 failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
