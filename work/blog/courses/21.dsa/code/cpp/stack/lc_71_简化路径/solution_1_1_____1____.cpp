// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134368624
// LeetCode 71. 简化路径 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <sstream>  // 引入头文件
#include <string>   // 引入头文件
#include <vector>   // 引入头文件
static std::string simplifyPath(const std::string &path) {
    std::vector<std::string> st;           // std::vector 小于 std::string 超过 st;
    std::istringstream iss(path);          // std::istringstream iss(当前路径);
    std::string part;                      // std::string part;
    while (std::getline(iss, part, '/')) { // 循环，直到不满足「std::getline(iss, part, ' 除以 '」
        if (part.empty() || part == ".")
            continue; // 若 part 是否为空 或 part 等于 「.」) continue;
        if (part == "..") {
            if (!st.empty())
                st.pop_back();
        } // 若 part 等于 「..」) { if (取反 st 是否为空) st 弹出 ); }
        else
            st.push_back(part); // 否则
    }
    std::string out = "/";                   // 把 「 除以 」; 写入 std::string out
    for (size_t i = 0; i < st.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 st.大小() 就继续
        if (i)
            out += "/"; // 若 下标 i) out 累加 「 除以 」;
        out += st[i];   // out累加 st[下标 i]
    }
    return out; // 返回 out
}
int main() {
    assert(simplifyPath("/home/") == "/home");
    assert(simplifyPath("/../") == "/");
    assert(simplifyPath("/home//foo/") == "/home/foo");
    assert(simplifyPath("/a/./b/../../c/") == "/c");
    std::cout << "PASS" << std::endl;
} // 断言校验