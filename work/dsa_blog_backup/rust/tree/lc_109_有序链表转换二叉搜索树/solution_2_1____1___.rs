// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135270549
// LeetCode 109. 有序链表转换二叉搜索树 — Rust 版（方案2）
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

#[derive(Debug)]
struct ListNode {
    val: i32,
    next: Option<Box<ListNode>>,
} // 定义类型
fn build_list(vals: &[i32]) -> Option<Box<ListNode>> {
    // 定义函数/方法 build_list
    let mut head: Option<Box<ListNode>> = None; // 把 None; 写入 let mut head: Option<Box<ListNode>>
    for &v in vals.iter().rev() {
        // for 按位与 值 in vals.iter().rev() {
        let mut n = Box::new(ListNode { val: v, next: None }); // 把 Box::new(ListNode { 值: 值, 下一个: None }); 写入 let mut n
        n.next = head; // 把 头节点; 写入 下一个
        head = Some(n); // 把 Some(元素个数); 写入 头节点
    }
    head // 头节点
}
fn sorted_list_to_bst(head: Option<Box<ListNode>>) -> Option<Rc<RefCell<TreeNode>>> {
    // 定义函数/方法 sorted_list_to_bst
    let mut nodes: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut nodes: Vec<i32>
    let mut cur = &head; // 把 按位与 头节点; 写入 let mut cur
    while let Some(n) = cur {
        // 边取边处理，取空即停
        nodes.push(n.val); // 把 元素个数.值 压入栈/数组尾部
        cur = &n.next; // 把 按位与 元素个数.下一个; 写入 当前值
    }
    fn build(nodes: &[i32], left: isize, right: isize) -> Option<Rc<RefCell<TreeNode>>> {
        // 定义函数/方法 build
        if left > right {
            return None;
        } // 若 左边界 超过 右边界 { return None; }
        let mid = left + (right - left) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2 存入 中点
        let root = TreeNode::new(nodes[mid as usize]); // 把 TreeNode::new(nodes[中点 as usize]) 存入 根节点
        root.borrow_mut().left = build(nodes, left, mid - 1); // 把 build(nodes, 左边界, 中点 减 1); 写入 左边界
        root.borrow_mut().right = build(nodes, mid + 1, right); // 把 build(nodes, 中点 加 1, 右边界); 写入 右边界
        Some(root) // Some(根节点)
    }
    if nodes.is_empty() {
        None
    } else {
        build(&nodes, 0, nodes.len() as isize - 1)
    }
}
fn inorder(n: Option<&Rc<RefCell<TreeNode>>>, out: &mut Vec<i32>) {
    // 定义函数/方法 inorder
    let node = match n {
        Some(x) => x,
        None => return,
    };
    let nb = node.borrow(); // 把 节点.borrow() 存入 nb
    inorder(nb.left.as_ref(), out); // inorder(nb.左边界.as_ref(), out);
    out.push(nb.val); // 把 nb.值 压入栈/数组尾部
    inorder(nb.right.as_ref(), out); // inorder(nb.右边界.as_ref(), out);
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(sorted_list_to_bst(None).is_none()); // 断言校验
    let t = sorted_list_to_bst(build_list(&[1, 2, 3])); // 把 sorted_list_to_bst(build_list( 按位与 [1, 2, 3])) 存入 另一字符串
    let mut out = Vec::new(); // 把 Vec::new(); 写入 let mut out
    inorder(t.as_ref(), &mut out); // inorder(另一字符串.as_ref(), 按位与 mut out);
    assert_eq!(out, vec![1, 2, 3]); // 断言校验
                                    // 结构验证：[1,2,3] 中点 2 为根
    let mut lvl = std::collections::VecDeque::new(); // 把 std::collections::VecDeque::new(); 写入 let mut lvl
    lvl.push_back(t.clone().unwrap()); // lvl 追加 另一字符串.clone().unwrap());
    let mut flat = Vec::new(); // 把 Vec::new(); 写入 let mut flat
    while let Some(n) = lvl.pop_front() {
        // 边取边处理，取空即停
        let nb = n.borrow(); // 把 元素个数.borrow() 存入 nb
        flat.push(nb.val); // 把 nb.值 压入栈/数组尾部
        if let Some(c) = nb.left.clone() {
            lvl.push_back(c);
        } // 若 let Some(字符) 赋值为 nb.左边界.clone() { lvl 追加 字符); }
        if let Some(c) = nb.right.clone() {
            lvl.push_back(c);
        } // 若 let Some(字符) 赋值为 nb.右边界.clone() { lvl 追加 字符); }
    }
    assert_eq!(flat, vec![2, 1, 3]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
