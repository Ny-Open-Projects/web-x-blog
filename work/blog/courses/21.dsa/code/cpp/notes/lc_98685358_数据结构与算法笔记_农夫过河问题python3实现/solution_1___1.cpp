// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/98685358
// LeetCode 98685358. 农夫过河问题 — C++ 版（农夫过河问题：BFS 求最短过河序列，状态 (农夫,狼,羊,菜)，0=左岸
// 1=右岸）
#include <iostream> // 引入头文件
#include <map>      // 引入头文件
#include <vector>   // 引入头文件

static bool is_safe(const std::vector<int> &s) { // 定义判定函数 is_safe
    if (s[1] == s[2] && s[0] != s[1])
        return false; // 若 字符串[1] 等于 字符串[2] 且 字符串[0] 不等于 字符串[1]，直接返回 false
    if (s[2] == s[3] && s[0] != s[2])
        return false; // 若 字符串[2] 等于 字符串[3] 且 字符串[0] 不等于 字符串[2]，直接返回 false
    return true; // 返回 true
}

static std::string key(const std::vector<int> &s) {
    std::string k;                          // std::string 下标 k;
    for (size_t i = 0; i < s.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 字符串.大小() 就继续
        if (i)
            k += ",";              // 若 下标 i) 下标 k 累加 「,」;
        k += std::to_string(s[i]); // 下标 k累加 std::to_string(字符串[下标 i])
    }
    return k; // 返回 下标 k
}

static std::vector<std::vector<int>>
solve() { // static std::vector 小于 std::vector 小于 int 超过 超过 solve() {
    std::vector<int> start{0, 0, 0, 0}; // std::vector 小于 int 超过 起点{0, 0, 0, 0};
    std::vector<int> goal{1, 1, 1, 1};  // std::vector 小于 int 超过 goal{1, 1, 1, 1};
    // prev: key -> (是否有父状态, 父key)
    std::map<std::string, std::pair<bool, std::string>> prev;
    prev[key(start)] = {false, ""}; // 把 {false, 「」}; 写入 prev[key(start)]
    std::map<std::string, std::vector<int>>
        state_by; // std::映射表 小于 std::string, std::vector 小于 int 超过 超过 state_by;
    state_by[key(start)] = start;           // 把 起点; 写入 state_by[key(start)]
    std::vector<std::vector<int>> q{start}; // std::vector 小于 std::vector 小于 int 超过 超过 节点{起点};
    size_t head = 0;                        // 把 0; 写入 size_t head
    while (head < q.size()) {               // 循环，直到不满足「头节点 小于 节点.大小(」
        std::vector<int> cur = q[head++]; // 把 节点[头节点 加一 ]; 写入 std::vector<int> cur
        std::string ck = key(cur);        // 把 key(当前值); 写入 std::string ck
        if (cur == goal) {                // 若 当前值 等于 goal
            std::vector<std::vector<int>> path; // std::vector 小于 std::vector 小于 int 超过 超过 当前路径;
            std::string k = ck;                 // 把 ck; 写入 std::string k
            while (true) {                      // 循环，直到不满足「true」
                path.push_back(state_by.at(k)); // 当前路径 追加 state_by.at(下标 k));
                if (!prev.at(k).first)
                    break;             // 若 取反 前一个.at(下标 k).first) break;
                k = prev.at(k).second; // 把 前一个.at(下标 k).second; 写入 下标 k
            }
            std::reverse(path.begin(), path.end()); // std::reverse(当前路径 迭代位置 , 当前路径.终点());
            return path;                            // 返回 当前路径
        }
        int farmer = cur[0];          // 把 当前值[0] 存入 farmer
        for (int i = 0; i < 4; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
            if (i != 0 && cur[i] != farmer)
                continue; // 若 下标 i 不等于 0 且 当前值[下标 i] 不等于 farmer) continue;
            std::vector<int> nxt = cur; // 把 当前值; 写入 std::vector<int> nxt
            nxt[0] = 1 - farmer;        // 把 1 减 farmer; 写入 nxt[0]
            if (i != 0)
                nxt[i] = 1 - farmer;   // 若 下标 i 不等于 0) nxt[下标 i] 赋值为 1 减 farmer;
            std::string nk = key(nxt); // 把 key(nxt); 写入 std::string nk
            if (prev.count(nk))
                continue; // 若 前一个.计数(nk)) continue;
            if (!is_safe(nxt))
                continue;          // 若 取反 is_safe(nxt)) continue;
            prev[nk] = {true, ck}; // 把 {true, ck}; 写入 prev[nk]
            state_by[nk] = nxt;    // 把 nxt; 写入 state_by[nk]
            q.push_back(nxt);      // 节点 追加 nxt);
        }
    }
    return {}; // 返回 {}
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::vector<int>> want = {
        // 把 { 写入 std::vector<std::vector<int>> want
        {0, 0, 0, 0}, {1, 0, 1, 0}, {0, 0, 1, 0}, {1, 1, 1, 0},
        {0, 1, 0, 0}, {1, 1, 0, 1}, {0, 1, 0, 1}, {1, 1, 1, 1},
    };
    std::vector<std::vector<int>> path = solve(); // 把 solve(); 写入 std::vector<std::vector<int>> path
    if (path.empty()) {
        std::cout << "FAILED: 无解" << std::endl;
        return 1;
    }
    if (path != want) {
        std::cout << "FAILED: path mismatch" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
