// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145045460
// LeetCode 503. 下一个更大元素 II — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> nextGreaterElements(const std::vector<int> &nums) {
    size_t n = nums.size();      // 把 数组.大小(); 写入 size_t n
    std::vector<int> res(n, -1); // std::vector 小于 int 超过 结果(元素个数, 减 1);
    std::vector<size_t> st;      // std::vector 小于 size_t 超过 st;
    for (size_t i = 0; i < 2 * n; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 2 乘 元素个数 就继续
        size_t ii = i % n;               // 把 下标 i 对…取模 元素个数; 写入 size_t ii
        while (!st.empty() &&
               nums[st.back()] <
                   nums[ii]) { // 循环，直到不满足「取反 st 是否为空 且 数组[st.back()] 小于 数组[ii]」
            res[st.back()] = nums[ii]; // 把 数组[ii]; 写入 res[st.back()]
            st.pop_back();             // 弹出栈顶元素
        }
        if (i < n)
            st.push_back(ii); // 若 下标 i 小于 元素个数) st 追加 ii);
    }
    return res; // 返回 结果
}
int main() {
    assert((nextGreaterElements({1, 2, 1}) == std::vector<int>{2, -1, 2}));
    assert((nextGreaterElements({3, 2, 1}) == std::vector<int>{-1, 3, 3}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS