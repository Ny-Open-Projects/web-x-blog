// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144993168
// LeetCode 108. 将有序数组转换为二叉搜索树 — Rust 版（方案1）
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

fn helper(nums: &[i32], left: usize, right: isize) -> Option<Rc<RefCell<TreeNode>>> {
    // 定义函数/方法 helper
    if left as isize > right {
        return None;
    } // 若 左边界 as isize 超过 右边界 { return None; }
    let mid = (left as isize + (right - left as isize) / 2) as usize; // 把 (左边界 as isize 加 (右边界 减 左边界 as isize) 除以 2) as usize 存入 中点
    let root = TreeNode::new(nums[mid]); // 把 TreeNode::new(数组[中点]) 存入 根节点
    root.borrow_mut().left = helper(nums, left, mid as isize - 1); // 把 helper(数组, 左边界, 中点 as isize 减 1); 写入 左边界
    root.borrow_mut().right = helper(nums, mid + 1, right); // 把 helper(数组, 中点 加 1, 右边界); 写入 右边界
    Some(root) // Some(根节点)
}
fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
    // 定义函数/方法 sorted_array_to_bst
    if nums.is_empty() {
        return None;
    } // 若 数组 是否为空 { return None; }
    helper(&nums, 0, nums.len() as isize - 1) // helper( 按位与 数组, 0, 数组.长度() as isize 减 1)
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let got = sorted_array_to_bst(vec![-10, -3, 0, 5, 9]); // 把 sorted_array_to_bst(vec取反 [ 减 10, 减 3, 0, 5, 9]) 存入 got
    let want = build_tree(&[Some(0), Some(-10), Some(5), None, Some(-3), None, Some(9)]);
    assert!(same_tree(got.as_ref(), want.as_ref())); // 断言校验
    assert!(same_tree(
        sorted_array_to_bst(vec![1]).as_ref(),
        build_tree(&[Some(1)]).as_ref()
    )); // 断言校验
    assert!(sorted_array_to_bst(vec![]).is_none()); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
