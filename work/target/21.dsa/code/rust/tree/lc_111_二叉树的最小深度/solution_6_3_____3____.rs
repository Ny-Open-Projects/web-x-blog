// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135759583
// LeetCode 111. 二叉树的最小深度 — Rust 版（方案6）
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

fn min_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
    // 定义函数/方法 min_depth
    let root = match root {
        Some(x) => x,
        None => return 0,
    };
    let mut q: Vec<(Rc<RefCell<TreeNode>>, i32)> = vec![(root, 1)];
    let mut head = 0; // 把 0; 写入 let mut head
    while head < q.len() {
        // while 头节点 小于 节点.长度() {
        let (node, l) = q[head].clone(); // 把 节点[头节点].clone(); 写入 let (node, l)
        head += 1; // 头节点累加 1
        let nb = node.borrow(); // 把 节点.borrow() 存入 nb
        if nb.left.is_none() && nb.right.is_none() {
            // 若 nb.左边界.is_none() 且 nb.右边界.is_none(
            return l; // 返回 左指针
        }
        if let Some(c) = nb.left.clone() {
            q.push((c, l + 1));
        } // 若 let Some(字符) 赋值为 nb.左边界.clone() { 节点 追加 (字符, 左指针 加 1)); }
        if let Some(c) = nb.right.clone() {
            q.push((c, l + 1));
        } // 若 let Some(字符) 赋值为 nb.右边界.clone() { 节点 追加 (字符, 左指针 加 1)); }
    }
    0
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        min_depth(build_tree(&[
            Some(3),
            Some(9),
            Some(20),
            None,
            None,
            Some(15),
            Some(7)
        ])),
        2
    ); // 断言校验
    assert_eq!(
        min_depth(build_tree(&[
            Some(2),
            None,
            Some(3),
            None,
            Some(4),
            None,
            Some(5),
            None,
            Some(6)
        ])),
        5
    ); // 断言校验
    assert_eq!(min_depth(None), 0); // 断言校验
    assert_eq!(min_depth(build_tree(&[Some(1)])), 1); // 断言校验
    assert_eq!(min_depth(build_tree(&[Some(1), Some(2)])), 2); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
