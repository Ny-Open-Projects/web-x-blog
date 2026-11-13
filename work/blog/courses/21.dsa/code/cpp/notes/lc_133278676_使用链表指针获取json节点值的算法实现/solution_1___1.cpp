// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
// LeetCode 133278676. 使用链表（指针链）获取 JSON 节点值 — C++ 版（方案A：安全遍历，缺失返回 nullptr）
#include <iostream> // 引入头文件
#include <map>      // 引入头文件
#include <memory>   // 引入头文件
#include <string>   // 引入头文件
#include <vector>   // 引入头文件

struct JNode {           // 定义类型
    bool is_obj = false; // 把 false 存入 is_obj
    int val = 0;         // 把 0 存入 值
    std::map<std::string, std::unique_ptr<JNode>> children;

    JNode *child(const std::string &key) const { // JNode 乘 子节点(const std::string 按位与 key) const {
        auto it = children.find(key);            // 把 children 查找 key) 存入 it
        return it == children.end()
                   ? nullptr
                   : it->second.get(); // 返回 it 等于 children.终点() ? nullptr : it 减 超过 second 查找 )
    }
};

static JNode *get_value(JNode *data, const std::vector<std::string> &path) {
    JNode *node = data;            // 把 data; 写入 JNode *node
    for (const auto &key : path) { // 逐个取出 当前路径 的元素（key）
        if (!node->is_obj)
            return nullptr;      // 若 取反 节点 减 超过 is_obj，直接返回 nullptr
        node = node->child(key); // 把 节点 减 超过 子节点(key); 写入 节点
        if (!node)
            return nullptr; // 若 取反 节点，直接返回 nullptr
    }
    return node; // 返回 节点
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

    if (auto *r = get_value(
            data.get(),
            {"a", "b",
             "c"})) { // 若 auto 乘 右指针 赋值为 get_value(data 查找 ), {「数组」, 「数组」, 「数组」}
        if (r->val != 1) {
            std::cout << "p1 failed" << std::endl;
            return 1;
        }
    } else {                                   // 否则
        std::cout << "p1 failed" << std::endl; // 打印输出
        return 1;                              // 返回 1
    }
    if (get_value(data.get(), {"a", "z"}) != nullptr) {
        std::cout << "p2 failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
