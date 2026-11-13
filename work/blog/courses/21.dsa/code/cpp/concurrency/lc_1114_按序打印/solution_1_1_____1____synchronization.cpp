// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
// LeetCode 1114. 按序打印 — C++ 版（方案1）
#include <cassert>                         // 引入头文件
#include <condition_variable>              // 引入头文件
#include <iostream>                        // 引入头文件
#include <mutex>                           // 引入头文件
#include <string>                          // 引入头文件
struct Foo {                               // 定义类型
    std::mutex m;                          // std::mutex 映射表;
    std::condition_variable cv;            // std::condition_variable cv;
    int step = 1;                          // 把 1 存入 步数
    void first(std::string &out) {         // 定义函数/方法 first
        out += "first";                    // out累加 「first」
        std::lock_guard<std::mutex> lk(m); // std::lock_guard 小于 std::mutex 超过 lk(映射表);
        step = 2;                          // 把 2; 写入 步数
        cv.notify_all();                   // cv.notify_all();
    }
    void second(std::string &out) {                // 定义函数/方法 second
        std::unique_lock<std::mutex> lk(m);        // std::unique_lock 小于 std::mutex 超过 lk(映射表);
        cv.wait(lk, [this] { return step >= 2; }); // 把 2; }); 写入 cv.wait(lk, [this] { return step >
        out += "second";                           // out累加 「second」
        step = 3;                                  // 把 3; 写入 步数
        cv.notify_all();                           // cv.notify_all();
    }
    void third(std::string &out) {                 // 定义函数/方法 third
        std::unique_lock<std::mutex> lk(m);        // std::unique_lock 小于 std::mutex 超过 lk(映射表);
        cv.wait(lk, [this] { return step >= 3; }); // 把 3; }); 写入 cv.wait(lk, [this] { return step >
        out += "third";                            // out累加 「third」
    }
};
int main() {                           // 程序入口：跑内嵌自测用例
    Foo foo;                           // Foo foo;
    std::string out;                   // std::string out;
    foo.first(out);                    // foo.first(out);
    foo.second(out);                   // foo.second(out);
    foo.third(out);                    // foo.third(out);
    assert(out == "firstsecondthird"); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS