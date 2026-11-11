// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135911085
// LeetCode 654. 最大二叉树 — Rust 版（方案2）
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

fn construct_maximum_binary_tree(nums: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
    // 定义函数/方法 construct_maximum_binary_tree
    if nums.is_empty() {
        return None;
    } // 若 数组 是否为空 { return None; }
    let mut idx = 0; // 把 0; 写入 let mut idx
    for i in 0..nums.len() {
        // 逐个取出 0 的元素（下标 i）
        if nums[i] > nums[idx] {
            idx = i;
        } // 若 数组[下标 i] 超过 数组[idx] { idx 赋值为 下标 i; }
    }
    let root = TreeNode::new(nums[idx]); // 把 TreeNode::new(数组[idx]) 存入 根节点
    root.borrow_mut().left = construct_maximum_binary_tree(&nums[..idx]); // 把 construct_maximum_binary_tree( 按位与 数组[..idx]); 写入 左边界
    root.borrow_mut().right = construct_maximum_binary_tree(&nums[idx + 1..]); // 把 construct_maximum_binary_tree( 按位与 数组[idx 加 1..]); 写入 右边界
    Some(root) // Some(根节点)
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let t = construct_maximum_binary_tree(&[3, 2, 1, 6, 0, 5]);
    assert_eq!(t.as_ref().unwrap().borrow().val, 6); // 断言校验
    assert_eq!(construct_maximum_binary_tree(&[1]).unwrap().borrow().val, 1); // 断言校验
    assert_eq!(
        construct_maximum_binary_tree(&[3, 2, 1])
            .unwrap()
            .borrow()
            .val,
        3
    ); // 断言校验
    assert!(construct_maximum_binary_tree(&[]).is_none()); // 断言校验
                                                           // 完整结构验证：LC 官方 [3,2,1,6,0,5] → 根6, 左[3,2,1]构造, 右[0,5]构造
    let want = build_tree(&[
        Some(6),
        Some(3),
        Some(5),
        None,
        Some(2),
        Some(0),
        None,
        None,
        Some(1),
        None,
        None,
    ]);
    assert!(same_tree(t.as_ref(), want.as_ref())); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
