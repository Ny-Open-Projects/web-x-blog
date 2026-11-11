// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085409
// 数据结构与算法之排序: 堆排序 — C++ 版（方案1）
#include <cassert>                                                // 引入头文件
#include <iostream>                                               // 引入头文件
#include <vector>                                                 // 引入头文件
static void sift(std::vector<int> &v, size_t start, size_t end) { // 定义函数/方法 sift
    size_t root = start;                                          // 把 起点; 写入 size_t root
    while (true) {                                                // 循环，直到不满足「true」
        size_t child = 2 * root + 1; // 把 2 乘 根节点 加 1; 写入 size_t child
        if (child > end)
            break;          // 若 子节点 超过 终点) break;
        size_t swap = root; // 把 根节点; 写入 size_t swap
        if (v[swap] < v[child])
            swap = child; // 若 值[swap] 小于 值[子节点]) swap 赋值为 子节点;
        if (child + 1 <= end && v[swap] < v[child + 1])
            swap = child +
                   1; // 若 子节点 加 1 不超过 终点 且 值[swap] 小于 值[子节点 加 1]) swap 赋值为 子节点 加 1;
        if (swap == root)
            break;                   // 若 swap 等于 根节点) break;
        std::swap(v[root], v[swap]); // 交换 值[根节点] 与 值[swap]
        root = swap;                 // 把 swap; 写入 根节点
    }
}
static std::vector<int> heapSort(std::vector<int> v) {
    if (v.empty())
        return v;        // 若 值 是否为空，直接返回 值
    size_t n = v.size(); // 把 值.大小(); 写入 size_t n
    for (size_t i = n / 2; i > 0; --i)
        sift(v, i - 1, n - 1); // 让 下标 i 从 元素个数 除以 2 开始计数，下标 i 超过 0 就继续
    for (size_t end = n; end > 1; --end) { // 让 终点 从 元素个数 开始计数，终点 超过 1 就继续
        std::swap(v[0], v[end - 1]);       // 交换 值[0] 与 值[终点 减 1]
        sift(v, 0, end - 2);               // sift(值, 0, 终点 减 2);
    }
    return v; // 返回 值
}
int main() { // 程序入口：跑内嵌自测用例
    assert((heapSort({5, 2, 4, 6, 1, 3}) == std::vector<int>{1, 2, 3, 4, 5, 6})); // 断言校验
    assert((heapSort({9, 8, 7, 6, 5}) == std::vector<int>{5, 6, 7, 8, 9}));       // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS