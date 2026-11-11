// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136838836
// LeetCode 791. 自定义字符串排序 — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <string>   // 引入头文件
static std::string customSortString(const std::string &order, const std::string &s) {
    int count[26] = {0}; // 把 {0}; 写入 int count[26]
    for (char c : s)
        ++count[c - 'a'];  // for (char 字符 : 字符串) 加一 计数[字符 减 '数组'];
    std::string out;       // std::string out;
    for (char c : order) { // for (char 字符 : order) {
        out.append(static_cast<size_t>(count[c - 'a']),
                   c); // 把 static_cast 小于 size_t 超过 (计数[字符 减 '数组'] 追加到列表尾部
        count[c - 'a'] = 0; // 把 0; 写入 count[c - 'a']
    }
    for (int i = 0; i < 26; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 26 就继续
        out.append(
            static_cast<size_t>(count[i]),
            static_cast<char>('a' + i)); // 把 static_cast 小于 size_t 超过 (计数[下标 i] 追加到列表尾部
    }
    return out; // 返回 out
}
int main() {                                             // 程序入口：跑内嵌自测用例
    assert(customSortString("cba", "abcd") == "cbad");   // 断言校验
    assert(customSortString("bcafg", "abcd") == "bcad"); // 断言校验
    std::cout << "PASS" << std::endl;                    // 全部用例通过，输出 PASS
    return 0;                                            // 返回 0
}
