// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137040405
// LeetCode 701. 二叉搜索树中的插入操作 — Rust 版（方案1）
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
fn levels_flat(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
    // 定义函数/方法 levels_flat
    let mut out = Vec::new(); // 把 Vec::new(); 写入 let mut out
    let mut q: Vec<Rc<RefCell<TreeNode>>> = root.into_iter().collect();
    while !q.is_empty() {
        // while 取反 节点 是否为空 {
        let mut nxt = Vec::new(); // 把 Vec::new(); 写入 let mut nxt
        for n in q {
            let b = n.borrow();
            out.push(b.val);
            if let Some(c) = b.left.clone() {
                nxt.push(c);
            }
            if let Some(c) = b.right.clone() {
                nxt.push(c);
            }
        } // 逐个取出 节点 的元素（元素个数）
        q = nxt; // 把 nxt; 写入 节点
    }
    out // out
}

fn insert_into_bst(root: Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<Rc<RefCell<TreeNode>>> {
    // 定义函数/方法 insert_into_bst
    match root {
        // 按情况匹配处理
        None => Some(TreeNode::new(val)),
        Some(node) => {
            let mut pos = node.clone(); // 把 节点.clone(); 写入 let mut pos
            loop {
                // loop {
                let (go_left, child) = {
                    // 把 { 写入 let (go_left, child)
                    let pb = pos.borrow(); // 把 pos.borrow() 存入 pb
                    if val < pb.val {
                        (true, pb.left.clone())
                    } else {
                        (false, pb.right.clone())
                    }
                };
                match child {
                    // 按情况匹配处理
                    Some(c) => pos = c,
                    None => {
                        let mut pm = pos.borrow_mut(); // 把 pos.borrow_mut(); 写入 let mut pm
                        if go_left {
                            pm.left = Some(TreeNode::new(val));
                        } else {
                            pm.right = Some(TreeNode::new(val));
                        }
                        break; // 跳出循环
                    }
                }
            }
            Some(node) // Some(节点)
        }
    }
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let t = build_tree(&[Some(4), Some(2), Some(7), Some(1), Some(3)]);
    let got = levels_flat(insert_into_bst(t, 5)); // 把 levels_flat(insert_into_bst(另一字符串, 5)) 存入 got
    assert_eq!(got, vec![4, 2, 7, 1, 3, 5]); // 断言校验
    let got2 = insert_into_bst(None, 5); // 把 insert_into_bst(None, 5) 存入 got2
    assert_eq!(levels_flat(got2), vec![5]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
