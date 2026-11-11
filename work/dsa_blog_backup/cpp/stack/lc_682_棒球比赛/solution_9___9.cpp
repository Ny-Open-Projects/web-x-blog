// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734875
// LeetCode 682. 棒球比赛 — C++ 版（方案9）
#include <cassert>                                          // 引入头文件
#include <iostream>                                         // 引入头文件
#include <string>                                           // 引入头文件
#include <vector>                                           // 引入头文件
static int calPoints(const std::vector<std::string> &ops) { // 定义函数/方法 calPoints
    std::vector<int> st;                                    // std::vector 小于 int 超过 st;
    for (const auto &op : ops) {                            // 逐个取出 ops 的元素（op）
        if (op == "+")
            st.push_back(
                st[st.size() - 1] +
                st[st.size() - 2]); // 若 op 等于 「 加 」) st 追加 st[st.大小() 减 1] 加 st[st.大小() 减 2]);
        else if (op == "D")
            st.push_back(2 * st.back()); // 否则，若 op 等于 「D」) st 追加 2 乘 st.back());
        else if (op == "C")
            st.pop_back(); // 否则，若 op 等于 「C」) st 弹出 );
        else
            st.push_back(std::stoi(op)); // 否则
    }
    int sum = 0; // 把 0 存入 累计和
    for (int v : st)
        sum += v; // 把 值; 写入 for (int v : st) sum +
    return sum;   // 返回 累计和
}
int main() {
    assert(calPoints({"5", "2", "C", "D", "+"}) == 30);
    assert(calPoints({"5", "-2", "4", "C", "D", "9", "+", "+"}) == 27);
    assert(calPoints({"1", "C"}) == 0);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS