// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134541657
// LeetCode 226. 翻转二叉树 — Rust 版（方案5）
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

fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
    // 定义函数/方法 invert_tree
    let root = root?; // 把 根节点? 存入 根节点
    let mut stack = vec![root.clone()]; // 把 vec取反 [根节点.clone()]; 写入 let mut stack
    while let Some(node) = stack.pop() {
        // 边取边处理，取空即停
        let mut n = node.borrow_mut(); // 把 节点.borrow_mut(); 写入 let mut n
        let tmp = n.left.take(); // 把 元素个数.左边界.take() 存入 临时变量
        n.left = n.right.take(); // 把 元素个数.右边界.take(); 写入 左边界
        n.right = tmp; // 把 临时变量; 写入 右边界
        let (l, r) = (n.left.clone(), n.right.clone()); // 把 (元素个数.左边界.clone(), 元素个数.右边界.clone()); 写入 let (l, r)
        drop(n); // drop(元素个数);
        if let Some(c) = l {
            stack.push(c);
        } // 若 let Some(字符) 赋值为 左指针 { 栈 追加 字符); }
        if let Some(c) = r {
            stack.push(c);
        } // 若 let Some(字符) 赋值为 右指针 { 栈 追加 字符); }
    }
    Some(root) // Some(根节点)
}
fn levels(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
    // 定义函数/方法 levels
    let mut res = Vec::new(); // 把 Vec::new(); 写入 let mut res
    let mut q: Vec<Rc<RefCell<TreeNode>>> = root.into_iter().collect();
    while !q.is_empty() {
        // while 取反 节点 是否为空 {
        let mut cur = Vec::new(); // 把 Vec::new(); 写入 let mut cur
        let mut nxt = Vec::new(); // 把 Vec::new(); 写入 let mut nxt
        for n in q {
            // 逐个取出 节点 的元素（元素个数）
            let nb = n.borrow(); // 把 元素个数.borrow() 存入 nb
            cur.push(nb.val); // 把 nb.值 压入栈/数组尾部
            if let Some(c) = nb.left.clone() {
                nxt.push(c);
            } // 若 let Some(字符) 赋值为 nb.左边界.clone() { nxt 追加 字符); }
            if let Some(c) = nb.right.clone() {
                nxt.push(c);
            } // 若 let Some(字符) 赋值为 nb.右边界.clone() { nxt 追加 字符); }
        }
        res.push(cur); // 把 当前值 压入栈/数组尾部
        q = nxt; // 把 nxt; 写入 节点
    }
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let t = build_tree(&[
        Some(4),
        Some(2),
        Some(7),
        Some(1),
        Some(3),
        Some(6),
        Some(9),
    ]);
    let got = levels(invert_tree(t)); // 把 levels(invert_tree(另一字符串)) 存入 got
    assert_eq!(got, vec![vec![4], vec![7, 2], vec![9, 6, 3, 1]]); // 断言校验
    assert_eq!(levels(invert_tree(None)), Vec::<Vec<i32>>::new()); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
