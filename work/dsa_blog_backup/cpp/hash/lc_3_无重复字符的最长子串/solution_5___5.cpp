// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135004189
// LeetCode 3. 无重复字符的最长子串 — C++ 版（方案5）
#include <cassert>                                          // 引入头文件
#include <iostream>                                         // 引入头文件
#include <string>                                           // 引入头文件
#include <unordered_set>                                    // 引入头文件
static int lengthOfLongestSubstring(const std::string &s) { // 定义函数/方法 lengthOfLongestSubstring
    std::unordered_set<char> set;                           // std::unordered_set 小于 char 超过 set;
    size_t left = 0;                                        // 把 0; 写入 size_t left
    int max_len = 0;                                        // 把 0 存入 max_len
    for (size_t right = 0; right < s.size();
         ++right) { // 让 右边界 从 0 开始计数，右边界 小于 字符串.大小() 就继续
        while (set.count(s[right])) { // 循环，直到不满足「set.计数(字符串[右边界]」
            set.erase(s[left]);       // set 删除 字符串[左边界]);
            ++left;                   // 加一 左边界;
        }
        set.insert(s[right]); // set 插入 字符串[右边界]);
        max_len = std::max(max_len, static_cast<int>(right - left + 1));
    }
    return max_len; // 返回 max_len
}
int main() {                                           // 程序入口：跑内嵌自测用例
    assert(lengthOfLongestSubstring("abcabcbb") == 3); // 断言校验
    assert(lengthOfLongestSubstring("bbbbb") == 1);    // 断言校验
    assert(lengthOfLongestSubstring("pwwkew") == 3);   // 断言校验
    assert(lengthOfLongestSubstring("") == 0);         // 断言校验
    std::cout << "PASS" << std::endl;                  // 全部用例通过，输出 PASS
    return 0;                                          // 返回 0
}
