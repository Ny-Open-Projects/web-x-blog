// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135666411
// LeetCode 257. 二叉树的所有路径 — Rust 版（方案1）
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

fn binary_tree_paths(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<String> {
    // 定义函数/方法 binary_tree_paths
    let mut paths = Vec::new(); // 把 Vec::new(); 写入 let mut paths
    fn dfs(n: Option<&Rc<RefCell<TreeNode>>>, path: String, paths: &mut Vec<String>) {
        // 定义函数/方法 dfs
        let node = match n {
            Some(x) => x,
            None => return,
        };
        let nb = node.borrow(); // 把 节点.borrow() 存入 nb
        let path = format!("{}{}", path, nb.val); // 把 format取反 (「{}{}」, 当前路径, nb.值) 存入 当前路径
        if nb.left.is_none() && nb.right.is_none() {
            // 若 nb.左边界.is_none() 且 nb.右边界.is_none(
            paths.push(path); // 把 当前路径 压入栈/数组尾部
        } else {
            // 否则
            let p2 = format!("{}->", path); // 把 format取反 (「{} 减 超过 」, 当前路径) 存入 p2
            dfs(nb.left.as_ref(), p2.clone(), paths); // dfs(nb.左边界.as_ref(), p2.clone(), paths);
            dfs(nb.right.as_ref(), p2, paths); // dfs(nb.右边界.as_ref(), p2, paths);
        }
    }
    dfs(root.as_ref(), String::new(), &mut paths); // dfs(根节点.as_ref(), String::new(), 按位与 mut paths);
    paths // paths
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        binary_tree_paths(build_tree(&[Some(1), Some(2), Some(3)])),
        vec!["1->2", "1->3"]
    ); // 断言校验
    assert_eq!(binary_tree_paths(build_tree(&[Some(1)])), vec!["1"]); // 断言校验
    assert!(binary_tree_paths(None).is_empty()); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
