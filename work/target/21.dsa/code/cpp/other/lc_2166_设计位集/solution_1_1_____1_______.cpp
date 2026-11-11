// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145556343
// LeetCode 2166. 设计位集 — C++ 版（方案1）
#include <cassert>               // 引入头文件
#include <iostream>              // 引入头文件
#include <string>                // 引入头文件
#include <vector>                // 引入头文件
struct Bitset {                  // 定义类型
    int n;                       // int 元素个数;
    std::vector<unsigned> words; // std::vector 小于 unsigned 超过 单词列表;
    int ones = 0;                // 把 0 存入 ones
    unsigned reverse = 0;        // 把 0; 写入 unsigned reverse
    explicit Bitset(int size) : n(size), words((size + 31) / 32, 0u) {}
    unsigned get(int idx) const { return ((words[idx >> 5] >> (idx & 31)) & 1u) ^ reverse; }
    void fix(int idx) {
        if (get(idx) == 0) {
            words[idx >> 5] |= 1u << (idx & 31);
            ++ones;
        }
    }
    void unfix(int idx) {
        if (get(idx) == 1) {
            words[idx >> 5] &= ~(1u << (idx & 31));
            --ones;
        }
    }
    void flip() {
        reverse ^= 1;
        ones = n - ones;
    } // 把 1; ones 赋值为 元素个数 减 ones; } 写入 void flip() { reverse ^
    bool all() const { return ones == n; } // 把 赋值为 元素个数; } 写入 bool all() const { return ones
    bool one() const { return ones > 0; } // bool one() const { return ones 超过 0; }
    int count() const { return ones; }    // int 计数() const { return ones; }
    std::string toString() const {        // std::string toString() const {
        std::string s;                    // std::string 字符串;
        for (int i = 0; i < n; ++i)
            s.push_back('0' +
                        static_cast<char>(get(i))); // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        return s;                                   // 返回 字符串
    }
};
int main() {      // 程序入口：跑内嵌自测用例
    Bitset bs(5); // Bitset bs(5);
    bs.fix(0);
    bs.fix(3);                        // bs.fix(0); bs.fix(3);
    assert(bs.toString() == "10010"); // 断言校验
    assert(bs.count() == 2);          // 断言校验
    bs.flip();                        // bs.flip();
    assert(bs.toString() == "01101"); // 断言校验
    assert(bs.count() == 3);          // 断言校验
    bs.unfix(0);                      // bs.unfix(0);
    assert(bs.toString() == "01101"); // 断言校验
    assert(!bs.all() && bs.one());    // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
