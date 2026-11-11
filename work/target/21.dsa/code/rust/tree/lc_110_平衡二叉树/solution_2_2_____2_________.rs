// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135170465
// LeetCode 110. 平衡二叉树 — Rust 版（方案2）
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

fn height(n: Option<&Rc<RefCell<TreeNode>>>) -> i32 {
    // 定义函数/方法 height
    let node = match n {
        Some(x) => x,
        None => return 0,
    };
    let nb = node.borrow(); // 把 节点.borrow() 存入 nb
    1 + height(nb.left.as_ref()).max(height(nb.right.as_ref())) // 1 加 height(nb.左边界.as_ref()).取较大值 height(nb.右边界.as_ref()))
}
fn is_balanced(root: Option<&Rc<RefCell<TreeNode>>>) -> bool {
    // 定义判定函数 is_balanced
    let node = match root {
        Some(x) => x,
        None => return true,
    };
    let nb = node.borrow(); // 把 节点.borrow() 存入 nb
    (height(nb.left.as_ref()) - height(nb.right.as_ref())).abs() <= 1
        && is_balanced(nb.left.as_ref())  // 且 is_balanced(nb.左边界.as_ref())
        && is_balanced(nb.right.as_ref()) // 且 is_balanced(nb.右边界.as_ref())
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let t1 = build_tree(&[Some(3), Some(9), Some(20), None, None, Some(15), Some(7)]);
    let t2 = build_tree(&[
        Some(1),
        Some(2),
        Some(2),
        Some(3),
        Some(3),
        None,
        None,
        Some(4),
        Some(4),
    ]);
    assert!(is_balanced(t1.as_ref())); // 断言校验
    assert!(!is_balanced(t2.as_ref())); // 断言校验
    assert!(is_balanced(None)); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
