// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
// LeetCode 107524703. 人鬼渡河问题 — C++ 版（方案1：安全判定谓词）
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

static bool is_safe(int r, int g) { // 定义判定函数 is_safe
    return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::tuple<int, int, bool>> cases = {
        // 把 { 写入 std::vector<std::tuple<int, int, bool>> cases
        {3, 3, true}, {3, 1, true}, {2, 2, true}, {1, 3, false}, {0, 0, true},
    };
    for (auto &[r, g, want] : cases) { // for (auto 按位与 [右指针, g, want] : cases) {
        if (is_safe(r, g) != want) {
            std::cout << "is_safe failed" << std::endl;
            return 1;
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
