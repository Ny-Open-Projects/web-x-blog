// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114689
// LeetCode 27. 移除元素 — C++ 版（方案3）
#include <cassert>                                          // 引入头文件
#include <iostream>                                         // 引入头文件
#include <vector>                                           // 引入头文件
static int removeElement(std::vector<int> &nums, int val) { // 定义函数/方法 removeElement
    size_t k = 0;                                           // 把 0; 写入 size_t k
    for (size_t i = 0; i < nums.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
        if (nums[i] != val)
            nums[k++] = nums[i]; // 若 数组[下标 i] 不等于 值) 数组[下标 k 加一 ] 赋值为 数组[下标 i];
    }
    return static_cast<int>(k); // 返回 static_cast 小于 int 超过 (下标 k)
}
int main() {                                        // 程序入口：跑内嵌自测用例
    std::vector<int> v = {3, 2, 2, 3};              // 把 {3, 2, 2, 3}; 写入 std::vector<int> v
    assert(removeElement(v, 3) == 2);               // 断言校验
    assert(v[0] == 2 && v[1] == 2);                 // 断言校验
    std::vector<int> v2 = {0, 1, 2, 2, 3, 0, 4, 2}; // 把 {0, 1, 2, 2, 3, 0, 4, 2}; 写入 std::vector<int> v2
    assert(removeElement(v2, 2) == 5);              // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS