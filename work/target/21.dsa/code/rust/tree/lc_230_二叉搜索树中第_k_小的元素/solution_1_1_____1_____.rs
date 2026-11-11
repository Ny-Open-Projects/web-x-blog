// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136684493
// LeetCode 230. 二叉搜索树中第K小的元素 — Rust 版（方案1）
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

fn kth_smallest(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {
    // 定义函数/方法 kth_smallest
    let mut k = k; // 把 下标 k; 写入 let mut k
    let mut stack: Vec<Rc<RefCell<TreeNode>>> = Vec::new(); // 把 Vec::new(); 写入 let mut stack: Vec<Rc<RefCell<TreeNode>>>
    let mut cur = root; // 把 根节点; 写入 let mut cur
    while cur.is_some() || !stack.is_empty() {
        // while 当前值.is_some() 或 取反 栈 是否为空 {
        while let Some(c) = cur {
            // 边取边处理，取空即停
            stack.push(c.clone()); // 把 字符.clone( 压入栈/数组尾部
            cur = c.borrow().left.clone(); // 把 字符.borrow().左边界.clone(); 写入 当前值
        }
        let node = stack.pop().unwrap(); // 把 栈 弹出 ).unwrap() 存入 节点
        k -= 1; // 下标 k累减 1
        if k == 0 {
            return node.borrow().val;
        } // 若 下标 k 等于 0 { return 节点.borrow().值; }
        cur = node.borrow().right.clone(); // 把 节点.borrow().右边界.clone(); 写入 当前值
    }
    -1 // 减 1
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let t = build_tree(&[Some(3), Some(1), Some(4), None, Some(2)]);
    assert_eq!(kth_smallest(t.clone(), 1), 1); // 断言校验
    assert_eq!(kth_smallest(t, 2), 2); // 断言校验
    let t2 = build_tree(&[
        Some(5),
        Some(3),
        Some(6),
        Some(2),
        Some(4),
        None,
        None,
        Some(1),
    ]);
    assert_eq!(kth_smallest(t2, 3), 3); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
