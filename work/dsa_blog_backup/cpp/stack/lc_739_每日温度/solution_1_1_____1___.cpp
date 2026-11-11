// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233913
// LeetCode 739. 每日温度 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> dailyTemperatures(const std::vector<int> &temps) {
    size_t n = temps.size();         // 把 temps.大小(); 写入 size_t n
    std::vector<int> res(n, 0);      // std::vector 小于 int 超过 结果(元素个数, 0);
    std::vector<size_t> st;          // std::vector 小于 size_t 超过 st;
    for (size_t i = 0; i < n; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        while (!st.empty() &&
               temps[st.back()] <
                   temps[i]) { // 循环，直到不满足「取反 st 是否为空 且 temps[st.back()] 小于 temps[下标 i]」
            res[st.back()] = static_cast<int>(i - st.back());
            st.pop_back(); // 弹出栈顶元素
        }
        st.push_back(i); // st 追加 下标 i);
    }
    return res; // 返回 结果
}
int main() {
    assert((dailyTemperatures({73, 74, 75, 71, 69, 72, 76, 73}) == std::vector<int>{1, 1, 4, 2, 1, 1, 0, 0}));
    assert((dailyTemperatures({30, 40, 50, 60}) == std::vector<int>{1, 1, 1, 0}));
    assert((dailyTemperatures({30, 60, 90}) == std::vector<int>{1, 1, 0}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS