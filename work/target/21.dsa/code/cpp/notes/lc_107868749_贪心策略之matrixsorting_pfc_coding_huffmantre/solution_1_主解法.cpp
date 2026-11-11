// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107868749
// LeetCode 107868749. 贪心策略 — C++ 版（贪心策略之 matrixSort / PFC 编码 / Huffman 树）
#include <algorithm>     // 引入头文件
#include <iostream>      // 引入头文件
#include <string>        // 引入头文件
#include <unordered_map> // 引入头文件
#include <vector>        // 引入头文件

static void matrix_sort(std::vector<std::vector<int>> &matrix) { // 定义函数/方法 matrix_sort
    if (matrix.empty())
        return; // 若 矩阵 是否为空) return;
    size_t rows = matrix.size(),
           cols = matrix[0].size(); // 把 矩阵.大小(), 列数 赋值为 矩阵[0].大小(); 写入 size_t rows
    for (size_t c = 0; c < cols; ++c) { // 让 字符 从 0 开始计数，字符 小于 列数 就继续
        std::vector<int> col;           // std::vector 小于 int 超过 col;
        for (size_t r = 0; r < rows; ++r)
            col.push_back(matrix[r][c]); // 让 右指针 从 0 开始计数，右指针 小于 行数 就继续
        std::sort(col.begin(), col.end()); // std::sort(col 迭代位置 , col.终点());
        for (size_t r = 0; r < rows; ++r)
            matrix[r][c] = col[r]; // 让 右指针 从 0 开始计数，右指针 小于 行数 就继续
    }
    for (size_t r = 0; r < rows; ++r)
        std::sort(matrix[r].begin(), matrix[r].end()); // 让 右指针 从 0 开始计数，右指针 小于 行数 就继续
}

struct Huff {              // 定义类型
    long long freq;        // long long 频次表;
    std::string sym;       // 叶子时非空
    Huff *left = nullptr;  // 把 nullptr; 写入 Huff *left
    Huff *right = nullptr; // 把 nullptr; 写入 Huff *right
    bool leaf = false;     // 把 false 存入 leaf
};

static Huff *build_huffman(const std::vector<std::pair<std::string, long long>> &freqs) {
    std::vector<std::pair<long long, Huff *>>
        nodes; // std::vector 小于 std::pair 小于 long long, Huff 乘 超过 超过 nodes;
    for (const auto &p : freqs) { // 逐个取出 freqs 的元素（节点）
        nodes.push_back({p.second, new Huff{p.second, p.first, nullptr, nullptr, true}});
    }
    std::sort(nodes.begin(), nodes.end(), [](const auto &a, const auto &b) { return a.first < b.first; });
    while (nodes.size() > 1) {          // 循环，直到不满足「nodes.大小() 超过 1」
        Huff *a = nodes.front().second; // 把 nodes.front().second; 写入 Huff *a
        nodes.erase(nodes.begin());     // nodes 删除 nodes 迭代位置 );
        Huff *b = nodes.front().second; // 把 nodes.front().second; 写入 Huff *b
        nodes.erase(nodes.begin());     // nodes 删除 nodes 迭代位置 );
        Huff *merged = new Huff{a->freq + b->freq, "", a, b, false};
        size_t i = 0; // 把 0; 写入 size_t i
        while (i < nodes.size() && nodes[i].first < merged->freq)
            ++i;
        nodes.insert(
            nodes.begin() + i,
            {merged->freq, merged}); // nodes 插入 nodes 迭代位置 加 下标 i, {merged 减 超过 频次表, merged});
    }
    return nodes.front().second; // 返回 nodes.front().second
}

static void walk(Huff *node, const std::string &prefix, std::unordered_map<std::string, std::string> &codes) {
    if (node->leaf) { // 若 节点 减 超过 leaf
        codes[node->sym] =
            prefix.empty() ? "0" : prefix; // 把 prefix 是否为空 ? 「0」 : prefix; 写入 codes[node->sym]
        return;                            // return;
    }
    walk(node->left, prefix + "0", codes);  // walk(节点 减 超过 左边界, prefix 加 「0」, codes);
    walk(node->right, prefix + "1", codes); // walk(节点 减 超过 右边界, prefix 加 「1」, codes);
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::pair<std::string, long long>> freqs = {
        // 把 { 写入 std::vector<std::pair<std::string, long long>> freqs
        {"A", 5}, {"B", 9}, {"C", 12}, {"D", 13}, {"E", 16}, {"F", 45}};

    // case1: matrixSort
    std::vector<std::vector<int>> mat = {{5, 3, 4}, {1, 6, 2}, {7, 9, 8}};
    matrix_sort(mat); // matrix_sort(mat);
    std::vector<std::vector<int>> want = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    if (mat != want) {
        std::cout << "matrixSort mismatch" << std::endl;
        return 1;
    }

    // case2: WPL
    auto codes = std::unordered_map<std::string, std::string>{};
    walk(build_huffman(freqs), "", codes);     // walk(build_huffman(freqs), 「」, codes);
    long long wpl = 0;                         // 把 0 存入 wpl
    std::vector<std::string> code_list;        // std::vector 小于 std::string 超过 code_list;
    for (const auto &p : freqs) {              // 逐个取出 freqs 的元素（节点）
        const std::string &c = codes[p.first]; // 把 codes[节点.first]; 写入 const std::string &c
        wpl +=
            p.second * static_cast<long long>(
                           c.size()); // wpl累加 节点.second 乘 static_cast 小于 long long 超过 (字符.大小())
        code_list.push_back(c); // code_list 追加 字符);
    }
    if (wpl != 224) {
        std::cout << "WPL mismatch: " << wpl << std::endl;
        return 1;
    }

    // case3: 前缀无关
    bool prefix_free = true; // 把 true 存入 prefix_free
    for (size_t i = 0; i < code_list.size();
         ++i) // 让 下标 i 从 0 开始计数，下标 i 小于 code_list.大小() 就继续
        for (size_t j = 0; j < code_list.size();
             ++j) // 让 下标 j 从 0 开始计数，下标 j 小于 code_list.大小() 就继续
            if (i != j && code_list[j].compare(0, code_list[i].size(), code_list[i]) == 0)
                prefix_free = false; // 把 false; 写入 prefix_free
    if (!prefix_free) {
        std::cout << "not prefix-free" << std::endl;
        return 1;
    }

    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
