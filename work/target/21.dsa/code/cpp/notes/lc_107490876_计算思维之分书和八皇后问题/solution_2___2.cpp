// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — C++ 版（方案2：分书，函数式不可变副本）
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

static const int LIKE[5][5] = {
    // 把 { 写入 static const int LIKE[5][5]
    {0, 0, 1, 1, 0}, {1, 1, 0, 0, 1}, {0, 1, 1, 0, 1}, {0, 0, 0, 1, 0}, {0, 1, 0, 0, 1},
};

static void try_assign(int reader, std::vector<int> assigned,
                       std::vector<std::vector<int>>
                           &results) { // std::vector 小于 std::vector 小于 int 超过 超过 按位与 results) {
    if (reader == 5) {                 // 若 reader 等于 5
        results.push_back(assigned); // results 追加 assigned);
        return;                      // return;
    }
    for (int book = 0; book < 5; ++book) { // 让 book 从 0 开始计数，book 小于 5 就继续
        if (LIKE[reader][book] == 1 &&
            assigned[book] == -1) { // 若 LIKE[reader][book] 等于 1 且 assigned[book] 等于 减 1
            std::vector<int> nxt = assigned;      // 把 assigned; 写入 std::vector<int> nxt
            nxt[book] = reader;                   // 把 reader; 写入 nxt[book]
            try_assign(reader + 1, nxt, results); // try_assign(reader 加 1, nxt, results);
        }
    }
}

int main() {                               // 程序入口：跑内嵌自测用例
    std::vector<std::vector<int>> results; // std::vector 小于 std::vector 小于 int 超过 超过 results;
    try_assign(0, std::vector<int>(5, -1),
               results); // try_assign(0, std::vector 小于 int 超过 (5, 减 1), results);
    std::vector<std::vector<int>> want = {{1, 2, 0, 3, 4}, {1, 4, 0, 3, 2}};
    if (results != want) {
        std::cout << "mismatch" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
