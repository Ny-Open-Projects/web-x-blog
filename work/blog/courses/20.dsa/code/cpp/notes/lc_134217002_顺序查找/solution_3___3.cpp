// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134217002
// 数据结构与算法之查找: 顺序查找 — C++ 版（方案3）
#include <cassert>                                           // 引入头文件
#include <iostream>                                          // 引入头文件
#include <vector>                                            // 引入头文件
static int seqSearch(const std::vector<int> &arr, int key) { // 定义函数/方法 seqSearch
    for (size_t i = 0; i < arr.size(); ++i)
        if (arr[i] == key)
            return static_cast<int>(i); // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
    return -1;                          // 返回 减 1
}
int main() {                               // 程序入口：跑内嵌自测用例
    assert(seqSearch({1, 2, 3}, 1) == 0);  // 断言校验
    assert(seqSearch({1, 2, 3}, 2) == 1);  // 断言校验
    assert(seqSearch({1, 2, 3}, 4) == -1); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS