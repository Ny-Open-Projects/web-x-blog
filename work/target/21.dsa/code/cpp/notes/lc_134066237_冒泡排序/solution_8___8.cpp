// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237
// 数据结构与算法之排序: 冒泡排序 — C++ 版（方案8）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> gnomeSortBubble(std::vector<int> v) {
    for (size_t i = 0; i < v.size(); ++i) // 让 下标 i 从 0 开始计数，下标 i 小于 值.大小() 就继续
        for (size_t j = 0; j + 1 < v.size() - i;
             ++j) // 让 下标 j 从 0 开始计数，下标 j 加 1 小于 值.大小() 减 下标 i 就继续
            if (v[j] > v[j + 1])
                std::swap(
                    v[j],
                    v[j + 1]); // 若 值[下标 j] 超过 值[下标 j 加 1]) std::交换 值[下标 j], 值[下标 j 加 1]);
    return v; // 返回 值
}
int main() { // 程序入口：跑内嵌自测用例
    assert((gnomeSortBubble({5, 4, 3, 2, 1}) == std::vector<int>{1, 2, 3, 4, 5})); // 断言校验
    assert((gnomeSortBubble({3, 1, 2}) == std::vector<int>{1, 2, 3}));             // 断言校验
    assert(gnomeSortBubble({}).empty());                                           // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS