// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134350547
// LeetCode 384. 打乱数组 — C++ 版（方案2）
#include <algorithm>            // 引入头文件
#include <cassert>              // 引入头文件
#include <iostream>             // 引入头文件
#include <vector>               // 引入头文件
struct ShuffleArray {           // 定义类型
    std::vector<int> orig, cur; // std::vector 小于 int 超过 orig, 当前值;
    explicit ShuffleArray(const std::vector<int> &vals) : orig(vals), cur(vals) {}
    std::vector<int> reset() {
        cur = orig;
        return cur;
    }                            // 把 orig; return 当前值; } 写入 std::vector<int> reset() { cur
    std::vector<int> shuffle() { // std::vector 小于 int 超过 shuffle() {
        for (size_t i = cur.size(); i > 1; --i) { // 让 下标 i 从 当前值.大小() 开始计数，下标 i 超过 1 就继续
            std::swap(cur[i - 1], cur[0]); // 交换 当前值[下标 i 减 1] 与 当前值[0]
        }
        return cur; // 返回 当前值
    }
};
int main() {                                         // 程序入口：跑内嵌自测用例
    ShuffleArray s({1, 2, 3});                       // ShuffleArray 字符串({1, 2, 3});
    auto sh = s.shuffle();                           // 把 字符串.shuffle() 存入 sh
    auto sortedSh = sh;                              // 把 sh 存入 sortedSh
    std::sort(sortedSh.begin(), sortedSh.end());     // std::sort(sortedSh 迭代位置 , sortedSh.终点());
    assert((sortedSh == std::vector<int>{1, 2, 3})); // 断言校验
    auto r = s.reset();                              // 把 字符串.reset() 存入 右指针
    assert((r == std::vector<int>{1, 2, 3}));        // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS