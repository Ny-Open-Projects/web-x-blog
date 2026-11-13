// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134082074
// 数据结构与算法之排序: 插入排序 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> insertionSort(std::vector<int> v) {
    for (size_t i = 1; i < v.size(); ++i) { // 让 下标 i 从 1 开始计数，下标 i 小于 值.大小() 就继续
        int key = v[i];                     // 把 值[下标 i] 存入 key
        size_t j = i;                       // 把 下标 i; 写入 size_t j
        while (j > 0 && v[j - 1] > key) {
            v[j] = v[j - 1];
            --j;
        }
        v[j] = key; // 把 key; 写入 v[j]
    }
    return v; // 返回 值
}
int main() {
    assert((insertionSort({5, 4, 3, 2, 1}) == std::vector<int>{1, 2, 3, 4, 5}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS