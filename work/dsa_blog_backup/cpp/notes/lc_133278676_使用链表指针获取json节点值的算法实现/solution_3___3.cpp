// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
// LeetCode 133278676. 使用链表（指针链）获取 JSON 节点值 — C++ 版（方案B：逐键求值 / reduce 链式访问）
#include <iostream> // 引入头文件
#include <map>      // 引入头文件
#include <memory>   // 引入头文件
#include <string>   // 引入头文件

struct JNode {           // 定义类型
    bool is_obj = false; // 把 false 存入 is_obj
    int val = 0;         // 把 0 存入 值
    std::map<std::string, std::unique_ptr<JNode>> children;
};

static JNode *get_value_eval(JNode *data, const std::string &path) {
    // 合法路径直接逐键求值（"a/b/c" 形式）
    JNode *cur = data;             // 把 data; 写入 JNode *cur
    size_t start = 0;              // 把 0; 写入 size_t start
    while (start <= path.size()) { // 循环，直到不满足「起点 不超过 当前路径.大小(」
        size_t slash = path.find('/', start); // 把 当前路径 查找 ' 除以 ', 起点); 写入 size_t slash
        std::string key =
            path.substr(start, slash - start); // 把 当前路径 截取 起点, slash 减 起点); 写入 std::string key
        cur = cur->children[key].get(); // 把 当前值 减 超过 children[key] 查找 ); 写入 当前值
        if (slash == std::string::npos)
            break;         // 若 slash 等于 std::string::npos) break;
        start = slash + 1; // 把 slash 加 1; 写入 起点
    }
    return cur; // 返回 当前值
}

int main() {                               // 程序入口：跑内嵌自测用例
    auto data = std::make_unique<JNode>(); // 把 std::make_unique 小于 JNode 超过 () 存入 data
    data->is_obj = true;                   // 把 true; 写入 data->is_obj
    auto &a = data->children["a"];         // 把 data 减 超过 children[「数组」]; 写入 auto &a
    a = std::make_unique<JNode>();         // 把 std::make_unique 小于 JNode 超过 (); 写入 数组
    a->is_obj = true;                      // 把 true; 写入 a->is_obj
    auto &b = a->children["b"];            // 把 数组 减 超过 children[「b」]; 写入 auto &b
    b = std::make_unique<JNode>();         // 把 std::make_unique 小于 JNode 超过 (); 写入 b
    b->is_obj = true;                      // 把 true; 写入 b->is_obj
    auto &c = b->children["c"];            // 把 b 减 超过 children[「字符」]; 写入 auto &c
    c = std::make_unique<JNode>();         // 把 std::make_unique 小于 JNode 超过 (); 写入 字符
    c->val = 1;                            // 把 1; 写入 c->val
    auto &d = data->children["d"];         // 把 data 减 超过 children[「d」]; 写入 auto &d
    d = std::make_unique<JNode>();         // 把 std::make_unique 小于 JNode 超过 (); 写入 d
    d->is_obj = true;                      // 把 true; 写入 d->is_obj
    auto &e = d->children["e"];            // 把 d 减 超过 children[「e」]; 写入 auto &e
    e = std::make_unique<JNode>();         // 把 std::make_unique 小于 JNode 超过 (); 写入 e
    e->val = 2;                            // 把 2; 写入 e->val

    // p1: 逐键求值
    if (get_value_eval(data.get(), "a/b/c")->val != 1) {
        std::cout << "p1 failed" << std::endl;
        return 1;
    }
    // p2: reduce 链式访问（同一遍历）
    if (get_value_eval(data.get(), "d/e")->val != 2) {
        std::cout << "p2 failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
