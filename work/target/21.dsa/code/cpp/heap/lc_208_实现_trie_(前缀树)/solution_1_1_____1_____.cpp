// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135533027
// LeetCode 208. 实现 Trie (前缀树) — C++ 版（方案1）
#include <cassert>       // 引入头文件
#include <iostream>      // 引入头文件
#include <memory>        // 引入头文件
#include <unordered_map> // 引入头文件
struct TrieNode {        // 定义类型
    std::unordered_map<char, std::unique_ptr<TrieNode>> children;
    bool isEnd = false; // 把 false 存入 isEnd
};
struct Trie { // 定义类型
    std::unique_ptr<TrieNode> root = std::make_unique<TrieNode>();
    void insert(const std::string &word) {    // 定义函数/方法 insert
        TrieNode *node = root.get();          // 把 根节点 查找 ); 写入 TrieNode *node
        for (char ch : word) {                // for (char 字符 : 单词) {
            auto &child = node->children[ch]; // 把 节点 减 超过 children[字符]; 写入 auto &child
            if (!child)
                child = std::make_unique<TrieNode>(); // 若 取反 子节点) 子节点 赋值为 std::make_unique 小于
                                                      // TrieNode 超过 ();
            node = child.get(); // 把 子节点 查找 ); 写入 节点
        }
        node->isEnd = true; // 把 true; 写入 node->isEnd
    }
    bool search(const std::string &word) const { // bool search(const std::string 按位与 单词) const {
        const TrieNode *node = root.get();       // 把 根节点 查找 ); 写入 const TrieNode *node
        for (char ch : word) {                   // for (char 字符 : 单词) {
            auto it = node->children.find(ch);   // 把 节点 减 超过 children 查找 字符) 存入 it
            if (it == node->children.end())
                return false;        // 若 it 等于 节点 减 超过 children.终点()，直接返回 false
            node = it->second.get(); // 把 it 减 超过 second 查找 ); 写入 节点
        }
        return node->isEnd; // 返回 节点 减 超过 isEnd
    }
    bool
    startsWith(const std::string &prefix) const { // bool startsWith(const std::string 按位与 prefix) const {
        const TrieNode *node = root.get();        // 把 根节点 查找 ); 写入 const TrieNode *node
        for (char ch : prefix) {                  // for (char 字符 : prefix) {
            auto it = node->children.find(ch);    // 把 节点 减 超过 children 查找 字符) 存入 it
            if (it == node->children.end())
                return false;        // 若 it 等于 节点 减 超过 children.终点()，直接返回 false
            node = it->second.get(); // 把 it 减 超过 second 查找 ); 写入 节点
        }
        return true; // 返回 true
    }
};
int main() {                          // 程序入口：跑内嵌自测用例
    Trie t;                           // Trie 另一字符串;
    t.insert("apple");                // 另一字符串 插入 「apple」);
    assert(t.search("apple"));        // 断言校验
    assert(!t.search("app"));         // 断言校验
    assert(t.startsWith("app"));      // 断言校验
    assert(!t.search("appl"));        // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
