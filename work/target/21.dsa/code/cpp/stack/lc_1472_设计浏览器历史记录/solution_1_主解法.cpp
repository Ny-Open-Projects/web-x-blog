// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145338856
// LeetCode 1472. 设计浏览器历史记录 — C++ 版（方案1）
#include <cassert>                    // 引入头文件
#include <iostream>                   // 引入头文件
#include <string>                     // 引入头文件
#include <vector>                     // 引入头文件
struct BrowserHistory {               // 定义类型
    std::vector<std::string> history; // std::vector 小于 std::string 超过 history;
    size_t cur;                       // size_t 当前值;
    explicit BrowserHistory(const std::string &homepage) : history{homepage}, cur(0) {}
    void visit(const std::string &url) { // 定义函数/方法 visit
        history.resize(cur + 1);         // history.resize(当前值 加 1);
        history.push_back(url);          // history 追加 url);
        cur = history.size() - 1;        // 把 history.大小() 减 1; 写入 当前值
    }
    std::string back(int steps) { // std::string back(int steps) {
        cur = cur >= static_cast<size_t>(steps) ? cur - steps : 0;
        return history[cur]; // 返回 history[当前值]
    }
    std::string forward(int steps) { // std::string forward(int steps) {
        cur = std::min(cur + static_cast<size_t>(steps), history.size() - 1);
        return history[cur]; // 返回 history[当前值]
    }
};
int main() {                                // 程序入口：跑内嵌自测用例
    BrowserHistory b("leetcode.com");       // BrowserHistory b(「leetcode.com」);
    b.visit("google.com");                  // b.visit(「google.com」);
    b.visit("facebook.com");                // b.visit(「facebook.com」);
    b.visit("youtube.com");                 // b.visit(「youtube.com」);
    assert(b.back(1) == "facebook.com");    // 断言校验
    assert(b.back(1) == "google.com");      // 断言校验
    assert(b.forward(1) == "facebook.com"); // 断言校验
    b.visit("linkedin.com");                // b.visit(「linkedin.com」);
    assert(b.forward(2) == "linkedin.com"); // 断言校验
    assert(b.back(2) == "google.com");      // 断言校验
    assert(b.back(7) == "leetcode.com");    // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS