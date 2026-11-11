// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145012016
// LeetCode 496. 下一个更大元素 I — C++ 版（方案1）
#include <cassert>       // 引入头文件
#include <iostream>      // 引入头文件
#include <stack>         // 引入头文件
#include <unordered_map> // 引入头文件
#include <vector>        // 引入头文件
static std::vector<int> nextGreaterElement(const std::vector<int> &nums1, const std::vector<int> &nums2) {
    std::unordered_map<int, int> next; // std::unordered_map 小于 int, int 超过 下一个;
    std::stack<int> st;                // std::栈 小于 int 超过 st;
    for (int v : nums2) {              // for (int 值 : 数组2) {
        while (!st.empty() && st.top() < v) { // 循环，直到不满足「取反 st 是否为空 且 st.top() 小于 值」
            next[st.top()] = v; // 把 值; 写入 next[st.top()]
            st.pop();           // 弹出栈顶元素
        }
        st.push(v); // 把 值 压入栈/数组尾部
    }
    std::vector<int> out;       // std::vector 小于 int 超过 out;
    for (int v : nums1) {       // for (int 值 : 数组1) {
        auto it = next.find(v); // 把 下一个 查找 值) 存入 it
        out.push_back(it != next.end()
                          ? it->second
                          : -1); // 把 下一个.终点() ? it 减 超过 second : 减 1); 写入 out.push_back(it !
    }
    return out; // 返回 out
}
int main() {
    assert((nextGreaterElement({4, 1, 2}, {1, 3, 4, 2}) == std::vector<int>{-1, 3, -1}));
    assert((nextGreaterElement({2, 4}, {1, 2, 3, 4}) == std::vector<int>{3, -1}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS