// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130668538
// LeetCode 58. 最后一个单词的长度 — C++ 版（方案1）
#include <cassert>                           // 引入头文件
#include <iostream>                          // 引入头文件
#include <string>                            // 引入头文件
static int lengthOfLastWord(std::string s) { // 定义函数/方法 lengthOfLastWord
    int end = static_cast<int>(s.size()) - 1; // 把 static_cast 小于 int 超过 (字符串.大小()) 减 1 存入 终点
    while (end >= 0 && s[end] == ' ')
        --end; // 循环，直到不满足「终点 不低于 0 且 字符串[终点] 等于 ' ') 减一 终点;」
    if (end < 0)
        return 0;    // 若 终点 小于 0，直接返回 0
    int start = end; // 把 终点 存入 起点
    while (start >= 0 && s[start] != ' ')
        --start; // 循环，直到不满足「起点 不低于 0 且 字符串[起点] 不等于 ' ') 减一 起点;」
    return end - start; // 返回 终点 减 起点
}
int main() {                                               // 程序入口：跑内嵌自测用例
    assert(lengthOfLastWord("Hello World") == 5);          // 断言校验
    assert(lengthOfLastWord(" ") == 0);                    // 断言校验
    assert(lengthOfLastWord("a") == 1);                    // 断言校验
    assert(lengthOfLastWord(" fly me to the moon ") == 4); // 断言校验
    std::cout << "PASS" << std::endl;                      // 全部用例通过，输出 PASS
    return 0;                                              // 返回 0
}
