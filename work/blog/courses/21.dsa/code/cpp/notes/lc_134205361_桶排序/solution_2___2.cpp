// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361
// 数据结构与算法之排序: 桶排序 — C++ 版（方案2）
#include <cassert>                                        // 引入头文件
#include <iostream>                                       // 引入头文件
#include <vector>                                         // 引入头文件
static int getIndex(const std::vector<int> &arr, int k) { // 定义函数/方法 getIndex
    for (int v : arr)
        if (v == k)
            return k; // 把 赋值为 下标 k) return 下标 k; 写入 for (int v : arr) if (v
    return -1;        // 返回 减 1
}
int main() {                              // 程序入口：跑内嵌自测用例
    assert(getIndex({1, 2, 3}, 1) == 1);  // 断言校验
    assert(getIndex({1, 2, 3}, 3) == 3);  // 断言校验
    assert(getIndex({1, 2, 3}, 5) == -1); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS