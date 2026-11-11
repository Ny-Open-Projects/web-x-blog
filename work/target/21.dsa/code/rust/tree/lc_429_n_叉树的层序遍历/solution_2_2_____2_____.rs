// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137532387
// LeetCode 429. N叉树的层序遍历 — Rust 版（方案2）
use std::cell::RefCell;
use std::rc::Rc; // 引入依赖 // 引入依赖

#[derive(Debug)]
struct TreeNode {
    // 定义类型
    val: i32,
    left: Option<Rc<RefCell<TreeNode>>>,
    right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    // 实现块
    fn new(val: i32) -> Rc<RefCell<TreeNode>> {
        // 定义函数/方法 new
        Rc::new(RefCell::new(TreeNode {
            val,
            left: None,
            right: None,
        })) // Rc::new(RefCell::new(TreeNode { 值, 左边界: None, 右边界: None }))
    }
}

fn build_tree(vals: &[Option<i32>]) -> Option<Rc<RefCell<TreeNode>>> {
    // 定义函数/方法 build_tree
    if vals.is_empty() || vals[0].is_none() {
        // 若 vals 是否为空 或 vals[0].is_none(
        return None; // 返回 None
    }
    let root = TreeNode::new(vals[0].unwrap()); // 把 TreeNode::new(vals[0].unwrap()) 存入 根节点
    let mut queue: Vec<Rc<RefCell<TreeNode>>> = vec![root.clone()];
    let mut i = 1; // 把 1; 写入 let mut i
    while !queue.is_empty() && i < vals.len() {
        // while 取反 队列 是否为空 且 下标 i 小于 vals.长度() {
        let node = queue.remove(0); // 把 队列 弹出 0) 存入 节点
        if i < vals.len() {
            // 若 下标 i 小于 vals.长度(
            if let Some(v) = vals[i] {
                // 若 let Some(值) 赋值为 vals[下标 i]
                let child = TreeNode::new(v); // 把 TreeNode::new(值) 存入 子节点
                node.borrow_mut().left = Some(child.clone()); // 把 Some(子节点.clone()); 写入 左边界
                queue.push(child); // 把 子节点 压入栈/数组尾部
            }
            i += 1; // 下标 i累加 1
        }
        if i < vals.len() {
            // 若 下标 i 小于 vals.长度(
            if let Some(v) = vals[i] {
                // 若 let Some(值) 赋值为 vals[下标 i]
                let child = TreeNode::new(v); // 把 TreeNode::new(值) 存入 子节点
                node.borrow_mut().right = Some(child.clone()); // 把 Some(子节点.clone()); 写入 右边界
                queue.push(child); // 把 子节点 压入栈/数组尾部
            }
            i += 1; // 下标 i累加 1
        }
    }
    Some(root) // Some(根节点)
}

struct Node {
    val: i32,
    children: Vec<Node>,
} // 定义类型
impl Node {
    fn new(v: i32) -> Node {
        Node {
            val: v,
            children: Vec::new(),
        }
    }
} // 定义函数/方法 new
fn level_order(root: Option<&Node>) -> Vec<Vec<i32>> {
    // 定义函数/方法 level_order
    let mut res = Vec::new(); // 把 Vec::new(); 写入 let mut res
    let root = match root {
        Some(x) => x,
        None => return res,
    };
    let mut q: Vec<&Node> = vec![root]; // 把 vec取反 [根节点]; 写入 let mut q: Vec<&Node>
    while !q.is_empty() {
        // while 取反 节点 是否为空 {
        let mut level = Vec::new(); // 把 Vec::new(); 写入 let mut level
        let mut nxt = Vec::new(); // 把 Vec::new(); 写入 let mut nxt
        for n in q {
            // 逐个取出 节点 的元素（元素个数）
            level.push(n.val); // 把 元素个数.值 压入栈/数组尾部
            for c in &n.children {
                nxt.push(c);
            } // 逐个取出 元素个数 的元素（字符）
        }
        res.push(level); // 把 level 压入栈/数组尾部
        q = nxt; // 把 nxt; 写入 节点
    }
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut root = Node::new(1); // 把 Node::new(1); 写入 let mut root
    let mut c3 = Node::new(3); // 把 Node::new(3); 写入 let mut c3
    c3.children = vec![Node::new(5), Node::new(6)]; // 把 vec取反 [Node::new(5), Node::new(6)]; 写入 c3.children
    root.children = vec![c3, Node::new(2), Node::new(4)]; // 把 vec取反 [c3, Node::new(2), Node::new(4)]; 写入 root.children
    assert_eq!(
        level_order(Some(&root)),
        vec![vec![1], vec![3, 2, 4], vec![5, 6]]
    ); // 断言校验
    assert!(level_order(None).is_empty()); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
