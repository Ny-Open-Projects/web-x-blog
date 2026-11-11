// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
// 数据结构与算法之排序: 快速排序 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> quickSort(const std::vector<int> &nums) {
    if (nums.size() <= 1)
        return nums;                   // 若 数组.大小() 不超过 1，直接返回 数组
    int pivot = nums[nums.size() / 2]; // 把 数组[数组.大小() 除以 2] 存入 pivot
    std::vector<int> lt, eq, gt;       // std::vector 小于 int 超过 lt, eq, gt;
    for (int x : nums) {               // for (int x : 数组) {
        if (x < pivot)
            lt.push_back(x); // 若 x 小于 pivot) lt 追加 x);
        else if (x == pivot)
            eq.push_back(x); // 否则，若 x 等于 pivot) eq 追加 x);
        else
            gt.push_back(x); // 否则
    }
    auto out = quickSort(lt);                    // 把 quickSort(lt) 存入 out
    out.insert(out.end(), eq.begin(), eq.end()); // out 插入 out.终点(), eq 迭代位置 , eq.终点());
    auto r = quickSort(gt);                      // 把 quickSort(gt) 存入 右指针
    out.insert(out.end(), r.begin(), r.end()); // out 插入 out.终点(), 右指针 迭代位置 , 右指针.终点());
    return out;                                // 返回 out
}
int main() { // 程序入口：跑内嵌自测用例
    assert((quickSort({5, 4, 3, 2, 1}) == std::vector<int>{1, 2, 3, 4, 5})); // 断言校验
    assert((quickSort({3, 1, 4, 1, 5}) == std::vector<int>{1, 1, 3, 4, 5})); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS