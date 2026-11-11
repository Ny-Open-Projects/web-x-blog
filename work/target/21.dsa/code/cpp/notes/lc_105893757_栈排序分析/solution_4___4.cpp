// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
// 栈排序分析 — C++ 版（方案4）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> stackSort(const std::vector<int> &input) {
    std::vector<int> st; // std::vector 小于 int 超过 st;
    for (int v : input)
        st.push_back(v);  // for (int 值 : input) st 追加 值);
    std::vector<int> out; // std::vector 小于 int 超过 out;
    while (!st.empty()) {
        out.push_back(st.back());
        st.pop_back();
    } // 循环，直到不满足「取反 st 是否为空) { out 追加 st.back()); st 弹出 ); }」
    return out; // 返回 out
}
int main() { // 程序入口：跑内嵌自测用例
    assert((stackSort({3, 1, 5, 2, 4}) == std::vector<int>{4, 2, 5, 1, 3})); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS