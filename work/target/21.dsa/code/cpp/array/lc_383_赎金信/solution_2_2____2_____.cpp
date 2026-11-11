// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134312127
// LeetCode 383. 赎金信 — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <string>   // 引入头文件
static bool canConstruct(const std::string &ransom,
                         const std::string &magazine) { // 定义函数/方法 canConstruct
    int cnt[26] = {0};                                  // 把 {0}; 写入 int cnt[26]
    for (char c : magazine)
        ++cnt[c - 'a'];     // for (char 字符 : magazine) 加一 计数[字符 减 '数组'];
    for (char c : ransom) { // for (char 字符 : ransom) {
        if (--cnt[c - 'a'] < 0)
            return false; // 若 减一 计数[字符 减 '数组'] 小于 0，直接返回 false
    }
    return true; // 返回 true
}
int main() {
    assert(!canConstruct("a", "b"));
    assert(!canConstruct("aa", "ab"));
    assert(canConstruct("aa", "aab"));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS