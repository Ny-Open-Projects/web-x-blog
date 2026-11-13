// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135314196
// LeetCode 98. 验证二叉搜索树 — Rust 版（方案3）
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

fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
    // 定义判定函数 is_valid_bst
    let root = match root {
        Some(x) => x,
        None => return true,
    };
    let mut stack: Vec<(Rc<RefCell<TreeNode>>, Option<i64>, Option<i64>)> =
        vec![(root, None, None)];
    while let Some((node, low, high)) = stack.pop() {
        // 边取边处理，取空即停
        let nb = node.borrow(); // 把 节点.borrow() 存入 nb
        let v = nb.val as i64; // 把 nb.值 as i64 存入 值
        if let Some(l) = low {
            // 若 let Some(左指针) 赋值为 low
            if v <= l {
                return false;
            } // 若 值 不超过 左指针 { return false; }
        }
        if let Some(h) = high {
            // 若 let Some(h) 赋值为 high
            if v >= h {
                return false;
            } // 若 值 不低于 h { return false; }
        }
        if let Some(r) = nb.right.clone() {
            stack.push((r, Some(v), high));
        }
        if let Some(l) = nb.left.clone() {
            stack.push((l, low, Some(v)));
        }
    }
    true // true
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(is_valid_bst(build_tree(&[Some(2), Some(1), Some(3)]))); // 断言校验
    assert!(!is_valid_bst(build_tree(&[
        Some(5),
        Some(1),
        Some(4),
        None,
        None,
        Some(3),
        Some(6)
    ]))); // 断言校验
    assert!(is_valid_bst(None)); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
