// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案5：Matrix 封装 set/call）
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

class Matrix { // 定义类型
  public:      // public:
    Matrix(int r, int c) : row_(r), col_(c), buf_(r, std::vector<int>(c, 0)) {}
    void set(int r, int c, int v) {
        buf_[r][c] = v;
    } // 把 值; } 写入 void set(int r, int c, int v) { buf_[r][c]
    int call(int r, int c) const {
        return buf_[r][c];
    } // int call(int 右指针, int 字符) const { return buf_[右指针][字符]; }

  private:                              // private:
    int row_;                           // int row_;
    int col_;                           // int col_;
    std::vector<std::vector<int>> buf_; // std::vector 小于 std::vector 小于 int 超过 超过 buf_;
};

int main() {                        // 程序入口：跑内嵌自测用例
    Matrix m(4, 5);                 // Matrix 映射表(4, 5);
    for (int i = 0; i < 4; ++i)     // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
        for (int j = 0; j < 5; ++j) // 让 下标 j 从 0 开始计数，下标 j 小于 5 就继续
            m.set(i, j, i * j);     // 映射表.set(下标 i, 下标 j, 下标 i 乘 下标 j);
    if (m.call(2, 3) != 6) {
        std::cout << "matrix call failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
