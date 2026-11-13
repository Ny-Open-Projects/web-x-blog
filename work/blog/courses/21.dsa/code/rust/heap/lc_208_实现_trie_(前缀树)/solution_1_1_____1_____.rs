// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135533027
// LeetCode 208. 实现 Trie (前缀树) — Rust 版（方案1）
use std::collections::HashMap; // 引入依赖
struct TrieNode {
    children: HashMap<char, Box<TrieNode>>,
    is_end: bool,
} // 定义类型
impl TrieNode {
    fn new() -> Self {
        TrieNode {
            children: HashMap::new(),
            is_end: false,
        }
    }
} // 定义函数/方法 new
struct Trie {
    root: TrieNode,
} // 定义类型
impl Trie {
    // 实现块
    fn new() -> Self {
        Trie {
            root: TrieNode::new(),
        }
    } // 定义函数/方法 new
    fn insert(&mut self, word: &str) {
        // 定义函数/方法 insert
        let mut node = &mut self.root; // 把 按位与 mut self.根节点; 写入 let mut node
        for ch in word.chars() {
            // 逐个取出 单词 的元素（字符）
            node = node
                .children
                .entry(ch)
                .or_insert_with(|| Box::new(TrieNode::new()))
                .as_mut();
        }
        node.is_end = true; // 把 true; 写入 node.is_end
    }
    fn search(&self, word: &str) -> bool {
        // 定义函数/方法 search
        let mut node = &self.root; // 把 按位与 self.根节点; 写入 let mut node
        for ch in word.chars() {
            // 逐个取出 单词 的元素（字符）
            match node.children.get(&ch) {
                Some(n) => node = n,
                None => return false,
            } // 按情况匹配处理
        }
        node.is_end // 节点.is_end
    }
    fn starts_with(&self, prefix: &str) -> bool {
        // 定义函数/方法 starts_with
        let mut node = &self.root; // 把 按位与 self.根节点; 写入 let mut node
        for ch in prefix.chars() {
            // 逐个取出 prefix 的元素（字符）
            match node.children.get(&ch) {
                Some(n) => node = n,
                None => return false,
            } // 按情况匹配处理
        }
        true // true
    }
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut t = Trie::new(); // 把 Trie::new(); 写入 let mut t
    t.insert("apple"); // 另一字符串 插入 「apple」);
    assert!(t.search("apple")); // 断言校验
    assert!(!t.search("app")); // 断言校验
    assert!(t.starts_with("app")); // 断言校验
    assert!(!t.search("appl")); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
