// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145295630
// LeetCode 1047. 删除字符串中的所有相邻重复项 — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <string>   // 引入头文件
static std::string removeDuplicates(const std::string &s) {
    std::string st;    // std::string st;
    for (char c : s) { // for (char 字符 : 字符串) {
        if (!st.empty() && st.back() == c)
            st.pop_back(); // 若 取反 st 是否为空 且 st.back() 等于 字符) st 弹出 );
        else
            st.push_back(c); // 否则
    }
    return st; // 返回 st
}
int main() {
    assert(removeDuplicates("abbaca") == "ca");
    assert(removeDuplicates("azxxzy") == "ay");
    assert(removeDuplicates("") == "");
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS