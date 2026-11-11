// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133772625
// LeetCode 131. 分割回文串 — C++ 版（方案2）
#include <cassert>                        // 引入头文件
#include <iostream>                       // 引入头文件
#include <string>                         // 引入头文件
#include <vector>                         // 引入头文件
static bool isPal(const std::string &s) { // 定义判定函数 isPal
    size_t i = 0, j = s.size() - 1; // 把 0, 下标 j 赋值为 字符串.大小() 减 1; 写入 size_t i
    while (i < j) {                 // 循环，直到不满足「下标 i 小于 下标 j」
        if (s[i] != s[j])
            return false; // 若 字符串[下标 i] 不等于 字符串[下标 j]，直接返回 false
        ++i;
        --j; // 加一 下标 i; 减一 下标 j;
    }
    return true; // 返回 true
}
static std::vector<std::vector<std::string>> partition(const std::string &s) {
    std::vector<std::vector<std::string>>
        res;                       // std::vector 小于 std::vector 小于 std::string 超过 超过 结果;
    std::vector<std::string> path; // std::vector 小于 std::string 超过 当前路径;
    std::function<void(size_t)> dfs =
        [&](size_t start) { // 把 [ 按位与 ](size_t 起点) { 写入 std::function<void(size_t)> dfs
            if (start == s.size()) {
                res.push_back(path);
                return;
            } // 若 起点 等于 字符串.大小()) { 结果 追加 当前路径); return; }
            for (size_t e = start + 1; e <= s.size();
                 ++e) { // 让 e 从 起点 加 1 开始计数，e 不超过 字符串.大小() 就继续
                auto sub = s.substr(start, e - start); // 把 字符串 截取 起点, e 减 起点) 存入 sub
                if (isPal(sub)) {                      // 若 isPal(sub
                    path.push_back(sub);               // 当前路径 追加 sub);
                    dfs(e);                            // dfs(e);
                    path.pop_back();                   // 弹出栈顶元素
                }
            }
        };
    dfs(0);     // dfs(0);
    return res; // 返回 结果
}
int main() { // 程序入口：跑内嵌自测用例
    assert((partition("aab") ==
            std::vector<std::vector<std::string>>{{"a", "a", "b"}, {"aa", "b"}})); // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
