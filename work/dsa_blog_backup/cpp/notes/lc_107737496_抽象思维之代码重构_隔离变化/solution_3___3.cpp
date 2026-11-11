// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案3：螺旋矩阵递归填充）
#include <iostream> // 引入头文件
#include <sstream>  // 引入头文件
#include <string>   // 引入头文件
#include <vector>   // 引入头文件

class Matrix { // 定义类型
  public:      // public:
    explicit Matrix(int size) : n_(size), m_(size, std::vector<int>(size, 0)) {}

    void fill(int num, int begin, int size) { // 定义函数/方法 fill
        if (size == 0)
            return; // 若 大小 等于 0) return;
        if (size == 1) {
            m_[begin][begin] = num;
            return;
        } // 若 大小 等于 1) { 行数[begin][begin] 赋值为 num; return; }
        for (int j = 0; j < size - 1; ++j) {
            m_[begin + j][begin] = num++;
        } // 让 下标 j 从 0 开始计数，下标 j 小于 大小 减 1 就继续
        for (int j = 0; j < size - 1; ++j) {
            m_[begin + size - 1][begin + j] = num++;
        } // 让 下标 j 从 0 开始计数，下标 j 小于 大小 减 1 就继续
        for (int j = size - 1; j > 0; --j) {
            m_[begin + j][begin + size - 1] = num++;
        } // 让 下标 j 从 大小 减 1 开始计数，下标 j 超过 0 就继续
        for (int j = size - 1; j > 0; --j) {
            m_[begin][begin + j] = num++;
        } // 让 下标 j 从 大小 减 1 开始计数，下标 j 超过 0 就继续
        fill(num, begin + 1, size - 2); // fill(num, begin 加 1, 大小 减 2);
    }

    const std::vector<std::vector<int>> &rows() const { return m_; }

  private:                            // private:
    int n_;                           // int 列数;
    std::vector<std::vector<int>> m_; // std::vector 小于 std::vector 小于 int 超过 超过 行数;
};

static std::string fmt_row(const std::vector<int> &row) {
    std::ostringstream oss;                   // std::ostringstream oss;
    for (size_t i = 0; i < row.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 row.大小() 就继续
        if (i)
            oss << " "; // 若 下标 i) oss 小于 小于 「 」;
        oss.width(2);   // oss.width(2);
        oss << row[i];  // oss 小于 小于 row[下标 i];
    }
    return oss.str(); // 返回 oss.str()
}

int main() {         // 程序入口：跑内嵌自测用例
    Matrix m(6);     // Matrix 映射表(6);
    m.fill(1, 0, 6); // 映射表.fill(1, 0, 6);
    const char *want[6] = {
        // 把 { 写入 const char *want[6]
        " 1 20 19 18 17 16", " 2 21 32 31 30 15", " 3 22 33 36 29 14",
        " 4 23 34 35 28 13", " 5 24 25 26 27 12", " 6  7  8  9 10 11",
    };
    for (int i = 0; i < 6; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
        std::string got = fmt_row(m.rows()[i]); // 把 fmt_row(映射表.行数()[下标 i]); 写入 std::string got
        if (got != want[i]) {
            std::cout << "spiral6 row " << i << " failed" << std::endl;
            return 1;
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
