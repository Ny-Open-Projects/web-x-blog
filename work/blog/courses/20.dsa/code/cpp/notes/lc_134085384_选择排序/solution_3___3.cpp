// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085384
// 数据结构与算法之排序: 选择排序 — C++ 版（方案3）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> selectionSort(std::vector<int> v) {
    for (size_t i = 0; i + 1 < v.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 加 1 小于 值.大小() 就继续
        size_t m = i;                           // 把 下标 i; 写入 size_t m
        for (size_t j = i + 1; j < v.size(); ++j)
            if (v[j] < v[m])
                m = j; // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 值.大小() 就继续
        std::swap(v[i], v[m]); // 交换 值[下标 i] 与 值[映射表]
    }
    return v; // 返回 值
}
int main() {
    assert((selectionSort({5, 4, 3, 2, 1}) == std::vector<int>{1, 2, 3, 4, 5}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS