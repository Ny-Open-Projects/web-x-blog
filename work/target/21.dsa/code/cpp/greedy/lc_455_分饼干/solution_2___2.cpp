// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135096603
// LeetCode 455. 分发饼干 — C++ 版（方案2）
#include <algorithm>                                                     // 引入头文件
#include <cassert>                                                       // 引入头文件
#include <iostream>                                                      // 引入头文件
#include <vector>                                                        // 引入头文件
static int findContentChildren(std::vector<int> g, std::vector<int> s) { // 定义函数/方法 findContentChildren
    std::sort(g.begin(), g.end()); // std::sort(g 迭代位置 , g.终点());
    std::sort(s.begin(), s.end()); // std::sort(字符串 迭代位置 , 字符串.终点());
    size_t child = 0, cookie = 0;  // 把 0, cookie 赋值为 0; 写入 size_t child
    while (child < g.size() &&
           cookie < s.size()) { // 循环，直到不满足「子节点 小于 g.大小() 且 cookie 小于 字符串.大小(」
        if (s[cookie] >= g[child])
            ++child; // 若 字符串[cookie] 不低于 g[子节点]) 加一 子节点;
        ++cookie;    // 加一 cookie;
    }
    return static_cast<int>(child); // 返回 static_cast 小于 int 超过 (子节点)
}
int main() {                                             // 程序入口：跑内嵌自测用例
    assert(findContentChildren({1, 2, 3}, {1, 1}) == 1); // 断言校验
    assert(findContentChildren({1, 2}, {1, 2, 3}) == 2); // 断言校验
    std::cout << "PASS" << std::endl;                    // 全部用例通过，输出 PASS
    return 0;                                            // 返回 0
}
