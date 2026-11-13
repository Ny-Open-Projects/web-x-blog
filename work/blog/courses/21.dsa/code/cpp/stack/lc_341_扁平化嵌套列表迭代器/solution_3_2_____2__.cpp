// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145078849
// LeetCode 341. 扁平化嵌套列表迭代器 — C++ 版（方案3）
#include <cassert>                          // 引入头文件
#include <iostream>                         // 引入头文件
#include <memory>                           // 引入头文件
#include <vector>                           // 引入头文件
struct NI {                                 // 定义类型
    bool isInt;                             // bool isInt;
    int intVal = 0;                         // 把 0 存入 intVal
    std::vector<std::unique_ptr<NI>> items; // std::vector 小于 std::unique_ptr 小于 NI 超过 超过 items;
    static std::unique_ptr<NI> Int(int v) { // static std::unique_ptr 小于 NI 超过 Int(int 值) {
        auto n = std::make_unique<NI>();    // 把 std::make_unique 小于 NI 超过 () 存入 元素个数
        n->isInt = true;                    // 把 true; 写入 n->isInt
        n->intVal = v;                      // 把 值; 写入 n->intVal
        return n;                           // 返回 元素个数
    }
    static std::unique_ptr<NI> List() {  // static std::unique_ptr 小于 NI 超过 List() {
        auto n = std::make_unique<NI>(); // 把 std::make_unique 小于 NI 超过 () 存入 元素个数
        n->isInt = false;                // 把 false; 写入 n->isInt
        return n;                        // 返回 元素个数
    }
};
static void flatten(const NI *ni, std::vector<int> &out) { // 定义函数/方法 flatten
    if (ni->isInt) {
        out.push_back(ni->intVal);
        return;
    } // 若 ni 减 超过 isInt) { out 追加 ni 减 超过 intVal); return; }
    for (const auto &it : ni->items)
        flatten(it.get(), out); // 逐个取出 ni 减 超过 items 的元素（it）
}
int main() {                                       // 程序入口：跑内嵌自测用例
    auto top = NI::List();                         // 把 NI::List() 存入 top
    top->items.push_back(NI::Int(1));              // top 减 超过 items 追加 NI::Int(1));
    top->items.push_back(NI::Int(2));              // top 减 超过 items 追加 NI::Int(2));
    auto sub = NI::List();                         // 把 NI::List() 存入 sub
    sub->items.push_back(NI::Int(3));              // sub 减 超过 items 追加 NI::Int(3));
    sub->items.push_back(NI::Int(4));              // sub 减 超过 items 追加 NI::Int(4));
    top->items.push_back(std::move(sub));          // top 减 超过 items 追加 std::move(sub));
    std::vector<int> out;                          // std::vector 小于 int 超过 out;
    flatten(top.get(), out);                       // flatten(top 查找 ), out);
    assert((out == std::vector<int>{1, 2, 3, 4})); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS