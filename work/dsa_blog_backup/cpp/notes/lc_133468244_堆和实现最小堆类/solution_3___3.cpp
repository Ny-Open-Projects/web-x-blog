// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133468244
// 数据结构与算法之堆: 堆和实现最小堆类 — C++ 版（方案3）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> minHeapPopAll(const std::vector<int> &input) {
    std::vector<int> h;             // std::vector 小于 int 超过 h;
    auto up = [&](size_t i) {       // 把 [ 按位与 ](size_t 下标 i) { 存入 up
        while (i > 0) {             // 循环，直到不满足「下标 i 超过 0」
            size_t p = (i - 1) / 2; // 把 (下标 i 减 1) 除以 2; 写入 size_t p
            if (h[p] <= h[i])
                break;             // 若 h[节点] 不超过 h[下标 i]) break;
            std::swap(h[p], h[i]); // 交换 h[节点] 与 h[下标 i]
            i = p;                 // 把 节点; 写入 下标 i
        }
    };
    auto down = [&](size_t i) { // 把 [ 按位与 ](size_t 下标 i) { 存入 down
        size_t n = h.size();    // 把 h.大小(); 写入 size_t n
        while (true) {          // 循环，直到不满足「true」
            size_t l = 2 * i + 1, r = 2 * i + 2, m = i;
            if (l < n && h[l] < h[m])
                m = l; // 若 左指针 小于 元素个数 且 h[左指针] 小于 h[映射表]) 映射表 赋值为 左指针;
            if (r < n && h[r] < h[m])
                m = r; // 若 右指针 小于 元素个数 且 h[右指针] 小于 h[映射表]) 映射表 赋值为 右指针;
            if (m == i)
                break;             // 若 映射表 等于 下标 i) break;
            std::swap(h[i], h[m]); // 交换 h[下标 i] 与 h[映射表]
            i = m;                 // 把 映射表; 写入 下标 i
        }
    };
    for (int v : input) { // for (int 值 : input) {
        h.push_back(v);   // h 追加 值);
        up(h.size() - 1); // up(h.大小() 减 1);
    }
    std::vector<int> out;    // std::vector 小于 int 超过 out;
    while (!h.empty()) {     // 循环，直到不满足「取反 h.empty(」
        out.push_back(h[0]); // out 追加 h[0]);
        int last = h.back(); // 把 h.back() 存入 last
        h.pop_back();        // 弹出栈顶元素
        if (!h.empty()) {
            h[0] = last;
            down(0);
        } // 若 取反 h 是否为空) { h[0] 赋值为 last; down(0); }
    }
    return out; // 返回 out
}
int main() { // 程序入口：跑内嵌自测用例
    assert((minHeapPopAll({3, 1, 6, 5, 2, 4}) == std::vector<int>{1, 2, 3, 4, 5, 6})); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS