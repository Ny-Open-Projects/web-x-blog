// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136726698
// LeetCode 617. 合并二叉树 — Rust 版（方案2）
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
            let (a, b) = (a.borrow(), b.borrow()); // 把 (数组.borrow(), b.borrow()); 写入 let (a, b)
            a.val == b.val
                && same_tree(a.left.as_ref(), b.left.as_ref())
                && same_tree(a.right.as_ref(), b.right.as_ref())
        }
        _ => false,
    }
}
fn merge_trees(
    t1: Option<Rc<RefCell<TreeNode>>>,
    t2: Option<Rc<RefCell<TreeNode>>>,
) -> Option<Rc<RefCell<TreeNode>>> {
    // 定义函数/方法 merge_trees
    let n1 = match t1 {
        Some(x) => x,
        None => return t2,
    };
    if let Some(n2) = t2 {
        // 若 let Some(n2) 赋值为 t2
        n1.borrow_mut().val += n2.borrow().val; // 把 n2.borrow().值; 写入 n1.borrow_mut().val +
        let (l, r) = (n2.borrow().left.clone(), n2.borrow().right.clone());
        let (l1, r1) = (n1.borrow().left.clone(), n1.borrow().right.clone());
        {
            let mut b = n1.borrow_mut();
            b.left = merge_trees(l1, l);
            b.right = merge_trees(r1, r);
        }
    }
    Some(n1) // Some(n1)
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let m = |a: &[Option<i32>], b: &[Option<i32>], w: &[Option<i32>]| {
        let got = merge_trees(build_tree(a), build_tree(b)); // 把 merge_trees(build_tree(数组), build_tree(b)) 存入 got
        let want = build_tree(w); // 把 build_tree(权重) 存入 want
        assert!(same_tree(got.as_ref(), want.as_ref())); // 断言校验
    };
    m(
        &[Some(1), Some(3), Some(2), Some(5)],
        &[Some(2), Some(1), Some(3), None, Some(4), None, Some(7)],
        &[Some(3), Some(4), Some(5), Some(5), Some(4), None, Some(7)],
    );
    m(&[], &[Some(1)], &[Some(1)]); // 映射表( 按位与 [], 按位与 [Some(1)], 按位与 [Some(1)]);
    m(&[Some(1)], &[], &[Some(1)]); // 映射表( 按位与 [Some(1)], 按位与 [], 按位与 [Some(1)]);
    m(
        &[Some(1), Some(2), Some(3)],
        &[Some(1), Some(2), Some(3)],
        &[Some(2), Some(4), Some(6)],
    );
    println!("PASS"); // 全部用例通过，输出 PASS
}
