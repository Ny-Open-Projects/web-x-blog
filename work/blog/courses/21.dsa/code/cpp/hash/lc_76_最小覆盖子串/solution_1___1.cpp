// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135256754
// LeetCode 76. 最小覆盖子串 — C++ 版（方案1）
#include <cassert>       // 引入头文件
#include <iostream>      // 引入头文件
#include <string>        // 引入头文件
#include <unordered_map> // 引入头文件
static std::string minWindow(const std::string &s, const std::string &t) {
    if (s.empty() || t.empty())
        return ""; // 若 字符串 是否为空 或 另一字符串 是否为空，直接返回 「」
    std::unordered_map<char, int> target; // std::unordered_map 小于 char, int 超过 目标值;
    for (char c : t)
        ++target[c]; // for (char 字符 : 另一字符串) 加一 目标值[字符];
    int required =
        static_cast<int>(target.size()); // 把 static_cast 小于 int 超过 (目标值.大小()) 存入 required
    size_t left = 0;                     // 把 0; 写入 size_t left
    int formed = 0;                      // 把 0 存入 formed
    std::unordered_map<char, int> window;    // std::unordered_map 小于 char, int 超过 window;
    size_t min_len = SIZE_MAX, min_left = 0; // 把 SIZE_MAX, min_left 赋值为 0; 写入 size_t min_len
    for (size_t right = 0; right < s.size();
         ++right) {        // 让 右边界 从 0 开始计数，右边界 小于 字符串.大小() 就继续
        char c = s[right]; // 把 字符串[右边界]; 写入 char c
        ++window[c];       // 加一 window[字符];
        if (target.count(c) && window[c] == target[c])
            ++formed; // 若 目标值.计数(字符) 且 window[字符] 等于 目标值[字符]) 加一 formed;
        while (formed == required) { // 循环，直到不满足「formed 等于 required」
            if (right - left + 1 < min_len) {
                min_len = right - left + 1;
                min_left = left;
            }
            char lc = s[left]; // 把 字符串[左边界]; 写入 char lc
            --window[lc];      // 减一 window[lc];
            if (target.count(lc) && window[lc] < target[lc])
                --formed; // 若 目标值.计数(lc) 且 window[lc] 小于 目标值[lc]) 减一 formed;
            ++left;       // 加一 左边界;
        }
    }
    return min_len == SIZE_MAX
               ? ""
               : s.substr(min_left,
                          min_len); // 返回 min_len 等于 SIZE_MAX ? 「」 : 字符串 截取 min_left, min_len)
}
int main() {                                             // 程序入口：跑内嵌自测用例
    assert(minWindow("ADOBECODEBANC", "ABC") == "BANC"); // 断言校验
    assert(minWindow("a", "a") == "a");                  // 断言校验
    assert(minWindow("a", "aa") == "");                  // 断言校验
    std::cout << "PASS" << std::endl;                    // 全部用例通过，输出 PASS
    return 0;                                            // 返回 0
}
