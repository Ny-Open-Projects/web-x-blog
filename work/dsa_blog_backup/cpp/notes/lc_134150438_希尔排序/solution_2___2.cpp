// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134150438
// 数据结构与算法之排序: 希尔排序 — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> shellSort(std::vector<int> v) {
    size_t n = v.size();                          // 把 值.大小(); 写入 size_t n
    for (size_t gap = n / 2; gap > 0; gap /= 2) { // 让 gap 从 元素个数 除以 2 开始计数，gap 超过 0 就继续
        for (size_t i = gap; i < n; ++i) { // 让 下标 i 从 gap 开始计数，下标 i 小于 元素个数 就继续
            int key = v[i];                // 把 值[下标 i] 存入 key
            size_t j = i;                  // 把 下标 i; 写入 size_t j
            while (j >= gap && v[j - gap] > key) {
                v[j] = v[j - gap];
                j -= gap;
            }
            v[j] = key; // 把 key; 写入 v[j]
        }
    }
    return v; // 返回 值
}
int main() {
    assert((shellSort({5, 2, 4, 6, 1, 3}) == std::vector<int>{1, 2, 3, 4, 5, 6}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS