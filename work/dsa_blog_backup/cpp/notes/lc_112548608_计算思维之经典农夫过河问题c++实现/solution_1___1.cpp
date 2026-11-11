// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/112548608
// LeetCode 112548608. 计算思维之经典农夫过河问题C++实现（DFS 求任一可行过河序列）
#include <iostream> // 引入头文件
#include <set>      // 引入头文件
#include <string>   // 引入头文件
#include <vector>   // 引入头文件

static bool invalid(const std::vector<int> &st) { // 定义函数/方法 invalid
    int h = st[0], w = st[1], s = st[2],
        v = st[3]; // 把 st[0], 权重 赋值为 st[1], 字符串 赋值为 st[2], 值 赋值为 st[3] 存入 h
    if (h != s && s == w)
        return true; // 若 h 不等于 字符串 且 字符串 等于 权重，直接返回 true
    if (h != s && s == v)
        return true; // 若 h 不等于 字符串 且 字符串 等于 值，直接返回 true
    return false;    // 返回 false
}

static std::vector<char> solve_farmer() { // static std::vector 小于 char 超过 solve_farmer() {
    std::vector<char> path;               // std::vector 小于 char 超过 当前路径;
    std::set<std::string> visited;        // std::set 小于 std::string 超过 已访问集合;
    static const char roles[4] = {'-', 'W', 'S',
                                  'V'}; // 把 { ' 减 ', 'W', 'S', 'V' }; 写入 static const char roles[4]
    static const int role_idx[4] = {0, 1, 2, 3}; // 把 { 0, 1, 2, 3 }; 写入 static const int role_idx[4]

    std::function<bool(std::vector<int>)> go = [&](std::vector<int> st) -> bool {
        if (st == std::vector<int>{1, 1, 1, 1})
            return true; // 若 st 等于 std::vector 小于 int 超过 {1, 1, 1, 1}，直接返回 true
        std::string key; // std::string key;
        for (size_t i = 0; i < 4; ++i) {
            if (i)
                key += ",";
            key += std::to_string(st[i]);
        } // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
        if (visited.count(key))
            return false;                // 若 已访问集合.计数(key)，直接返回 false
        visited.insert(key);             // 已访问集合 插入 key);
        for (int ri = 0; ri < 4; ++ri) { // 让 ri 从 0 开始计数，ri 小于 4 就继续
            std::vector<int> ns = st;    // 把 st; 写入 std::vector<int> ns
            ns[0] = 1 - ns[0];           // 农夫总是过河
            if (ri != 0) {               // 若 ri 不等于 0
                int idx = role_idx[ri];  // 把 role_idx[ri] 存入 idx
                if (st[0] != st[idx])
                    continue;          // 出发前同岸
                ns[idx] = 1 - ns[idx]; // 把 1 减 ns[idx]; 写入 ns[idx]
            }
            if (invalid(ns))
                continue;                  // 若 invalid(ns)) continue;
            if (go(ns)) {                  // 若 go(ns
                path.push_back(roles[ri]); // 当前路径 追加 roles[ri]);
                return true;               // 返回 true
            }
        }
        return false; // 返回 false
    };

    go({0, 0, 0, 0});                       // go({0, 0, 0, 0});
    std::reverse(path.begin(), path.end()); // std::reverse(当前路径 迭代位置 , 当前路径.终点());
    return path;                            // 返回 当前路径
}

static bool simulate(const std::vector<char> &path) { // 定义函数/方法 simulate
    std::vector<int> st{0, 0, 0, 0};                  // std::vector 小于 int 超过 st{0, 0, 0, 0};
    for (char role : path) {                          // for (char role : 当前路径) {
        std::vector<int> before = st;                 // 把 st; 写入 std::vector<int> before
        st[0] = 1 - st[0];                            // 把 1 减 st[0]; 写入 st[0]
        if (role != '-') {                            // 若 role 不等于 ' 减 '
            int idx = (role == 'W')   ? 1
                      : (role == 'S') ? 2
                                      : 3; // 把 (role 等于 'W') ? 1 : (role 等于 'S') ? 2 : 3 存入 idx
            if (before[0] != before[idx])
                return false;      // 若 before[0] 不等于 before[idx]，直接返回 false
            st[idx] = 1 - st[idx]; // 把 1 减 st[idx]; 写入 st[idx]
        }
        if (invalid(st))
            return false; // 若 invalid(st)，直接返回 false
    }
    return st == std::vector<int>{1, 1, 1, 1}; // 返回 st 等于 std::vector 小于 int 超过 {1, 1, 1, 1}
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<char> want_path = {'S', '-', 'W', 'S', 'V', '-', 'S'};
    std::string want_readable =
        "HS H HW HS HV H HS"; // 把 「HS H HW HS HV H HS」; 写入 std::string want_readable

    std::vector<char> got_path = solve_farmer(); // 把 solve_farmer(); 写入 std::vector<char> got_path

    // case1: 路径一致
    if (got_path != want_path) {
        std::cout << "FAIL path mismatch" << std::endl;
        return 1;
    }

    // case2: 可读方案串
    std::string got_readable; // std::string got_readable;
    for (size_t i = 0; i < got_path.size();
         ++i) {               // 让 下标 i 从 0 开始计数，下标 i 小于 got_path.大小() 就继续
        char r = got_path[i]; // 把 got_path[下标 i]; 写入 char r
        if (i)
            got_readable += " "; // 若 下标 i) got_readable 累加 「 」;
        got_readable += 'H';     // got_readable累加 'H'
        if (r != '-')
            got_readable += r; // 若 右指针 不等于 ' 减 ') got_readable 累加 右指针;
    }
    if (got_readable != want_readable) {
        std::cout << "FAIL readable: " << got_readable << std::endl;
        return 1;
    }

    // case3: 7 步
    if (got_path.size() != 7) {
        std::cout << "FAIL steps" << std::endl;
        return 1;
    }

    // case4: 模拟校验
    if (!simulate(got_path)) {
        std::cout << "FAIL simulate" << std::endl;
        return 1;
    }

    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
