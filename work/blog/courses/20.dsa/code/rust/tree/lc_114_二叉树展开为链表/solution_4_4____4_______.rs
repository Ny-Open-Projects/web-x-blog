// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135637716
// LeetCode 114. 二叉树展开为链表 — Rust 版（方案4）
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

fn flatten(root: Option<Rc<RefCell<TreeNode>>>) {
    // 定义函数/方法 flatten
    let mut prev: Option<Rc<RefCell<TreeNode>>> = None; // 把 None; 写入 let mut prev: Option<Rc<RefCell<TreeNode>>>
    fn dfs(node: Option<Rc<RefCell<TreeNode>>>, prev: &mut Option<Rc<RefCell<TreeNode>>>) {
        // 定义函数/方法 dfs
        let n = match node {
            Some(x) => x,
            None => return,
        };
        dfs(n.borrow().right.clone(), prev); // dfs(元素个数.borrow().右边界.clone(), 前一个);
        dfs(n.borrow().left.clone(), prev); // dfs(元素个数.borrow().左边界.clone(), 前一个);
        let mut nb = n.borrow_mut(); // 把 元素个数.borrow_mut(); 写入 let mut nb
        nb.right = prev.take(); // 把 前一个.take(); 写入 右边界
        nb.left = None; // 把 None; 写入 左边界
        drop(nb); // drop(nb);
        *prev = Some(n);
    }
    dfs(root, &mut prev); // dfs(根节点, 按位与 mut 前一个);
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let t = build_tree(&[Some(1), Some(2), Some(5), Some(3), Some(4), None, Some(6)]);
    flatten(t.clone()); // flatten(另一字符串.clone());
    let mut cur = t; // 把 另一字符串; 写入 let mut cur
    let mut got = Vec::new(); // 把 Vec::new(); 写入 let mut got
    while let Some(n) = cur {
        // 边取边处理，取空即停
        let nb = n.borrow(); // 把 元素个数.borrow() 存入 nb
        assert!(nb.left.is_none(), "left must be null"); // 断言校验
        got.push(nb.val); // 把 nb.值 压入栈/数组尾部
        cur = nb.right.clone(); // 把 nb.右边界.clone(); 写入 当前值
    }
    assert_eq!(got, vec![1, 2, 3, 4, 5, 6]); // 断言校验
    let t2 = build_tree(&[Some(7)]); // 把 build_tree( 按位与 [Some(7)]) 存入 t2
    flatten(t2.clone()); // flatten(t2.clone());
    let mut got2 = Vec::new(); // 把 Vec::new(); 写入 let mut got2
    let mut cur2 = t2; // 把 t2; 写入 let mut cur2
    while let Some(n) = cur2 {
        got2.push(n.borrow().val);
        cur2 = n.borrow().right.clone();
    } // 边取边处理，取空即停
    assert_eq!(got2, vec![7]); // 断言校验
    let none: Option<Rc<RefCell<TreeNode>>> = None; // 把 None; 写入 let none: Option<Rc<RefCell<TreeNode>>>
    flatten(none); // flatten(none);
    println!("PASS"); // 全部用例通过，输出 PASS
}
