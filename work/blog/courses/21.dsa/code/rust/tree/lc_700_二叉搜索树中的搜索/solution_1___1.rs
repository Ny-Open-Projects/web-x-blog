// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135005838
// LeetCode 700. 二叉搜索树中的搜索 — Rust 版（方案1）
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

fn search_bst(root: Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<i32> {
    // 定义函数/方法 search_bst
    let mut cur = root; // 把 根节点; 写入 let mut cur
    while let Some(node) = cur {
        // 边取边处理，取空即停
        let n = node.borrow(); // 把 节点.borrow() 存入 元素个数
        if n.val == val {
            return Some(n.val);
        } // 若 元素个数.值 等于 值 { return Some(元素个数.值); }
        cur = if n.val > val {
            n.left.clone()
        } else {
            n.right.clone()
        };
    }
    None // None
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let t = build_tree(&[Some(4), Some(2), Some(7), Some(1), Some(3)]);
    assert_eq!(search_bst(t.clone(), 2), Some(2)); // 断言校验
    assert_eq!(search_bst(t.clone(), 5), None); // 断言校验
    assert_eq!(search_bst(t.clone(), 4), Some(4)); // 断言校验
    assert_eq!(search_bst(None, 1), None); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
