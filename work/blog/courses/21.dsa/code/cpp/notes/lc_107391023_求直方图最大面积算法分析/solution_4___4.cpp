// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
// 求直方图最大面积算法分析 — C++ 版（方案4）
#include <cassert>                                       // 引入头文件
#include <iostream>                                      // 引入头文件
#include <vector>                                        // 引入头文件
static int getResult(int n, const std::vector<int> &h) { // 定义函数/方法 getResult
    std::vector<size_t> st;                              // std::vector 小于 size_t 超过 st;
    int best = 0;                                        // 把 0 存入 当前最优
    for (size_t i = 0; i <= h.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 不超过 h.大小() 就继续
        int cur = i < h.size() ? h[i] : 0; // 把 下标 i 小于 h.大小() ? h[下标 i] : 0 存入 当前值
        while (!st.empty() &&
               h[st.back()] >= cur) { // 循环，直到不满足「取反 st 是否为空 且 h[st.back()] 不低于 当前值」
            int t = h[st.back()]; // 把 h[st.back()] 存入 另一字符串
            st.pop_back();        // 弹出栈顶元素
            long long left = st.empty() ? -1 : static_cast<long long>(st.back());
            long long width = static_cast<long long>(i) - left -
                              1; // 把 static_cast 小于 long long 超过 (下标 i) 减 左边界 减 1 存入 width
            best = std::max(best, static_cast<int>(t * width));
        }
        st.push_back(i); // st 追加 下标 i);
    }
    return best; // 返回 当前最优
}
int main() {                                              // 程序入口：跑内嵌自测用例
    assert(getResult(5, {0, 2, 3, 3, 3, 2, 0}) == 10);    // 断言校验
    assert(getResult(6, {0, 2, 1, 5, 6, 2, 3, 0}) == 10); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS