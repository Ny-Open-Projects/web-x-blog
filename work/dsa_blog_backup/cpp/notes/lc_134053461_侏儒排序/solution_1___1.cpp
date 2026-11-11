// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134053461
// 数据结构与算法之排序: 侏儒排序 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> gnomeSort(std::vector<int> v) {
    size_t i = 0;          // 把 0; 写入 size_t i
    while (i < v.size()) { // 循环，直到不满足「下标 i 小于 值.大小(」
        if (i == 0 || v[i - 1] <= v[i])
            ++i; // 若 下标 i 等于 0 或 值[下标 i 减 1] 不超过 值[下标 i]) 加一 下标 i;
        else {
            std::swap(v[i - 1], v[i]);
            --i;
        } // 否则
    }
    return v; // 返回 值
}
int main() {
    assert((gnomeSort({5, 4, 3, 2, 1}) == std::vector<int>{1, 2, 3, 4, 5}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS