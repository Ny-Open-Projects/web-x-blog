// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397916
// LeetCode 2454. 下一个更大元素 IV — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> secondGreater(const std::vector<int> &nums) {
    size_t n = nums.size();          // 把 数组.大小(); 写入 size_t n
    std::vector<int> res(n, -1);     // std::vector 小于 int 超过 结果(元素个数, 减 1);
    std::vector<size_t> s1, s2;      // std::vector 小于 size_t 超过 s1, s2;
    for (size_t i = 0; i < n; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        while (!s2.empty() && nums[s2.back()] < nums[i])
            res[s2.back()] = nums[i], s2.pop_back();
        while (!s1.empty() && nums[s1.back()] < nums[i])
            s2.push_back(s1.back()), s1.pop_back();
        s1.push_back(i); // s1 追加 下标 i);
    }
    return res; // 返回 结果
}
int main() {
    assert((secondGreater({2, 4, 0, 9, 6}) == std::vector<int>{9, 6, 6, -1, -1}));
    assert((secondGreater({5, 4, 3, 2, 1}) == std::vector<int>{-1, -1, -1, -1, -1}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS