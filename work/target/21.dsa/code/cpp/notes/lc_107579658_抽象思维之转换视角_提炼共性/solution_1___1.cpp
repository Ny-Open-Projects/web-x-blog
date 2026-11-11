// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107579658
// LeetCode 107579658. 转换视角，提炼共性 — C++ 版（抽象思维之转换视角：统一分书问题与八皇后的回溯框架）
// queen=false: 分书问题（5人，like 偏好矩阵）; queen=true: 八皇后
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

class Unified {                                                          // 定义类型
  public:                                                                // public:
    explicit Unified(bool queen) : queen_(queen), size_(queen ? 8 : 5) { // 定义函数/方法 Unified
        q_.assign(size_, -1);                                            // q_.assign(size_, 减 1);
        rows_.assign(size_, true);                                       // rows_.assign(size_, true);
        diag1_.assign(2 * size_ - 1, true); // diag1_.assign(2 乘 size_ 减 1, true);
        diag2_.assign(2 * size_ - 1, true); // diag2_.assign(2 乘 size_ 减 1, true);
    }

    std::vector<std::vector<int>> solve() { // std::vector 小于 std::vector 小于 int 超过 超过 solve() {
        place(0);                           // place(0);
        return results_;                    // 返回 results_
    }

  private: // private:
    static const std::vector<std::vector<int>>
        LIKE; // static const std::vector 小于 std::vector 小于 int 超过 超过 LIKE;

    bool is_valid(int row, int col) const { // bool is_valid(int row, int col) const {
        if (queen_)
            return true;            // 若 queen_，直接返回 true
        return LIKE[row][col] == 1; // 返回 LIKE[row][col] 等于 1
    }

    bool is_safe(int row, int col) const { // bool is_safe(int row, int col) const {
        if (queen_)
            return rows_[row] && diag1_[col - row + size_ - 1] && diag2_[col + row];
        return rows_[row]; // 返回 rows_[row]
    }

    void place(int col) {                     // 定义函数/方法 place
        if (col == static_cast<int>(size_)) { // 若 col 等于 static_cast 小于 int 超过 (size_
            results_.push_back(q_);           // results_ 追加 q_);
            return;                           // return;
        }
        for (int row = 0; row < static_cast<int>(size_);
             ++row) { // 让 row 从 0 开始计数，row 小于 static_cast 小于 int 超过 (size_) 就继续
            if (!is_valid(row, col))
                continue; // 若 取反 is_valid(row, col)) continue;
            if (!is_safe(row, col))
                continue;                              // 若 取反 is_safe(row, col)) continue;
            q_[col] = row;                             // 把 row; 写入 q_[col]
            rows_[row] = false;                        // 把 false; 写入 rows_[row]
            if (queen_) {                              // 若 queen_
                diag1_[col - row + size_ - 1] = false; // 把 false; 写入 diag1_[col - row + size_ - 1]
                diag2_[col + row] = false;             // 把 false; 写入 diag2_[col + row]
            }
            place(col + 1);                           // place(col 加 1);
            rows_[row] = true;                        // 把 true; 写入 rows_[row]
            if (queen_) {                             // 若 queen_
                diag1_[col - row + size_ - 1] = true; // 把 true; 写入 diag1_[col - row + size_ - 1]
                diag2_[col + row] = true;             // 把 true; 写入 diag2_[col + row]
            }
        }
    }

    bool queen_;                            // bool queen_;
    size_t size_;                           // size_t size_;
    std::vector<int> q_;                    // std::vector 小于 int 超过 q_;
    std::vector<bool> rows_;                // std::vector 小于 bool 超过 rows_;
    std::vector<bool> diag1_, diag2_;       // std::vector 小于 bool 超过 diag1_, diag2_;
    std::vector<std::vector<int>> results_; // std::vector 小于 std::vector 小于 int 超过 超过 results_;
};

const std::vector<std::vector<int>> Unified::LIKE = {
    // 把 { 写入 const std::vector<std::vector<int>> Unified::LIKE
    {0, 0, 1, 1, 0}, {1, 1, 0, 0, 1}, {0, 1, 1, 0, 1}, {0, 0, 0, 1, 0}, {0, 1, 0, 0, 1},
};

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::vector<int>> want = {{1, 2, 0, 3, 4}, {1, 4, 0, 3, 2}};
    Unified solver(false); // Unified solver(false);
    std::vector<std::vector<int>> got =
        solver.solve(); // 把 solver.solve(); 写入 std::vector<std::vector<int>> got
    if (got != want) {
        std::cout << "FAIL mismatch" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
