// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137409838
// LeetCode 572. 另一棵树的子树 — Rust 版（方案3）
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
fn same_tree(p: Option<&Rc<RefCell<TreeNode>>>, q: Option<&Rc<RefCell<TreeNode>>>) -> bool {
    // 定义函数/方法 same_tree
    match (p, q) {
        // 按情况匹配处理
        (None, None) => true,
        (Some(a), Some(b)) => {
            let (a, b) = (a.borrow(), b.borrow());
            a.val == b.val
                && same_tree(a.left.as_ref(), b.left.as_ref())
                && same_tree(a.right.as_ref(), b.right.as_ref())
        }
        _ => false,
    }
}

fn is_subtree(root: Option<Rc<RefCell<TreeNode>>>, sub: Option<Rc<RefCell<TreeNode>>>) -> bool {
    // 定义判定函数 is_subtree
    fn check(a: Option<&Rc<RefCell<TreeNode>>>, b: Option<&Rc<RefCell<TreeNode>>>) -> bool {
        // 定义判定函数 check
        match (a, b) {
            // 按情况匹配处理
            (None, None) => true,
            (Some(x), Some(y)) => {
                let (x, y) = (x.borrow(), y.borrow()); // 把 (x.borrow(), y.borrow()); 写入 let (x, y)
                x.val == y.val
                    && check(x.left.as_ref(), y.left.as_ref())
                    && check(x.right.as_ref(), y.right.as_ref())
            }
            _ => false,
        }
    }
    fn go(n: Option<&Rc<RefCell<TreeNode>>>, s: Option<&Rc<RefCell<TreeNode>>>) -> bool {
        // 定义函数/方法 go
        match n {
            // 按情况匹配处理
            None => false,
            Some(x) => {
                check(Some(x), s)
                    || go(x.borrow().left.as_ref(), s)
                    || go(x.borrow().right.as_ref(), s)
            }
        }
    }
    go(root.as_ref(), sub.as_ref()) // go(根节点.as_ref(), sub.as_ref())
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(is_subtree(
        build_tree(&[Some(3), Some(4), Some(5), Some(1), Some(2)]),
        build_tree(&[Some(4), Some(1), Some(2)])
    )); // 断言校验
    assert!(!is_subtree(
        build_tree(&[
            Some(3),
            Some(4),
            Some(5),
            Some(1),
            Some(2),
            None,
            None,
            None,
            None,
            Some(0)
        ]),
        build_tree(&[Some(4), Some(1), Some(2)])
    )); // 断言校验
    assert!(!is_subtree(None, None)); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
